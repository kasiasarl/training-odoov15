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
    'category':'Sales',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
    ],

    # always loaded
    'data': [
        # data
        # security
        'security/ir.model.access.csv',
        # views
        'views/student_management_views.xml',
        'views/course_management_views.xml',
        'views/templates.xml',
        # wizads
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
