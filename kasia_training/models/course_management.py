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
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    category_ids = fields.Many2many('res.partner.category', string='Category')

    def run_validate(self):
        self.write({'state': 'validated'})

    def run_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'course.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'views': [[False, 'form']],
            'target': 'new',
        }

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        return {
            'value': {
                'phone': self.partner_id.phone,
                'email': self.partner_id.email,
            }
        }
