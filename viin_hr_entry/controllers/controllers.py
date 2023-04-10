# -*- coding: utf-8 -*-
# from odoo import http


# class ViinHrEntry(http.Controller):
#     @http.route('/viin_hr_entry/viin_hr_entry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viin_hr_entry/viin_hr_entry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viin_hr_entry.listing', {
#             'root': '/viin_hr_entry/viin_hr_entry',
#             'objects': http.request.env['viin_hr_entry.viin_hr_entry'].search([]),
#         })

#     @http.route('/viin_hr_entry/viin_hr_entry/objects/<model("viin_hr_entry.viin_hr_entry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viin_hr_entry.object', {
#             'object': obj
#         })
