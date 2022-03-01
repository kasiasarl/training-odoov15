from odoo import api, fields, models


class StudentClass(models.Model):
    _name = 'student.class'
    _rec_name = 'st_class'
    _description = 'New Description'

    st_class = fields.Char(string='Class', required=True)
    student_ids = fields.One2many('student.management','class_id')
    student_count = fields.Integer()
