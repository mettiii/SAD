from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    is_candidate = fields.Boolean("Is Candidate")
    assigned_exam_id = fields.Many2one('exam.exam', string="Assigned Exam")
