from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ExamQuestionLine(models.Model):
    _name = 'exam.question.line'
    _description = 'Exam Question Line'

    display_id = fields.Many2one('exam.question.display', string='Question Display', ondelete='cascade')
    name = fields.Text(string='Question Text', required=True)

    question_type = fields.Selection([
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('essay', 'Essay'),
        # ('matching', 'Matching'),
    ], string='Question Type', required=True)

    # Multiple Choice fields
    option_a = fields.Char(string='Option A', help="First option for multiple-choice questions.")
    option_b = fields.Char(string='Option B', help="Second option for multiple-choice questions.")
    option_c = fields.Char(string='Option C', help="Third option for multiple-choice questions.")
    option_d = fields.Char(string='Option D', help="Fourth option for multiple-choice questions.")
    correct_ans = fields.Char(string='Correct Answer', help="Specify the correct option (A, B, C, or D).")

    # True/False
    true_false_answer = fields.Selection([
        ('true', 'True'),
        ('false', 'False'),
    ], string='True/False Answer', help="Select either True or False.")

    # Essay
    essay_answer = fields.Text(string='Essay Answer', help="Provide the expected essay answer here.")

    # Matching (commented)
    # match_question = fields.Char(string='Match Question', help="The question to match to an answer.")
    # match_answer = fields.Char(string='Match Answer', help="The answer that corresponds to the match question.")

    @api.constrains('question_type', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_ans',
                    'true_false_answer', 'essay_answer')
    def _check_question_fields(self):
        for record in self:
            if record.question_type == 'multiple_choice':
                if not (record.option_a and record.option_b and record.option_c and record.option_d):
                    raise ValidationError(_("All options (A, B, C, D) must be provided for multiple-choice questions."))
                if not record.correct_ans or record.correct_ans.upper() not in ['A', 'B', 'C', 'D']:
                    raise ValidationError(_("Correct Answer must be one of A, B, C, or D for multiple-choice questions."))
            elif record.question_type == 'true_false':
                if not record.true_false_answer:
                    raise ValidationError(_("A true/false answer must be provided for true/false questions."))
            # elif record.question_type == 'essay':
            #     if not record.essay_answer:
            #         raise ValidationError(_("An essay answer must be provided for essay questions."))
            # # elif record.question_type == 'matching':
            #     if not (record.match_question and record.match_answer):
            #         raise ValidationError(_("Both match question and match answer must be provided for matching questions."))
