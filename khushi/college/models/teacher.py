from odoo import api,fields,models
from datetime import datetime
from odoo.exceptions import ValidationError,UserError



class Teacher(models.Model):
    _name = "teacher.teacher"
    _description = "Teacher Information"
    _rec_name = "name"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    is_teacher = fields.Boolean(string="Is Teacher")
    status = fields.Selection([('married','Married'),('unmarried','Unmarried')], string="Status", default="unmarried")
    reg_time = fields.Datetime(string="Regestration Time",default=datetime.now())
    rank = fields.Float(string="Rank")
    address = fields.Text(string="Address")
    email = fields.Char(string="Email")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')], string="Gender" , default="female")
    contact = fields.Char(string="Contact")
    student_ids = fields.Many2many("student.student",string="Student")
    student_ids = fields.One2many('student.student', 'teacher_id', string="Students")
    partner_name = fields.Char(string="Partner Name")
    state = fields.Selection([('new','New'),('active','Active'),('regine','Regine')],string='State',default='new')
    student_count = fields.Integer(string="Student Count" ,compute="compute_student_count")
    salary = fields.Float(string="Salary")
    partner_id = fields.Many2one('res.partner',string="Partner")
    image_1920 = fields.Binary("Image") 
    salary_ids = fields.One2many("salary.salary","teacher_id",string="Salary")
    student_id = fields.Many2one("student.student",string="Students")


    def compute_student_count(self):
        for rec in self:
            rec.student_count = self.env['student.student'].search_count([('teacher_id','=',self.id)])

    @api.constrains('email')
    def _check_email(self):
        if self.email:    
            if self.email != '@':
                raise ValidationError('Please enter @ then correct email')



    def unlink(self):
        for student in self:
            if student.gender == 'female':
                raise UserError("Female recod can't be deleted")
        return super(Student, self).unlink()


    def action_new(self):
        self.state='new'
        print("clicked on button")

    def action_active(self):
        self.state='active'
        print("clicked on button")

    def action_regine(self):
        self.state='regine'
        print("clicked on button")

    def action_student(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Students',
            'res_model':'student.student',
            'view_type':'tree,form',
            'domain':[('teacher_id','=',self.id)],
            'view_mode':'tree,form',
            'target':'current',
        }

    def view_student(self):
        print("\n\n\n\n\nself.:::::;",self.student_ids)
        return {
            'name': 'Student',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_type': 'tree',
            'res_model': 'student.student',
            # 'domain': [('id', 'in', self.subject_ids.ids)],
            'target': 'new'
        }



