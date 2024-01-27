from odoo import api, models

class StudentReport(models.AbstractModel):
    _name = "report.college.report_student_pdf"

    def get_results(self, docids):
        print('\n\n  docids', docids)
        # list = []
        for doc in docids:
            results = self.env['result.result'].search([('student_id', '=', doc)])
            # list.append(results)
            return results
        return []

    @api.model
    def _get_report_values(self,docids,data=None):
        print("\n\n========docids",docids)
        studs = self.get_results(docids)
        print("\n\nstuds",studs,studs.ids)
        print("env----------------",self.env['result.result'].browse(docids))
        print("last===========",self.get_results(docids))
        return {
            'doc_ids': docids,
            'docs': self.env['result.result'].browse(docids),
            'doc_model': 'result.result',
            'data': data,
            'results': self.get_results(docids)
        }

