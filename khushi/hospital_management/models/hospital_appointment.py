from odoo import api,fields,models
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment Information"
    _order = "patient_id"

    name = fields.Char(string="Name",required=True, tracking=True)
    patient_id = fields.Many2one("hospital.patient",string="Hospital Patient")
    doctor_id = fields.Many2one("hospital.doctor",string="Hospital Doctor")
    note = fields.Html(string="Note")
    appointment_date = fields.Datetime(string="Appointment Date")
    appointment_lines_ids = fields.One2many("hospital.appointment.lines","appointment_id",string="Appointment line")
    age= fields.Integer(related='patient_id.age',string='Age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')],tracking=True)
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancle','Cancle')]
        , string="Status", default="draft")


    @api.onchange('patient_id')
    def onchange_gender(self):
        if self.patient_id:
            self.gender = self.patient_id.gender
            # self.note = self.patient_id.note

    @api.constrains('name')
    def _check_name(self):
        # if self.name:
        #     if self.name == self.name:
        #         raise ValidationError("name %s is a already exists" % (self.name))
        name_rec = self.env['hospital.appointment'].search([('name','=',self.name), ('id', '!=', self.id)])
        if name_rec:
            raise ValidationError("Name %s is a already exists" % (self.name))

        # record = self.search([(self.name, '==', self.name)])
        #     raise ValidationError("name %s is a already exists" % (self.name))


    def default_get(self, fields_list):
        res = super(HospitalAppointment, self).default_get(fields_list)
        res['patient_id'] = 4
        res['note'] = 'I am khsuhi' 
        return res
        



    def action_draft(self):
        self.state = 'draft'
        print("clicked on button")

    def action_confirm(self):
        self.state = 'confirm'
        appointment = self.env['hospital.appointment``'].search_count([])
        print("Appointment----------->",appointment)

        # print("clicked on button")

    def action_done(self):
        self.gender = "female"
        print("clicked on button")

    def action_cancle(self):
        self.state = 'cancle'
        print("clicked on button")


    # def name_get(self):
    #     res = []
    #     for student in self:
    #         res.append((student.id, "%s - %s" % (student.name, student.zender)))
    #     return res

    def unlink(self):
         # if self.state == "done":
         raise ValidationError("You can not deleted %s as it is %s state" % (self.name, self.state)) 
         return super(HospitalAppointment, self).unlink()





class HospitalAppointmentLines(models.Model):
    _name = "hospital.appointment.lines"
    _description = 'Hospital Appointment  Line information'

    product_id = fields.Many2one("product.product",string="Product")
    product_qty = fields.Integer(string="Qty")
    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")