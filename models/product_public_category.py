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

from openerp import models, fields, api
from openerp.http import request

class product_public_category(models.Model):
    _inherit = "product.public.category"

    @api.one
    def filter_tree(self):
        filter_ids = self.env['product.product.filter.category'].search([('public_categ_ids','=',self.id)])

        category_tree =[]
        filter_list = request.httprequest.args.getlist('filter')
        filter_values = {v.split(":")[0]:v.split(":")[1] for v in filter_list if v.split(":")[1]}
        for filter_cat in filter_ids:
            items =[]
            if filter_cat.filter_type != 'product_price'  :
                for product_filter_id in filter_cat.filter_filter_ids :

                    selected = True if str(filter_cat.id) in filter_values and filter_values[str(filter_cat.id)] == str(product_filter_id.id)  else False
                    
                    args=filter_values.copy()
                    if selected:
                        del args[str(filter_cat.id)]
                    else :
                        args[str(filter_cat.id)]=str(product_filter_id.id)

                    arg_string=""
                    for x in args.keys():
                        arg_string+='filter=' + x +":" + args[x] +"&" 

                    items.append({'name':product_filter_id.name,'id':product_filter_id.id,'selected':selected,'args':arg_string})

            category_tree.append({'name':filter_cat.name,'id':filter_cat.id,'childs':items})

        return category_tree
 