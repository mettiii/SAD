from odoo import models, fields, api

class ExamResult(models.Model):
    _name = 'exam.result'
    _description = 'Exam Result'

    taker_id = fields.Many2one('exam.takers', string='Exam Taker', required=False)  # Optional if you use hr.employee
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    exam_id = fields.Many2one('exam.management', string='Exam', required=True)
    score = fields.Float(string='Score')
    passed = fields.Boolean(string='Passed', compute='_compute_passed', store=True)
    remarks = fields.Text(string='Remarks')

    @api.depends('score', 'exam_id.passing_score')
    def _compute_passed(self):
        for rec in self:
            passing = rec.exam_id.passing_score or 50.0  # Fallback to 50 if undefined
            rec.passed = rec.score >= passing

    def action_print_scorecard(self):
        return self.env.ref('Exam_Management.action_scorecard_report').report_action(self)

