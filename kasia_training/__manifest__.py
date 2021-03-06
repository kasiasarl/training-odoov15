# -*- coding: utf-8 -*-
{
    'name': "KASIA TRAINING",
    'summary': """
        Odoo Training v15
    """,
    'description': """
        Odoo Training v15
    """,
    'author': "KASIA",
    'website': "https://kasia.mg",
    'category': 'Sales',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
    ],

    # always loaded
    'data': [
        # data
        'data/ir_sequence_data.xml',
        # security
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        # views
        'views/student_management_views.xml',
        'views/course_management_views.xml',
        'views/res_partner_views.xml',
        'views/student_class_views.xml',
        'views/website_templates.xml',
        # report
        'report/student_report.xml',
        # wizards
        'wizard/course_wizard_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
