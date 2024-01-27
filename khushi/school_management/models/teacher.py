from odoo import api,fields,models, _
from odoo.exceptions import UserError

class Teacher(models.Model):
	_name ="teacher.teacher"
	_description ="Teacher Information"
	_order ="name"

	name=fields.Char(string="Name", default= lambda self: _('New'), readonly=1, required=1)
	age=fields.Integer(string="Age")
	is_teacher=fields.Boolean("Teacher")
	married=fields.Selection([
		('married','Married'),
		('unmarried','Unmarried'),
		])
	reg_time=fields.Datetime(string='Regestration Time')
	rank=fields.Float(string="Rank")
	dob=fields.Date("Date Of Birth")
	address=fields.Text("Address")
	zender=fields.Selection([
		('male','Male'),
		('female','Female'),
		('other','Other')],string='zender',default='female')
	student_ids = fields.One2many('student.student', 'teacher_id', string="Students")

	state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),('close','Close')],string='stuats',default='draft')
	contact = fields.Char(string="Contact Number")
	email = fields.Char(string="Email")

	@api.onchange('married','is_teacher')
	def _onchange_married(self):
	#1 ex.
		if self.married == 'married':
			self.zender = 'female'
    #2
		if self.is_teacher == True:
			self.age = 18

	@api.model
	def _name_search(self, name='', args=None, operator='ilike', limit=100):
		"To search the records based on the typed value in relational fields."
		teachers  = self._search(['|' ,('name', 'ilike', name), ('address','ilike',name)])
		return teachers


	_sql_constraints = [
		('email_unique_contact_unique','UNIQUE(email)','Please enter unique email id and contact number'),
	]

	@api.model_create_multi
	def create(self,vals_list):
		for vals in vals_list:
			if vals.get('name', _('New')) == _('New'):
				vals['name'] = self.env['ir.sequence'].next_by_code('teacher.teacher') or _('New')
		return super(Teacher, self).create(vals_list)
	# 	# teacher=super(Teacher,self).create(vals_list)
	# 	# teacher.write({'is_teacher':True})
	# 	# teacher.is_teacher = True
	# 	# return teacher
    
    
 
	def action_confirm(self):
		self.state='confirm'
		print("\n\n\n\nself.env.context.get('test'):::::::;",self.env.context.get('test'))				
		if not self.env.context.get('test'): #   or   self._context.get('test')
			print("\n\n\n\nself.env.context.get('test'):::::::;",self.env.context.get('test'))				
			teacher = self.search([('is_teacher','=',False)])
			# print("\n\n\n\n\nteacher:::::::::::::::::",teacher)
			teacher.is_teacher = True
		else:
			teacher_t = self.search([('is_teacher','=',True)])
			teacher_t.is_teacher = False
		


	# def action_confirm(self):
	# 	self.state='confirm'
	# 	print("clicked on button")

	def action_draft(self):
		self.state='draft'
		print("clicked on button")

	def action_done(self):
		self.state='done'
		print("clicked on button")

	def action_close(self):
		self.state='close'
		print("clicked on button")

	def write(self,vals_list):
		teacher=super(Teacher,self).write(vals_list)
		return teacher

	def copy(self):
		return super(Teacher, self).copy(default={'address': 'sahibaugh'})

	def unlink(self):
		for teacher in self:
			if teacher.is_teacher == False:
				raise UserError("teacher id is false so record will not be deleted")
			if teacher.married == 'unmarried':
				raise UserError("unmarried record not deleted")
			return super(Teacher,self).unlink()

