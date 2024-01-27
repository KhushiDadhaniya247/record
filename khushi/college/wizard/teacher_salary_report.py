from odoo import fields,api,models

class SalaryReport(models.TransientModel):
    _name = "salary.report"
    _description = "Teacher Salary Report"

    teacher_id = fields.Many2one("teacher.teacher",string="Teacher")
    start_salary = fields.Float("Start Salary")
    end_salary = fields.Float("End Salary")



    def salary_report_teacher(self):
        print("\n\nClickkkedddd........")
        teachers = self.env['teacher.teacher'].search([
            ('salary','>=',self.start_salary),
            ('salary','<=',self.end_salary),

        ])
        print("teachers-------------------",teachers)
        return self.env.ref('college.action_teacher_salary_pdf').report_action(teachers)


    # def Report_salary(self):
    #     print("print Clickkkedddd...........")
    #     salary = self.env['teacher.teacher'].search([
    #         ('salary_ids','>=',self.start_salary),
    #         ('salary_ids','<=',self.end_salary),
    #     ])
    #     print("salaryy:::::::::::::::::",salary)
        
    #     return self.env.ref('college.action_teacher_salary_pdf').report_action(salary)            