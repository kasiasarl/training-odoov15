from odoo import api, fields, models


class StudentClass(models.Model):
    _name = 'student.class'
    _rec_name = 'st_class'
    _description = 'New Description'

    st_class = fields.Char(string='Class', required=True)
    student_ids = fields.One2many('student.management', 'class_id')
    student_count = fields.Integer(compute='_compute_student_count')
    student_age = fields.Integer(compute='_compute_student_count', store=True)

    @api.depends('student_ids')
    def _compute_student_count(self):
        for item in self:
            item.write({'student_count': len(item.student_ids), 'student_age': sum(item.student_ids.mapped('age'))})
