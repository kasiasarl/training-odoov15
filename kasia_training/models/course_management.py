# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CourseManagement(models.Model):
    _name = 'course.management'
    _description = 'Course Management'

    name = fields.Char(string='Name', required='')
    course_date = fields.Datetime(string='Date', required=True)
    course_end = fields.Datetime(string='End', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', domain="[('is_profesor','=', True)]", required=True)
    state = fields.Selection([('new', 'New'), ('validated', 'Validated'), ('end', 'End'), ('canceled', 'Canceled')],
                             default='new')

    def run_validate(self):
        self.write({'state': 'validated'})
