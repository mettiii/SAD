from odoo import http
from odoo.http import request
from werkzeug.exceptions import BadRequest


class CandidatePortal(http.Controller):

    @http.route('/exam/login', type='http', auth='public', website=True)
    def exam_login(self, error=None, **kwargs):
        return request.render('Exam_Management.exam_login_template', {
            'error': error
        })

    @http.route('/exam/authenticate', type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def exam_authenticate(self, **post):
        username = post.get('username')
        password = post.get('password')

        try:
            uid = request.session.authenticate(request.db, username, password)
            if uid:
                return request.redirect('/exam/dashboard')
            else:
                return request.redirect('/exam/login?error=credentials')

        except BadRequest as e:
            if 'invalid CSRF token' in str(e):
                return request.redirect('/exam/login?error=csrf')
            else:
                raise
        except Exception:
            return request.redirect('/exam/login?error=credentials')

    @http.route('/exam/dashboard', type='http', auth='user', website=True)
    def exam_dashboard(self, **kwargs):
        user = request.env.user

        # Look for exam.taker (external user)
        exam_taker = request.env['exam.taker'].sudo().search([
            ('user_id', '=', user.id)
        ], limit=1)

        # Look for internal employee
        employee = request.env['hr.employee'].sudo().search([
            ('user_id', '=', user.id)
        ], limit=1)

        # Get assigned exams
        if exam_taker:
            assigned_exams = exam_taker.exam_ids.sudo()
        elif employee:
            assigned_exams = request.env['exam.management'].sudo().search([
                ('assigned_employees', 'in', employee.id)
            ])
        else:
            assigned_exams = []

        return request.render('Exam_Management.exam_dashboard_template', {
            'user': user,
            'employee': employee,
            'exam_taker': exam_taker,
            'assigned_exams': assigned_exams,
            'is_hr': user.has_group('Exam_Management.group_exam_hr_admin'),
            'is_examiner': user.has_group('Exam_Management.group_exam_examiner'),
            'is_candidate': user.has_group('Exam_Management.group_exam_candidate'),
        })

    @http.route('/my/exams/<int:exam_id>/start', type='http', auth='user', website=True)
    def start_exam(self, exam_id, **kwargs):
        user = request.env.user

        # Get employee securely
        employee = request.env['hr.employee'].sudo().search([('user_id', '=', user.id)], limit=1)
        exam = request.env['exam.management'].sudo().browse(exam_id)

        # Security: Only assigned employees can access
        if employee and employee not in exam.assigned_employees:
            return request.render("website.403")

        # If exam_taker model is used for external users
        exam_taker = request.env['exam.taker'].sudo().search([('user_id', '=', user.id)], limit=1)
        if exam_taker and exam not in exam_taker.exam_ids:
            return request.render("website.403")

        return request.render('Exam_Management.exam_paper_template', {
            'exam': exam,
            'questions': exam.question_ids.sudo(),
            'employee': employee,
            'user': user,
        })