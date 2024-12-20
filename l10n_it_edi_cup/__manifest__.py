# -*- coding: utf-8 -*-
{
    'name': "l10n_it_edi_cup",

    'summary': "Gestione cup per Fatturazione elettronica anche per clienti privati",

    'description': """
Gestione cup per Fatturazione elettronica anche per clienti privati, basato su estensione di l10n_it_edi versione 18
    """,

    'author': "Applibra",
    'website': "https://github.com/OCA/l10n-italy",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization/Italy',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_it_edi'],
    'auto_install': ['l10n_it_edi'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/l10n_it_edi_cup_view_inherited.xml',
        'data/invoice_it_template.xml'
    ],
}

