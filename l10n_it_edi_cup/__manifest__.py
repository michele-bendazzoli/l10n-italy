# -*- coding: utf-8 -*-
{
    'name': "ITA - Fattura elettronica - Cup",

    'summary': "Gestione cup per Fatturazione elettronica anche per clienti privati",

    'description': """
Gestione cup per Fatturazione elettronica anche per clienti privati
    """,

    'author': "Applibra",
    'website': "https://github.com/OCA/l10n-italy",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Localizations/EDI',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_it_edi'],
    'auto_install': ['l10n_it_edi'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/l10n_it_edi_cup_view_inherited.xml',
        'data/l10n_it_edi_cup_invoice_it_template.xml'
    ],
    'license': 'LGPL-3',
}

