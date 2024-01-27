from odoo import fields,models

class Divison(models.Model):
	_name = "divison.divison"
	_description = "Divison"
	_order = "name"

	name=fields.Char(string="Divison",required=True)
	standard_id =fields.Many2one('standard.standard',string='standard',readonly=True)
	



