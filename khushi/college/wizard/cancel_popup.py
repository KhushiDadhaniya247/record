from odoo import fields, models


class CancelPop(models.TransientModel):
    _name = "cancel.popup"
    _description = "Cancel Popup "

    reason = fields.Text(string="Reason Of Cancelltion")
    date = fields.Date(string="Date")
    c_name = fields.Char("Candidate name")

    # def action_done_popup(self):
    #     print("click on button")

    def action_cancel_exam(self):
        print("clickk.................")
        # active_exam = self.env['exam.exam'].browse(self._context.get('active_id'))
        # active_exam.write({'state': 'cancel', 'cancel_reason': self.cancel})
        # return {'type': 'ir.actions.act_window_close'}
        # print("heloooooo",active_exam)

    def action_cancel_exam(self):
        exam_id = self.env.context.get('active_id')
        exam = self.env['exam.exam'].browse(exam_id)
        exam.write({'state':'cancel',
                    'date_exam': self.date,
                    'exam_cancel':self.reason,
                    'candidate_name':self.c_name
        })


   

