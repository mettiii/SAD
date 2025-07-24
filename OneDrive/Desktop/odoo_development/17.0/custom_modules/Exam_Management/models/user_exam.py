# from odoo import models, fields, api
#
# class ExamQuestionDisplay(models.Model):
#     _name = 'exam.question.display'
#     _description = 'Display Exam Questions'
#
#     exam_id = fields.Many2one('exam.management', string='Exam', required=True)
#
#     # Use Many2many computed fields to represent filtered subsets of questions
#     mcq_lines = fields.Many2many(
#         'exam.question',
#         string='Multiple Choice Questions',
#         compute='_compute_question_lines',
#         store=False,
#         compute_sudo=True,
#         readonly=True,
#     )
#     tf_lines = fields.Many2many(
#         'exam.question',
#         string='True/False Questions',
#         compute='_compute_question_lines',
#         store=False,
#         compute_sudo=True,
#         readonly=True,
#     )
#     essay_lines = fields.Many2many(
#         'exam.question',
#         string='Essay Questions',
#         compute='_compute_question_lines',
#         store=False,
#         compute_sudo=True,
#         readonly=True,
#     )
#
#     @api.depends('exam_id.question_ids')
#     def _compute_question_lines(self):
#         for rec in self:
#             if not rec.exam_id:
#                 rec.mcq_lines = False
#                 rec.tf_lines = False
#                 rec.essay_lines = False
#                 continue
#
#             questions = rec.exam_id.question_ids
#             rec.mcq_lines = questions.filtered(lambda q: q.question_type == 'multiple_choice')
#             rec.tf_lines = questions.filtered(lambda q: q.question_type == 'true_false')
#             rec.essay_lines = questions.filtered(lambda q: q.question_type == 'essay')
#
#     def submit_exam(self):
#         """Submit the exam answers and create answer records."""
#         employee = self._get_employee()  # Make sure this method is defined and returns hr.employee record
#         answer_model = self.env['exam.answer']
#
#         for question in self.exam_id.question_ids:
#             # Retrieve posted answer from context or wherever the frontend sets it
#             posted_val = self.env.context.get(f'answer_{question.id}', False)
#             answer_model.create({
#                 'question_id': question.id,
#                 'employee_id': employee.id,
#                 'display_id': self.id,
#                 'selected_option': posted_val,
#             })
#
#         return {
#             'type': 'ir.actions.client',
#             'tag': 'display_notification',
#             'params': {
#                 'title': 'Exam Submitted',
#                 'message': 'Your answers were submitted successfully!',
#                 'type': 'success',
#             }
#         }
