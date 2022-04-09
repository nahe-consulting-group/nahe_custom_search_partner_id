# -*- coding: utf-8 -*-
# from odoo import http


# class Nahe-custom-search-partner-id(http.Controller):
#     @http.route('/nahe-custom-search-partner-id/nahe-custom-search-partner-id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe-custom-search-partner-id/nahe-custom-search-partner-id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe-custom-search-partner-id.listing', {
#             'root': '/nahe-custom-search-partner-id/nahe-custom-search-partner-id',
#             'objects': http.request.env['nahe-custom-search-partner-id.nahe-custom-search-partner-id'].search([]),
#         })

#     @http.route('/nahe-custom-search-partner-id/nahe-custom-search-partner-id/objects/<model("nahe-custom-search-partner-id.nahe-custom-search-partner-id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe-custom-search-partner-id.object', {
#             'object': obj
#         })
