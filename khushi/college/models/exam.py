from odoo import api,fields,models
import datetime
from odoo.exceptions import ValidationError,UserError

class Exam(models.Model):
    _name = 'exam.exam'
    _description = "Student Exam"
    # _rec_name = "name"

    name = fields.Char("Student Name",required=1)
    date = fields.Date("Result Date")
    teacher_id = fields.Many2one("teacher.teacher",string="Teacher Name")
    subject = fields.Char(string="Subject")

        # "student_subject_relation", 'student_id', 'subject_id', string="Subjects")
    marks = fields.Float("Marks",compute="all_marks")
    # compute="all_marks"
    exam_session = fields.Selection([
        ('internal','Internal'),
        ('external','External')],string="Exam Session")
    exam_line_ids = fields.One2many("exam.line","exam_id",string="Exam Line")
    state = fields.Selection([('draft','Draft'),('start','Start'),('complete','Complete'),('cancel','Cancel')]
        , string="Status",default="draft")
    cut_mark = fields.Float("cut Marks")
    line_mark = fields.Float("Marks")
    is_student = fields.Boolean("Is Student")
    sequence = fields.Char(string="sequence" ,readonly=True)
    # Status = fields.Char("Status")
    exam_name = fields.Char("Exam Name")
    exam_date = fields.Date("Exam Date")
    exam_cancel = fields.Text("Reason of Cancelltion")
    date_exam = fields.Date("Exam Cancel Date")
    candidate_name = fields.Char("Candidate Name")

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('my.sequence.code')
        return super(Exam, self).create(vals)

    @api.constrains('exam_date')
    def _check_exam_date(self):
        today_date = datetime.date.today()
        for record in self:
            if record.exam_date != today_date:
                raise ValidationError('Exam date cannot be in the past/Future.')


    @api.depends('exam_line_ids','exam_line_ids.total')
    def all_marks(self):
        for exam in self:
            marks = 0
            for line in exam.exam_line_ids:
                marks += line.total
            exam.marks = marks

    
    # def name_get(self):
    #     res=[]
    #     for exam in self:
    #         res.append((exam.id,"%s" % (exam.marks)))
    #     return res

    @api.onchange('is_student')
    def onchange_student(self):
        if self.is_student == True:
            self.exam_session = "internal"


    def action_complete(self):
        # self.Status = "Pass"
        self.state = 'complete'
        print("clicked on button")

    def action_draft(self):
        self.state = "draft"
        print("click on button")


    def action_start(self):
        self.state = 'start'
        print("clicked on button")

    # def action_cancel(self):
    #     self.state='cancel'
    #     print("Click on button")

    def action_cancel(self):
        return {
            'name': 'Cancel Exam',
            'view_mode': 'form',
            'res_model': 'cancel.popup',
            'view_id': self.env.ref('college.cancel_popup_form_view').id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    # ----------------------------------------------------------------------------
    def unlink(self):
        for student in self:
            if student.is_student == True:
                raise UserError("Record can't be deleted:")
        return super(student, self).unlink(student)





    




class ExamLine(models.Model):
    _name = "exam.line"
    _description = "Exam Lines"
    # _order = "name"

    subject = fields.Char("Subject")
    exam_name = fields.Char("Exam Name")
    cut_mark = fields.Float("cut Marks")
    line_mark = fields.Float("Marks")
    total = fields.Float("Total Marks",compute="Total_marks",store=True)
    exam_id = fields.Many2one("exam.exam",string="Exam")


    @api.depends('total','cut_mark')
    def Total_marks(self):
        for ab in self:
            ab.total=ab.line_mark-ab.cut_mark

