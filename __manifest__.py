# -*- coding: utf-8 -*-
{
    'name': "academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Rajesh Prajapati",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       'views/views.xml',
        # 'views.xml',
        'views/templates.xml',
       'views/partner.xml',
        # 'data.xml',
        'demo/demo.xml',
    ],
    # 'qweb':[
    # 'static/src/xml/test.xml',
    # ],
    # only loaded in demonstration mode
    # 'demo': [
    #     # 'demo/demo.xml',
    # ],
    'application' : True
}