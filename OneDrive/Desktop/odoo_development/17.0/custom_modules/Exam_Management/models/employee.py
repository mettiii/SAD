from odoo import models, fields, api, _


class Employee(models.Model):
    _inherit = 'hr.employee'

    image_1920 = fields.Binary("Image", attachment=True)
    bank_branch = fields.Char(string="Bank Branch")
    employee_code = fields.Char(string="Employee ID")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", required=False)
    dob = fields.Date(string="Date of Birth")
    job_grad = fields.Selection([
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
    exam_user_role = fields.Selection([
        ('hr_admin', 'HR Admin'),
        ('examiner', 'Examiner'),
        ('candidate', 'Candidate'),
    ], string="Exam Role")
    password = fields.Char(string="Password")
    login = fields.Char(string="Login", required=True)
    email = fields.Char(string="Email")
    groups_id = fields.Many2many('res.groups', 'hr_employee_groups_rel', 'employee_id', 'group_id',
                                 string="Access Groups")
    lang = fields.Selection(
        selection=lambda self: self.env['res.lang'].get_installed(),
        string="Language",
        default=lambda self: self.env.user.lang,
    )
    tz = fields.Selection(
        selection='_tz_get',
        string='Timezone',
        default=lambda self: self.env.user.tz,
        help="The user's timezone.",
    )

    exam_result_ids = fields.One2many(
        'exam.result',
        'employee_id',
        string="Exam Results"
    )

    user_id = fields.Many2one('res.users', string="Related User", ondelete='set null')

    @api.model
    def _tz_get(self):
        return [(tz, tz) for tz in fields.Selection._tz_get()]

    @api.model
    def create(self, vals):
        role = vals.get('exam_user_role')
        user_vals = {}

        if vals.get('login') and vals.get('password'):
            user_vals = {
                'name': vals.get('name', 'New User'),
                'login': vals['login'],
                'password': vals['password'],
            }

            # Assign group based on selected role
            group_ids = []
            if role:
                group = self._get_exam_group_by_role(role)
                if group:
                    group_ids.append((6, 0, [group.id]))
            if group_ids:
                user_vals['groups_id'] = group_ids

            user = self.env['res.users'].create(user_vals)
            vals['user_id'] = user.id
            vals.pop('password')
            vals.pop('image', None)
        return super(Employee, self).create(vals)

    def write(self, vals):
        for rec in self:
            user = rec.user_id
            role = vals.get('exam_user_role')
            if user and role:
                group = self._get_exam_group_by_role(role)
                if group:
                    user.groups_id = [(6, 0, [group.id])]
        return super(Employee, self).write(vals)

    def _get_exam_group_by_role(self, role):
        group_map = {
            'hr_admin': 'Exam_Management.group_exam_hr_admin',
            'examiner': 'Exam_Management.group_exam_candidate',
            'candidate': 'Exam_Management.group_exam_candidate',
        }
        return self.env.ref(group_map.get(role))
