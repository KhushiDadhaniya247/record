from odoo import api,fields,models

class Salary(models.Model):
    _name = "salary.salary"   
    _description = "Salary"

    date = fields.Date("Date")
    teacher_id = fields.Many2one("teacher.teacher",string="Teacher Id",required=True)
    total_salary = fields.Float("salary")
    tax = fields.Float("Tax")
    net_salary = fields.Float("Net Salary",compute="_compute_total",store=True)


    @api.depends('total_salary', 'tax')
    def _compute_total(self):
      for fl in self:
          fl.net_salary = fl.total_salary - (fl.total_salary * fl.tax) / 100