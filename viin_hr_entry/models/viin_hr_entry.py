from odoo import models, fields

class ViinWorkEntry(models.Model):
    _inherit = ['hr.work.entry']
    _description = 'Viin Work Entry'


def action_cancel_work_entry(self):
    for r in self:
        if r.state == 'conflict':
            r.write({'state':'Cancelled'})
            