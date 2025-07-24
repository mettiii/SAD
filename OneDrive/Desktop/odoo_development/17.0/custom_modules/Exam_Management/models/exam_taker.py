from odoo import models, fields, api

class ExamTaker(models.Model):
    _name = 'exam.taker'
    _description = 'Exam Taker'

    name = fields.Char(required=True)
    user_id = fields.Many2one('res.users', string='Portal User', required=True, ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', string='Linked Employee')
    exam_ids = fields.Many2many('exam.management', string='Assigned Exams')
    is_employee = fields.Boolean(string="Is Employee", compute="_compute_is_employee", store=True)

    @api.depends('employee_id')
    def _compute_is_employee(self):
        for record in self:
            record.is_employee = bool(record.employee_id)
