from odoo import api,models

class SalaryTeacher(models.AbstractModel):
	_name = "report.college.report_student_pdf"

	def get_salary(self,docids):
		print("\n\ndocids|||||||",docids)
		for doc in docids:
			salary = self.env['salary.salary'].search([('teacher_id','=',doc)])
			return salary
		return []

	@api.model
	def _get_report_values(self,docids,data=None):
		print("\n\ndocids----------->",docids)
		salary = self.get_salary(docids)
		print("\n\nsalary",salary,salary.ids) 
		print("\n\ntest----",self.env['teacher.teacher'].browse(docids))
		print("\n\nSalary",self.get_salary(docids))
		return{
			'doc_ids':docids,
			'docs': self.env['teacher.teacher'].browse(docids),
            'doc_model': 'teacher.teacher',
            'data': data,
            'salary': self.get_salary(docids)
		}
