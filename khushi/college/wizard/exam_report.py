from odoo import fields,api,models

class ExamReport(models.TransientModel):
    _name = "exam.report"
    _description = "Exam Report"


    student_id = fields.Many2one('exam.exam',string="Name")


    def action_exam_popup(self):
      print("clickk on button..")




      return self.env.ref('college.action_exam_report_pdf').report_action(self)



