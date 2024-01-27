from odoo import api,fields,models,_

class Subject(models.Model):
    _name = "subject.subject"
    _description = "Subject Information"
    

    name = fields.Char(string="Subject Name")   
    teacher_id = fields.Many2one("teacher.teacher",string="Teacher")
    teachers_id = fields.Many2many("teacher.teacher",string="Teachers")
    students_ids= fields.One2many("student.student","subject_id",string="subjects")
    # squ = fields.Char(string="squ" ,readonly=True)


    # squ = fields.Char(string="squ" ,readonly=True)


    # @api.model_create_multi

    # def create(self,vals):
    #     vals['squ'] = self.env['ir.sequence'].next_by_code('my.sequence.code')
    #     return super(Car_Management, self).create(vals)
