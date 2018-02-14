# -*- coding: utf-8 -*-
{
    'name': "receipt_checks_date",

    'summary': """
        Add field in Accounting to register the date of checks receipt.""",

    'description': """
        Add field in Accounting to register the date of checks receipt.
        You can visualise it in POS lines order.
    """,

    'author': "Valentin",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}