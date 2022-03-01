from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_profesor = fields.Boolean(default=False)
