from odoo import fields,models


class StudentReport(models.TransientModel):
    _name = "student.report"
    _description = "Student Report"

    teacher_id = fields.Many2one("teacher.teacher",string="Teacher")
    student_id = fields.Many2one("student.student",string="Student")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")


    def action_report_stud(self):
        print("\n\nButton Is Clicked")
        students = self.env['student.student'].search([
            ('dob', '>=', self.start_date),
            ('dob', '<=', self.end_date),
        ])
        print("students----------",students)
        return self.env.ref('college.action_report_student_pdf').report_action(students)


    def report_salary(self):
        print("\n\nbutton is Clicked::==")

        # teachers = self.env['teacher.teacher'].search([
        #     ('salary_ids','>=',self.start_date),
        #     ('salary_ids','<=',self.end_date),


        #     ])
        # print("teachers-------------------",teachers)
        return self.env.ref('college.action_report_student_pdf').report_action(self.teacher_id)
        return self.env.ref('college.action_report_student_pdf').report_action(student_id)



    def salary_teacher(self):
        print("\n\nSalary button is click... ")
        # salary = self.env['salary.salary'].search([
        #     ('date', '>=',self.start_date),
        #     ('date', '<=',self.end_date),
        # ])
        # print("salary----------",salary)
        return self.env.ref('college.action_report_student_pdf').report_action(self.teacher_id)




