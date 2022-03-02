# -*- coding: utf-8 -*-
from odoo import http


class StudentManagement(http.Controller):
    @http.route('/student', auth='public', website=True)
    def list(self, **kw):
        StudentObject = http.request.env['student.management']
        st_list = StudentObject.search([])
        return http.request.render('kasia_training.student_list', {'student': st_list})

    @http.route('/student/<model("student.management"):student_data>', auth='public', website=True)
    def single(self, student_data, **kw):
        return http.request.render('kasia_training.student_page', {'stline': student_data})
