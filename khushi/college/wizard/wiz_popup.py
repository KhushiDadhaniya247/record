from odoo import fields, models,api


class WizPopup(models.TransientModel):
    _name = "wiz.popup"
    _description = "Popup Wizard"

    total_salary = fields.Float(string="salary")
    date = fields.Date(string="Date")
    tax = fields.Float(string="Tax Amount")
    net_salary = fields.Float(string="Net Salary")
    teacher_id = fields.Many2one('teacher.teacher',string="Teacher Name")
    teacher_ids = fields.Many2many('teacher.teacher', string='Selected Teachers')
    # ,default=lambda self: self._default_teacher_id()


    # def update_info_fun(self):
    #     active_id = self._context.get('active_id')
    #     upd_var=self.env['wiz.popup'].browse(active_id)
    #     print("\n\nupdate var",upd_var)
    #     vals={'teacher_id':self.name.id}
    #     upd_var.write(vals)

    @api.model
    def default_get(self,fields):
        res = super(WizPopup,self).default_get(fields)
        active_id = self._context.get('active_id')
        print("\n\n\nself._context.get",self._context.get)
        brw_id = self.env['teacher.teacher'].browse(active_id)
        # print("\n\nbrw_id------------",brw_id)

        if active_id:
            res['teacher_id'] = brw_id.id


        return res


    def action_receive_salary(self):
        print("\n\nButton is Clicked")
        print("\n\nButton is Clicked", self.env.context)
        ctx = self.env.context
        print('\n\n ===========ctx', ctx)
        if ctx.get('active_model') == 'teacher.teacher' and ctx.get('active_ids'):
            teacher_ids = ctx.get('active_ids')

            for teacher_id in teacher_ids:
                teacher_salary = self.env['salary.salary'].create({
                    'teacher_id': teacher_id,
                    'total_salary': self.total_salary,
                    'tax': self.tax,
                    'date': self.date,
                    # 'net_salary': self.net_salary
                })
                print("\n\nteacher_salary", teacher_salary)

    
    # single record mate wizard(many2one)
    
    # def action_receive_salary(self):
    #     print("\n\nButton is Clicked")
    #     print("\n\nButton is Clicked", self.env.context)
    #     ctx = self.env.context
    #     print('\n\n ===========ctx', ctx)
    #     print('\n\n ------------TEACHER', self.teacher_id, self.teacher_id.id)
    #     teacher_salary = self.env['salary.salary'].create({
    #         'teacher_id': self.teacher_id.id,
    #         'total_salary': self.total_salary,
    #         'tax': self.tax,
    #         'date': self.date,
    #     })
    #     print("\n\nteacher_salary", teacher_salary)


    # multiple record mate wizard(one2many mate)

    def action_receive_salary(self):
        print("\n\nButton is Clicked")
        print("\n\nButton is Clicked", self.env.context)
        ctx = self.env.context
        print('\n\n ===========ctx', ctx)
        print('\n\n ------------TEACHER',self.teacher_ids,self.teacher_ids.ids)

        for teacher_id in self.teacher_ids: 
            teacher_salary = self.env['salary.salary'].create({
                'teacher_id': teacher_id.id,
                'total_salary': self.total_salary,
                'tax': self.tax,
                'date': self.date,
            })
            print("\n\nteacher_salary", teacher_salary)

                        
 

























    # without browse

    # def action_receive_salary(self):
    #     print("\n\nButton is Clicked")
    #     print("\n\nButton is Clicked",self.env.context)
    #     ctx = self.env.context
    #     if ctx.get('active_model') == 'teacher.teacher' and ctx.get('active_ids'):
    #         teachers=self.env['teacher.teacher'].browse(ctx.get('active_ids'))

    #         for teacher in teachers:
    #             teacher_salary = self.env['salary.salary'].create({
    #                 'teacher_id': teacher.id,
    #                 'total_salary': self.total_salary,
    #                 'tax': self.tax,
    #                 'date': self.date,
    #                 'net_salary': self.net_salary 
    #             })
    #             print("\n\nteacher_salary",teacher_salary)
    




 
 