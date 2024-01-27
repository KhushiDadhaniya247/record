from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime



class Student(models.Model):
    _name = "student.student"
    _description = "Student Information"
    _order = 'name'
    _rec_name = 'name'

    # partner_id = fields.Many2one('res.partner')
    name = fields.Char("Student Name", required=1)
    rollnumber = fields.Integer(string="Roll Number")
    email = fields.Char(string="Email")
    is_student = fields.Boolean("Student", default=True)
    dob = fields.Date("Date Of Birth", help="Please enter date of birth")
    address = fields.Text("Address")
    # def name_get(self):
    #     res = []
    #     for student in self:
    #         res.append((student.id, "%s - %s" % (student.name, student.zender)))
    #     return res
    age=fields.Float(string="Age")
    active = fields.Boolean('Active', default=True)
    zender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')], string="Zender", default='male')
    reg_time = fields.Datetime('Regestration Time')
    binary = fields.Binary(string="Image")
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),
                            ('close','Close'),('done','Done')],string="Status",default='draft')
    taxt_note = fields.Html(string="Note")
    percentage = fields.Float(string='Percentage', required=True, default=100.0)
    contact = fields.Char(string="Contact")


    ### Relational
    standard_id = fields.Many2one('standard.standard', string="Standard")
    teacher_id = fields.Many2one('teacher.teacher', string="Teacher") #, readonly=True
    subject_ids = fields.Many2many("subject.subject", "student_subject_relation", 'student_id', 'subject_id', string="Subjects")
    teacher_ids = fields.Many2many("teacher.teacher", string="Teachers")


    divison_id = fields.Many2one("divison.divison",string="Divison")

    # _sql_constraints = [
    # ('email_unique', 'UNIQUE(email)', 'Please enter unique email'),
    # ('check_age', 'CHECK(age < 10.0)', 'Please enter age above 18')
    # ]

    _sql_constraints = [
        ('check_age', 'CHECK(percentage >= 0 AND percentage <= 100)',
         'The percentage of an analytic distribution should be between 0 and 100.'),
        ('check_age', 'CHECK(age <= 18.0)', 'Please enter age above 18'),
        # ('check_contact','CHECK(contact >= 10 AND contact <=10)''Please enter correct contact number')
    ]

    # @api.constrains('dob')
    # def _check_dob(self):
    #     if self.dob:
    #         if self.dob > datetime.now().date():
    #             raise UserError('Date of birth can not be entered future date.')

    @api.constrains('contact')
    def _check_contact(self):
        if self.contact:    
            if len(self.contact) != 10:
            # if len(self.contact) >= 10 and len(self.contact) <= 10:
                raise ValidationError('Please enter corrrect contact number')

    @api.onchange('teacher_id.email','teacher_id')
    def _onchange_email(self):
        self.email = self.teacher_id.email

    @api.onchange('zender')
    def onchange_zender(self):
        if self.zender == 'female':
            self.is_student = False

    # @api.onchange('zender_set')
    # def onchange_zender(self):
    #     if self.action_zender_set:
    #         self.zender = 'other'


    def name_get(self):
        res = []
        for student in self:
            res.append((student.id, "%s - %s" % (student.name, student.zender)))
        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name :
            args += ['|', ('name', operator, name), ('address', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    def action_confirm(self):
        # self.write({'state': 'confirm'})
        patient = self.env['student.student'].search([])
        print("patient--------------->",patient)
        female = self.env['student.student'].search([('zender','=','female')])
        print("Female--------------->",female)
        male = self.env[student.student].search([('zender','=','male')])
        print("Male-------------->",male)

    # 2nd up ^
    # def action_confirm(self):
    #     self.state = 'confirm'
    #     if not self.env.context.get('set_zender'):
    #         self.zender = 'female'
    #     else:
    #         self.zender = 'other'
        # female_students = self.search([('zender', '=', 'female')])
        # female_students.age = 5

        # total_female_students = self.search_count([('zender', '=', 'female')])

        # print("\n\n\n\n\n\nfemal_Students:::::::::::::::",female_students, total_female_students)

        # self.env['teacher.teacher'].create({
        #     'name':'Diya',
        #     'is_teacher':True,
        #     'married':'unmarried',
        #     'zender':'female'
        #     })
    # 

    def view_subjects(self):
        print("\n\n\n\n\nself.:::::;",self.subject_ids)
        return {
            'name': 'Subjects',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_type': 'tree',
            'res_model': 'subject.subject',
            # 'domain': [('id', 'in', self.subject_ids.ids)],
            'target': 'new'
        }

    def action_done(self):
        self.state = 'done'
        print("clicked on button")

    def action_draft(self):
        self.state = 'draft'
        print("clicked on button")

    def action_close(self):
        self.state = 'close'
        print("clicked on button")

    def action_zender_set(self):
        self.zender = 'other'
        print("dhsjkfjkj")



    @api.model_create_multi
    def create(self, vals_list):
        "Called when create new record is created"
        "Sql: Insert Into Table name"
        "param: List of Dict"
        "return recordsets"
        # print("\n\n\n\nvals_list:::::::::",vals_list)
        # student = super(Student, self).create(vals_list)


        # self.env['teacher.teacher'].create({
        #     'name': 'Sudhir Arya',
        #     'address': 'Navrangpura',
        #     'is_teacher': True
        #     })


        # print("\n\n\n\nstudent::::::::",student, type(student.id))
        # # student.write({'name': 'ST00' + str(student.id)})
        # return student
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('student.student') or _('New')
        return super(Student, self).create(vals_list)


    def write(self, vals):
        "Called when existing record is updated"
        "Sql: update table_name set name='ddasds' where id=3 "
        "return True"
        # print("\n\n\n\nvals::::::",vals)
        # student = super(Student, self).write(vals)
        # print("\n\n\n\n\nstudent::::::;", student)
        # return student
        student = super(Student,self).write(vals)
        print("\n\n\n\n::::::::::::::::",vals)
        if vals.get('state') == 'confirm':
            self.age = 0

        return student 



    def unlink(self):
        "Called when existing record is deleted "
        "Sql: delete from table_name where id=12"
        "return True"
        for student in self:
            if student.zender == 'female':
                raise UserError("Female recod can't be deleted")
        return super(Student, self).unlink()

    def copy(self):
        "Called when record is duplicated."
        "It will create the call create method."
        "return New recordset"
        return super(Student, self).copy(default={'dob': datetime.now()})






