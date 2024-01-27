from odoo import api,fields,models,_
import datetime
from odoo.exceptions import ValidationError 
# from dateutil.relativedelta import relativedelta
# from datetime import date

class Student(models.Model):
    _name = "student.student"   
    _description = "Student Information"
    # _order = "name"
    _rec_name = "name"

    name = fields.Char(string="Name",required=1)
    rollnumber = fields.Integer(string="Roll Number")
    email = fields.Char(string="Email")
    standard = fields.Char(string="Standard")
    is_student = fields.Boolean(string="Is Student" ,default=True)
    address = fields.Text(string="Address")
    dob = fields.Date(string="Date Of Birth",)
    age = fields.Char(string="Age",compute="_get_age_from_student")  #defalut=4
    gender = fields.Selection([
      ('male','Male'),
      ('female','Female'),
      ('other','Other')], string="Gender")
    reg_time = fields.Datetime(string="Regestration Time")
    date = fields.Date(string="Date")
    contact = fields.Char(string="Contact", placeholder="+91")
    teacher_id = fields.Many2one('teacher.teacher', string="Teacher")
    binary = fields.Binary(string="Image")
    subject = fields.Char(string="Subject")
    partner_id = fields.Many2one('res.partner',string="Partner")
    active = fields.Boolean(string="Active" ,default=True)
    subject_id = fields.Many2one("subject.subject",string="subjects")
    result_ids = fields.One2many("result.result","student_id",string="Result")
    teacher_count = fields.Integer(string="Teacher Count" ,compute="compute_teacher_count")


    def compute_teacher_count(self):
        for rec in self:
            rec.teacher_count = self.env['teacher.teacher'].search_count([('student_id','=',self.id)])


    # def search_read(self):
    #     rec = self.env['student.student'].search([('gender','=','male')])
    #     print("\n\nrec===================",rec)
        
    # @api.model_create_multi
    # def create(self,vals_list):
    #     for vals in vals_list:
    #         if vals.get('name',_('New')) == ('New'):
    #             vals['name'] = self.env['ir.sequence'].next_by_code('student.student') or _('New')
    #     return super(Student,self).create(vals_list)

    # ex=1(name_get() Method)

    # def name_get(self):
    #     res = []
    #     for student in self:
    #         res.append((student.id, "%s - %s" % (student.name, student.gender)))
    #     return res

    # ex=2

    def name_get(self):
        res=[]
        for student in self:
            res.append((student.id,"%s - %s" % (student.name,student.is_student)))
        return res

    # @api.constrains('dob')
    # def _check_dob(self):
    #     for rec in self:
    #         print("....TODAY........",fields.Date.today())
    #         print("...........REC DOB...........",rec.dob)
    #         if rec.dob > fields.Date.today():
    #             raise ValidationError("The Entered date of birth is not acceptable!")

    # def write (self,vals):
    #     print("write method is triggered")
    #     return super(Student,self).write(vals)


    def _get_age_from_student(self):
        today_date = datetime.date.today()
        for stud in self:
            if stud.dob:
                dob = fields.Datetime.to_datetime(stud.dob).date()
                total_age = str(int((today_date - dob).days / 365))
                stud.age = total_age
            else:
                stud.age = "not providated"

    @api.onchange('patient_id')
    def _onchange_partner_id(self):
        self.write({
            'email':self.partner_id.email,
            'contact':self.partner_id.contact
            })
    
    @api.onchange('teacher_id.email','teacher_id')
    def _onchange_email(self):
        self.email = self.teacher_id.email
    # @api.onchange('standard','is_student')
    # def onchange(self):
    #     if self.standard == 0:
    #         self.is_student = False

    

    # @api.model_create_multi
    # def create(self,vals_list):
    #     for vals in vals_list:
    #         if vals.get('name', _('New')) == _('New'):
    #             vals['name'] = self.env['ir.sequence'].next_by_code('student.student') or _('New')
    #     return super(Student, self).create(vals_list)

    def action_teacher(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Teacher',
            'res_model':'teacher.teacher',
            'view_type':'tree,form',
            'domain':[('student_id','=',self.id)],
            'view_mode':'tree,form',
            'target':'current',
        }