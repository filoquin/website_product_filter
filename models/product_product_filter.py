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

from datetime import datetime , timedelta ,  date
from dateutil import parser

from openerp import models, fields, api
from openerp import tools

from openerp.tools.translate import _



class product_product_filter_category(models.Model):
    _name = "product.product.filter.category"
    _description = "Product filter category"

    name = fields.Char('Name' , required=True)
    prefix = fields.Char('Prefix')
    suffix = fields.Char('Suffix')
    amount_from = fields.Float('From')
    amount_to = fields.Float('to')
    amount_step = fields.Float('step')

    public_categ_ids = fields.Many2many(
                            comodel_name='product.public.category',
                            relation='filter_public_categ',
                            column1='filter_id',
                            column2='categ_id',string='Category')
    filter_type = fields.Selection([('filter_name','by filter name'),('filter_domain','by filter domain'),('product_price','by product price')],string="Type",default='filter_name')
    filter_filter_ids = fields.One2many('product.product.filter.filter','filter_category_id')
    sequence = fields.Integer('sequence', help="Sequence for the handle.",default=10)


    @api.one
    def set_assign_domanin(self):
        for filters in self.filter_filter_ids:
            if filters.domain and  self.filter_type=="filter_name":
                product_ids = self.env['product.template'].search([('product_filter_ids','!=',self.id)] + eval(filters.domain))
                for product in product_ids:
                    product.write({'product_filter_ids':[(4,self.id)]})
                


class product_product_filter_filter(models.Model):
    _name = "product.product.filter.filter"
    _description = "Product filter filter name"
    _order = 'sequence'

    name = fields.Char('Name', required=True)
    filter_category_id = fields.Many2one('product.product.filter.category',string='Category')
    icon = fields.Many2one('ir.attachment',string='Icon')
    domain = fields.Text('Domain' )
    sequence = fields.Integer('sequence', help="Sequence for the handle.",default=10)


