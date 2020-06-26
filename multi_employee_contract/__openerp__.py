# -*- coding: utf-8 -*-

{
    'name': 'Multiple Employee Contract',
    'version': '9.0.1.0.0',
    'author': 'Aktiv Software',
    'website': 'http://www.aktivsoftware.com',
    'summary': 'Create Multiple Contract at a same time.',
    'category': 'Generic Modules/Human Resources',
    'license': 'AGPL-3',
    'depends': ['hr_payroll'],
    'data': [
            'wizard/mutli_contract_view.xml',
    ],
    'description': """
        This module is used to create multiple contracts of an
        employee at a time.
    """,

    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
}
