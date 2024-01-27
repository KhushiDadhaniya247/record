from odoo import fields,api,models

class ErpPartner(models.Model):
    _inherit = "res.partner"


    crm = fields.Selection([
        ('zoho','Zoho'),
        ('salesforce','Salesforce'),
        ('hubspot','Hubspot'),
        ('clickup','Clickup'),
        ('sap','SAP'),
        ('other','Other')],string="CRM:")