from odoo import fields, models

class Standard(models.Model):
	_name = "standard.standard"
	_description = "Standard"
	_order = "name"

	name = fields.Integer(string="Standard",required=True)
	divison_ids = fields.One2many('divison.divison','standard_id',string='divison')
	# subject_ids = fields.Many2many('subject.subject', 'standard_subject_relation', 'standard_id', 'subject_id', string='Subjects')
	subject_ids = fields.Many2many("subject.subject", "standard_subject_relation", 'standard_id', 'subject_id', string="Subjects")
