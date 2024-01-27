from odoo import api,fields,models,_
from odoo.exceptions import UserError


class Partner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string="Teacher", default=True)
    teacher_ref = fields.Char(string="Teacher Ref")
    rank = fields.Float(string="Rank")

    # def unlink(self):
    #     for Partner in self:
    #         if Partner.is_teacher == True:
    #             raise UserError("recod can't be deleted")
    #     return super(Partner, self).unlink(partner)

    @api.onchange('state_id')
    def _onchange_state(self):
        super(Partner,self)._onchange_state()
        print('\n\n 111111111 MY Method', self.state_id)
        if self.state_id:
            self.zip = '11111'


    @api.onchange('country_id')
    def _onchange_country_id(self):
        super(Partner,self)._onchange_country_id()
        print('\n\n|||||||||||||| HELLO',self.country_id,self.country_id.id)
        if self.country_id.id == 104:
           self.mobile = '+91'
           print('\n\n|||||||||||||| My METHOD',self.country_id)





class TestPartner(models.Model):
    _name = 'test.res.partner'
    _description = "Test Partner"
    _inherits = {'res.partner': 'test_partner_id'}

    test_partner_id = fields.Many2one('res.partner', 'partner')
    is_test = fields.Boolean('Test')
