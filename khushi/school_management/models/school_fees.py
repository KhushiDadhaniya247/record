from odoo import api,fields,models, _

class school_fees(models.Model):
	_name ="school.fees"
	_description ="School Fees"
	_order ="name"
	_rec_name = 'name'


	name = fields.Char("Student Name",default= lambda self: _('New'), readonly=1, required=1)
	student_id = fields.Many2one("student.student",string='Student')
	fees_date = fields.Date(string="Fees Date")
	total_fees = fields.Float(string="Total Fees", compute='_compute_all_total')
	# fees_id = fields.One2many("school.fees","school_fees_line_id",string="fees")
	fees_line_ids = fields.One2many("school.fees.line","fees_id",string="school fees line")
	currency_id = fields.Many2one("res.currency",string='Currency')
	tax_amount = fields.Float(string="Tax Amount", compute='_compute_all_total')
	total = fields.Float(string="Total", compute='_compute_all_total')
	state = fields.Selection([('new','New'),('paid','Paid'),('cancle','Cancle')],string="Status")

	@api.model_create_multi
	def create(self,vals_list):
	# 	fees = super(school_fees, self).create(vals_list)
	# 	fees.write({'name': 'FS00' + str(fees.id)})
	# 	return fees

		for vals in vals_list:
			if vals.get('name',_('New')) == ('New'):
				vals['name'] = self.env['ir.sequence'].next_by_code('school.fees') or _('New')
				return super(school_fees,self).create(vals_list)




	@api.depends('fees_line_ids', 'fees_line_ids.price', 'fees_line_ids.sub_total')
	def _compute_all_total(self):
		for fees in self:
			total_fees = total_tax_amt = total = 0
			for line in fees.fees_line_ids:
				total_fees += line.price
				total_tax_amt += line.sub_total - line.price
				total += line.sub_total
			fees.total_fees = total_fees
			fees.tax_amount = total_tax_amt
			fees.total = total

    # for prectice :-

	# def _compute_all_total(self):
	# 	for fees in self:
	# 		total_fees = total_tax_amt = total = 0
	# 		for line in fees.fees_line_ids:
	# 			total_fees+=line.price
	# 			total_tax_amt+=line.sub_total-line.price
	# 			total+=line.sub_total
	# 		fees.total_fees = total_fees
	# 		fees.tax_amount = total_tax_amt
	# 		fees.total = total




class school_fees_line(models.Model):
	_name ="school.fees.line"
	_description = "School Fees Line"
	_order = "name"

	currency_id = fields.Many2one(related='fees_id.currency_id',string='Currency')
	name = fields.Char("Student Name")
	price = fields.Float(string="Price")
	tax = fields.Float(string="Tax")
	sub_total = fields.Float(string="Sub Total", compute='_compute_total',store=True)
	fees_id = fields.Many2one('school.fees',string="Fees")


	@api.depends('price', 'tax')
	def _compute_total(self):
		for fl in self:
			fl.sub_total = fl.price + (fl.price * fl.tax) / 100


 