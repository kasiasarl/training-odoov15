# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CourseManagement(models.Model):
    _name = 'course.management'
    _description = 'Course Management'

    name = fields.Char(string='Name', required='')
    course_date = fields.Datetime(string='Date', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', domain="[('is_profesor','=', True)]")
