{
    'name': 'Multiple Employee Contract',
    'version': '1.0',
    'author': 'Aktiv Software',
    'website': 'http://www.aktivsoftware.com',
    'summary': 'Create Multiple Contract at a same time.',
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'depends': ['hr_payroll', 'resource'],
    'data': [
            'wizard/mutli_contract_view.xml',
    ],
    'description': """
        This module helps to create multiple employee's contracts from a wizard only if the previous contract is in expired state. 
    """,
    'auto_install': False,
    'installable': True,
    'application': True,
}

