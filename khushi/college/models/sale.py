from odoo import models, fields, api



class new_one(models.Model):
    _inherit="sale.order.line"


    new_on=fields.Char("newaddes",compute="_compute_new")


    def _compute_new(self):
        for rec in self:
            rec.new_on=rec.product_template_id

