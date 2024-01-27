from odoo import api,fields,models

class Result(models.Model):
    _name = "result.result"   
    _description = "Student Result"

    student_id = fields.Many2one("student.student",string="Student Id")
    subject_id = fields.Many2one("subject.subject",string="Subject Id")
    marks = fields.Char("Marks")

