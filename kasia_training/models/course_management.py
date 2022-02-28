# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CourseManagement(models.Model):
    _name = 'course.management'
    _description = 'Course Management'

    name = fields.Char()
