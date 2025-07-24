from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ExamQuestion(models.Model):
    _name = 'exam.question'
    _description = 'Exam Questions'

    # Optional reference to batch import or display wizard (if used)
    display_id = fields.Many2one('exam.question.display', string='Question Display', ondelete='set null')
    import_wizard_id = fields.Many2one('exam.question.import.wizard', string="Import Wizard")
    mark = fields.Float(string="Mark", required=True)
    department_id = fields.Many2one('hr.department', string="Department", tracking=True)
    upload_file = fields.Binary(string="Upload CSV File")
    question_ids = fields.One2many(
        'exam.question',
        'import_wizard_id',
        string="Imported Questions",
        readonly=True,
    )

    name = fields.Text(string='Question Text', required=True)
    question_type = fields.Selection([
        ('true_false', 'True/False'),
        ('multiple_choice', 'Multiple Choice'),
        # ('matching', 'Matching'),
        ('essay', 'Essay'),
    ], string='Question Type', required=True)

    # Fields for different question types
    true_false_answer = fields.Selection([('True', 'True'), ('False', 'False')], string='True/False Answer')
    essay_answer = fields.Text(string='Expected Essay Answer')

    option_a = fields.Char(string='Option A')
    option_b = fields.Char(string='Option B')
    option_c = fields.Char(string='Option C')
    option_d = fields.Char(string='Option D')
    correct_ans = fields.Char(string="Correct Answer")

    # match_question = fields.Char(string='Column A')
    # match_answer = fields.Char(string='Column B')

    exam_type = fields.Selection([
        ('recruitment', 'Recruitment'),
        ('promotion', 'Promotion'),
        ('psychometric', 'Psychometric Assessments'),
    ], string="Exam Type", tracking=True)

    job_grade = fields.Selection([
        ('junior', 'Junior'),
        ('mid', 'Mid-Level'),
        ('senior', 'Senior'),
        ('executive', 'Executive')
    ], string="Job Grade", tracking=True)

    job_role = fields.Selection([
        ('acc', 'Accountant'),
        ('it', 'IT'),
        ('secretary', 'Secretary')
    ], string="Job Role", tracking=True)

    exam_ids = fields.Many2many('exam.management', string='Used In Exams')

    @api.constrains('question_type')
    def _check_required_fields_by_type(self):
        for record in self:
            if record.question_type == 'true_false' and not record.correct_ans:
                raise ValidationError("True/False answer must be provided.")
            if record.question_type == 'multiple_choice':
                if not any([record.option_a, record.option_b, record.option_c, record.option_d]):
                    raise ValidationError("At least one multiple choice option must be filled.")
                if not record.correct_ans:
                    raise ValidationError("Correct answer must be set for multiple choice questions.")
            # if record.question_type == 'matching':
            #     if not record.match_question or not record.match_answer:
            #         raise ValidationError("Matching question and answer must be provided.")

