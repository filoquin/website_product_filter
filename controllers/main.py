# -*- coding: utf-8 -*-
import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp.addons.web.controllers.main import login_redirect

from openerp.addons.website_sale.controllers.main import website_sale

import logging

_logger = logging.getLogger(__name__)

class website_sale(website_sale):


    def _filter_category_tree(self, category):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        filter_ids = filter_obj.search(cr, uid,[('public_categ_ids','=',int(category))] , context=context)
        category_tree =[]
        filter_list = request.httprequest.args.getlist('filter')
        filter_values = {v.split(":")[0]:v.split(":")[1] for v in filter_list if v.split(":")[1]}

        for filter_cat in filter_ids.browse():
            items =[]
            if filter_cat.filter_type != 'product_price'  :
                for product_filter_id in filter_cat.product_filter_ids :
                    items.append({'name':product_filter_id.name,'id':product_filter_id.id,'selected':False})

            category_tree.append({'name':filter_cat.name,'id':filter_cat.id,'childs':items})

        return category_tree

    def _get_search_domain(self, search, category, attrib_values):

        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry

        domain = super(website_sale,self)._get_search_domain( search, category, attrib_values)

        if category:
            filter_list = request.httprequest.args.getlist('filter')

            filter_values = {v.split(":")[0]:v.split(":")[1] for v in filter_list if v.split(":")[1]}

            filter_obj = pool.get('product.product.filter.category')
            filter_ids = filter_obj.search(cr, uid,[('public_categ_ids','=',int(category))] , context=context)

            for filter_str_id in filter_values.keys():
                filter_id = int(filter_str_id)
                if filter_id in filter_ids:
                    filter_item=filter_obj.browse(cr, uid,filter_id, context=context)
                    if filter_item and filter_item.filter_type=='filter_name':
                        
                        filter_filter_ids=[x.id for x in filter_item.filter_filter_ids]
                        if int(filter_values[filter_str_id]) in filter_filter_ids: 
                            domain +=[('product_filter_ids','=',int(filter_values[filter_str_id]))]
                    if filter_item and filter_item.filter_type=='filter_domain':
                        filter_filter_domains={x.id : x.domain for x in filter_item.filter_filter_ids}
                        if int(filter_values[filter_str_id]) in filter_filter_domains.keys: 
                            domain +=filter_filter_domains[filter_item]

                    if filter_item and filter_item.filter_type=='product_price':
                        pass
        _logger.info("domain  %r  " %domain)

        return domain




