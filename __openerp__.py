# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'website product filter',
    'version': '0.1',
    'category': 'website',
    'description': """
website Product filter
======================
Product website filter
    """,
    'author': 'Filoquin',
    'website': 'http://www.hormigag.com.ar',
    'depends': ['base','product','website','website_sale'],
    'installable': True,
    'data': ['product_product_filter.xml','layout.xml'],
    'images':[],    
    'auto_install': False,
}
