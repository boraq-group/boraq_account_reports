# -*- coding: utf-8 -*-
{
    'name': "Boraq Account Report",

    'summary': """
        This module will help to add analytic filter in report.
        
        """,

    'description': """
        This module will help to add analytic filter in report.
    """,

    'author': "Boraq-Group",
    'website': "",
    'category': 'Accounting',
    'version': '13.0.1.0',
    'depends': ['account_reports','account'],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_financial_report_data.xml',
        'views/assets.xml',
        ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
