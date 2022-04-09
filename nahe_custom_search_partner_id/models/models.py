# -*- coding: utf-8 -*-

from odoo import models, fields, api


class naheCustomSearchID(models.Model):
    _inherit = 'sale.order'

    id_contacto = fields.Integer(string='ID contacto', related='partner_id.id', tracking=True)
    sale_order_count_contacto = fields.Integer(string='Ventas del contacto', related='partner_id.sale_order_count')



