# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2016- Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

class mrp_production_product_line(models.Model):
    _inherit = 'mrp.production.product.line'

    line_unity_cost = fields.Float(string='Unity Cost', related='product_id.standard_price')
    line_material_cost = fields.Float(string='Material Cost', compute='_line_material_cal')
    lot_number = fields.Char(string="Lot number")
    
    @api.one
    def _line_material_cal(self):
        self.line_material_cost = self.product_id.standard_price * self.product_qty


class mrp_bom_line(models.Model):
    _inherit = 'mrp.bom.line'

    line_unity_cost = fields.Float(string='Unity Cost', related='product_id.standard_price')
    line_material_cost = fields.Float(string='Material Cost', compute='_line_material_cal')

    @api.one
    def _line_material_cal(self):
        self.line_material_cost = self.product_id.standard_price * self.product_qty

class mrp_production(models.Model):
    _inherit = 'mrp.production'
    
    lot_number = fields.Char(string="Lot number")
    

    