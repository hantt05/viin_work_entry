# -*- coding: utf-8 -*-
{
    'name': "Viin Work Entries",

    'summary': """
        Manage work entries of employee""",

    'description': """
        This module manage work entries of employee in your company
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Work Entry',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_work_entry','hr_work_entry_contract'],

    # always loaded
    'data': [
        'security/viin_hr_entry_security.xml',
        'security/ir.model.access.csv',
        'views/root_menu.xml',
        'views/viin_hr_entry_views.xml',
        'report/viin_hr_entry_report.xml',
        'views/res_config_settings_work_entry_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'images': ['static/description/main_screenshot.png'],
    'license':'LGPL-3'
}
