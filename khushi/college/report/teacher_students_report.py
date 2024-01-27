from odoo import api,models


class TeacherStudReport(models.AbstractModel):
    _name = "report.college.report_student_pdf"

    def get_students(self, docids):
        print('\n\n MY docids', docids)
        for doc in docids:
            students = self.env['student.student'].search([('teacher_id', '=', doc)])
            return students
        return []

    @api.model
    def _get_report_values(self, docids, data=None):
        print('\n\n ----------docids', docids)
        # my parsel report
        studs = self.get_students(docids)
        print('\n\n studs', studs, studs.ids)
        print("test----------------",self.env['teacher.teacher'].browse(docids))
        print("data----",data)
        print("last-----------",self.get_students(docids))
        print("doc_model",'teacher.teacher')
        return {
            'doc_ids': docids,
            'docs': self.env['teacher.teacher'].browse(docids),
            'doc_model': 'teacher.teacher',
            'data': data,
            'students': self.get_students(docids)
        }
