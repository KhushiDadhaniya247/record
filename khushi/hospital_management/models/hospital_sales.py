from odoo import api,fields,models

class Sales(models.Model):
    _name = "hospital.sales"
    _description = "Hospital sales Information"
    _order = "name"

    name = fields.Char(string="Name",required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')],string="Gender")
    price = fields.Float(string="Price")
    medicine = fields.Char(string="Medicine")
    note = fields.Html(string="Note")
    date = fields.Date(string="Date")
    patient_id = fields.Many2one("hospital.patient",string="Hospital Patient")
    sales_count = fields.Integer(string="Sales count")


    def action_doctor(self):
        return{
            'type':'ir.actions.act_window',
            'name':'Doctor',
            'res_model':'hospital.octor',
            'domain':[('sales_count','=',self.id)],
            'view_mode':'tree,form',
            'target':'current',

        }
