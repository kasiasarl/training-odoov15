# -*- coding: utf-8 -*-
# from odoo import http


# class KasiaTraining(http.Controller):
#     @http.route('/kasia_training/kasia_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kasia_training/kasia_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kasia_training.listing', {
#             'root': '/kasia_training/kasia_training',
#             'objects': http.request.env['kasia_training.kasia_training'].search([]),
#         })

#     @http.route('/kasia_training/kasia_training/objects/<model("kasia_training.kasia_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kasia_training.object', {
#             'object': obj
#         })
