{
    'name': 'Hospital Management',
    'description': 'Manage patient',
    'author': 'ERP Harbor',
    'website': 'erpharbor.in',
    'version': '16.0.1.0.0',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_sales_views.xml',
        'views/hospital_patient_views.xml',
        'views/menu.xml',

    ],
    'assets': {},
    'license': 'LGPL-3',
}
