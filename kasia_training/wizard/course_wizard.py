from odoo import api, fields, models


class CourseWizard(models.TransientModel):
    _name = 'course.wizard'
    _rec_name = 'name'
    _description = 'Course Wizard'

    name = fields.Char()
    new_date = fields.Datetime(string='Date')

    def run_validate(self):
        active_id = self.env.context.get('active_id')
        CourseManagement = self.env['course.management'].browse(active_id)
        CourseManagement.write({
            'name': self.name,
            'course_date': self.new_date
        })
