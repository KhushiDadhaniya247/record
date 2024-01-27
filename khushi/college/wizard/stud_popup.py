from odoo import fields, models


class StudPopup(models.TransientModel):
    _name = "stud.popup"
    _description = "Stud Popup "

    subject_id = fields.Many2one("subject.subject",string="Subject")
    marks = fields.Integer("Marks")

    def action_submit_stud(self):
        print("\n\nButton Is Clicked",self)
        print("\nButton Is Clicked",self.env.context)
        ctx = self.env.context
        if ctx.get('active_model') == 'student.student' and ctx.get('active_id'):
            print("\nButton Is Clicked", ctx.get('active_model'), ctx.get('active_id'))
            print('\n\n Field values', self.subject_id.id, self.marks)
            result_dict = {'student_id': ctx.get('active_id'), 'subject_id': self.subject_id.id, 'marks': self.marks}
            print('\n\n result_dict',result_dict)
            result = self.env['result.result'].create(result_dict)
            print('\n\n result', result)
                                                           
