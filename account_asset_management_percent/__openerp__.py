# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2015-2016 SimplERP srl (<http://www.simplerp.it>).
#    Copyright (C) 2017 Sergio Corato
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Italian customization for asset',
    'version': '8.0.2.1.0',
    'category': 'other',
    'author': 'Sergio Corato',
    'website': 'http://www.efatto.it',
    'license': 'AGPL-3',
    'description': 'Italian customization for asset',
    'depends': [
        'account',
        'account_asset_management',
        'l10n_it_account',
    ],
    'data': [
        'data/reports.xml',
        'report/print_asset_report.xml',
        'views/account_asset_view.xml',
        'views/report_asset.xml',
        'views/wizard_asset_compute.xml',
        'views/wizard_asset_confirm.xml',
    ],
    'installable': True
}