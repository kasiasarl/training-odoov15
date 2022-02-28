# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age',)
    sexe = fields.Selection([('m', 'M'), ('f', 'F')], string='Sexe', default='m')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    image = fields.Image(string='Image')
