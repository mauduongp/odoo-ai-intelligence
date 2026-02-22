# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'AI Base',
    'version': '1.0',
    'summary': 'AI Base',
    'sequence': 10,
    'description': """
AI Base
====================
    """,
    'category': 'AI/AI',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'views/ai_provider_views.xml',
        'views/ai_menu_items.xml',
        'views/res_config_setting_views.xml',
    ],
    'installable': True,
    'application': False,
    'assets': {
    },
    'author': 'Mau DP',
    'license': 'LGPL-3',
}
