{
    'name': 'College Management',
    'description': 'Manage patient',
    'author': 'ERP Harbor',
    'website': 'erpharbor.in',
    'version': '16.0.1.0.0',
    'depends': ['base', 'sale_management'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'data/ir_sequence.xml',
        'wizard/stud_popup_views.xml',
        'wizard/exam_report_views.xml',
        'wizard/student_report_popup_views.xml',
        'views/student_views.xml',
        'wizard/wiz_popup_views.xml',
        'wizard/teacher_salary_report_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml',
        'views/student_result_views.xml',
        'views/teacher_salary_views.xml',
        'views/res_partner_views.xml',
        'views/res_partner_teacher_views.xml',
        'wizard/cancel_popup_views.xml',
        'views/exam_views.xml',
        # 'views/crm_lead_views.xml',
        'views/erp_views.xml',
        # Reports
        'report/student_pdf_report.xml',
        'report/teacher_pdf_report.xml',
        'report/student_card_report.xml',
        'report/report_student_pdf.xml',
        'report/salaray_report_pdf.xml',
        # 'report/teacher_stud_report.xml',
        # Menu
        'views/menu.xml',

    ],
    'assets': {},
    'license': 'LGPL-3',
}