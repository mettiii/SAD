from odoo import models, fields, api, _

class ExamAnswer(models.Model):
    _name = 'exam.answer'
    _description = 'Candidate Answer'

    display_id = fields.Many2one('exam.question.display', string="Display Link")
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    question_id = fields.Many2one('exam.question', string="Question", required=True)

    selected_option = fields.Char(string="Selected Option")  # A, B, C, D or True/False
    essay_response = fields.Text(string="Essay Answer")

    # Automatically computed for MCQ/True-False
    is_correct = fields.Boolean(string="Is Correct", compute="_compute_is_correct", store=True)

    # Manual grading for essays
    essay_score = fields.Float(string="Essay Score", help="Score given by evaluator for essay questions")
    is_essay_graded = fields.Boolean(string="Essay Graded", default=False)

    # Optional: make view logic easier
    is_essay_question = fields.Boolean(string="Is Essay Question", compute="_compute_is_essay_question", store=False)

    @api.depends('question_id.question_type', 'selected_option', 'question_id.correct_ans', 'question_id.true_false_answer')
    def _compute_is_correct(self):
        for rec in self:
            q = rec.question_id
            if q.question_type == 'multiple_choice':
                rec.is_correct = (rec.selected_option or '').strip().lower() == (q.correct_ans or '').strip().lower()
            elif q.question_type == 'true_false':
                rec.is_correct = (rec.selected_option or '').strip().lower() == (q.true_false_answer or '').strip().lower()
            else:
                rec.is_correct = False  # Essay and others are manually graded

    @api.depends('question_id.question_type')
    def _compute_is_essay_question(self):
        for rec in self:
            rec.is_essay_question = rec.question_id.question_type == 'essay'
