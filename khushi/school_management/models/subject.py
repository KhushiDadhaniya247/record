from odoo import api,fields,models

class Subject(models.Model):
	_name = "subject.subject"
	_description ="Subjetcs Information"
	_order = "name"


	name = fields.Char(string="Subject Name",required=True)
