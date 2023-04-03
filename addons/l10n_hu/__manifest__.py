# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hungary - Accounting',
    'website': 'https://www.odoo.com/documentation/master/applications/finance/fiscal_localizations.html',
    'version': '3.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
        Accounting chart and localization for Hungary
    """,
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'data/account_tax_report_data.xml',
        'data/res.bank.csv',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
