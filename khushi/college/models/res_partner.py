from odoo import api,fields,models,_


class Partner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean("Student", default=True)
    student_ref = fields.Char("Stud REF")
    phone = fields.Char("Phone",required=True)
    mobile = fields.Char(" Mobile")
    # is_teacher = fields.Boolean(string="Teacher",default=True)
    state = fields.Selection([('draft','Draft'),('register','Register')], string="Status", default="draft")


    def action_draft(self):
        self.state = 'draft'
        print("clicked on button")

    def action_register(self):
        self.state = 'register'
        print("clicked on button")
