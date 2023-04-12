from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description ="Setting"

    module_hr_work_entry_contract = fields.Boolean(string='Work Entry Contract', default=True,
                                                  help="Integration Work Entry Contract")
    module_hr_work_entry_holidays = fields.Boolean(string='Work Entry Holiday', default=True,
                                                   help="Integration Work Entry Holiday")
