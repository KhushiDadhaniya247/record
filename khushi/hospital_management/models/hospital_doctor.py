from odoo import api,fields,models

class Doctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor Information"
    _order = "name"

    name = fields.Char(string="Name",required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')],string="Gender")

    user_id = fields.Many2one('res.users',string="User")
    patient_id = fields.Many2one("hospital.patient",string="Hospital patient")
    appointment_count = fields.Integer(string="Appointment Count", compute="compute_appointment_count")
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancle','Cancle')]
        , string="Status", default="draft") 
    sales_id = fields.Many2one('hospital.sales',string="Hospital Sales")


    def compute_appointment_count(self):
        for record in self:
            record.appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', self.id)])
            # record.appointment_count = appointment_count

    
    @api.onchange('patient_id')
    def onchange_gender(self):
        if self.patient_id:
            self.gender = self.patient_id.gender

    def action_draft(self):
        self.state = 'draft'
        print("clicked on button")


    def action_done(self):
        self.state = 'done'
        print("clicked on button")


    def action_confirm(self):
        self.state = 'confirm'
        print("clicked on button")


    def action_cancle(self):
        self.state = 'cancle'
        print("clicked on button")
