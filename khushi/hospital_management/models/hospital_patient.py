from odoo import api,models,fields, _
from odoo.exceptions import ValidationError,UserError
from datetime import datetime

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient information'
    _order = 'name'


    name = fields.Char(string= "Patient Name",required=True)
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age")
    date = fields.Date(string="Date")
    amount = fields.Float(string="Amount")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')],string="Gender")
    note = fields.Html(string="Note")
    active = fields.Boolean(string="Active",default=True)
    appointment_count = fields.Integer(string="Appointment Count",compute="compute_appointment_count")
    # state = fields.Selection([('draft','Draft'),('done','Done')
    #                         ('confirm','Confirm'),('cancle','Cancle')],string="Stuts" , default="draft")
    # sales_count = fields.Integer(string="Sales count")


    def compute_appointment_count(self):
        for rec in self:
           rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id','=',self.id)])

    @api.onchange('age','gender')
    def _onchange_age(self):
        if self.age == 22:
            self.gender = "female"


    @api.constrains('dob')
    def _check_dob(self):
        if self.dob:
            if self.dob > datetime.now().date():
                raise UserError('Date of birth can not be entered future date.')

        if self.gender == 'other':
            self.age = 0



    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if vals.get('name',_('New')) == ('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(Patient,self).create(vals_list)


    # @api.constrains('age')
    # def _check_age(self):
        # for rec in self:
        #     if rec.age == 0:
        # if self.age == 0:
        #     raise ValidationError("Age can not be zero")


# default= lambda self: _('New'), readonly=1
    def action_appointment(self):
        return{
            'type':'ir.actions.act_window',
            'name':'Appointment',
            'res_model':'hospital.appointment',
            'domain':[('patient_id','=',self.id)],
            'view_mode':'tree,form',
            'target':'current',


        }


    @api.model_create_multi
    def create(self, vals_list):
        print("vals_list------->",vals_list)
        return super(Patient,self).create(vals_list)

    def write(self,vals):
        print("write method is triggered",vals)
        return super(Patient,self).write(vals)

    def unlink(self):
        print("deleted record--------->%s"%(self.name))
        # if self.gender == 'male':
        return super(Patient,self).unlink()


