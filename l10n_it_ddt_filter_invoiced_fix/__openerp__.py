# -*- coding: utf-8 -*-
# Copyright 2017 Sergio Corato
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'DDT fix invoiced filter',
    'version': '8.0.1.0.0',
    'category': 'other',
    'author': 'Sergio Corato',
    'website': 'https://efatto.it',
    'license': 'AGPL-3',
    'description': '''Fix invoiced filter.''',
    'depends': [
        'l10n_it_ddt',
    ],
    'data': [
        'views/stock.xml',
    ],
    'installable': False
}
