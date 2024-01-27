from odoo import fields,models,api

class Lead(models.Model):
	_inherit = "crm.lead"


	pyment = fields.Selection([('case','Case'),('online','Online')],string="Pyment Method")