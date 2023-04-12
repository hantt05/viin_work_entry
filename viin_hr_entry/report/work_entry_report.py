from odoo import models, fields, api, tools

class WorkEntryAnalylis(models.Model):
    _name = 'work.entry.report'
    _description = 'Work Entry Analysis'
    _auto = False
    
    employee_id = fields.Many2one('hr.employee', readonly=True)
    work_entry_type_id = fields.Many2one('hr.work.entry.type',string="Work entry type", readonly=True)
    state = fields.Char(readonly=True)
    date_start = fields.Date(string='Start Date', readonly=True)
    date_stop = fields.Date(string='End Date', readonly=True)
    
    def _table_query(self):
        return '%s %s' % (self._select(), self._frorm())

    @api.model
    def _select(self):
        return """
        SELECT we.id AS id, 
            emp.id AS employee_id, 
            type.id AS work_entry_type_id, 
            we.name AS name, 
            we.state AS state,  
            we.date_start AS date_start, 
            we.date_stop AS date_stop
        """
    @api.model
    def _from(self):
        return """
        FROM hr_work_entry we
            JOIN hr_employee emp ON we.employee_id=emp.id
            JOIN hr_work_entry_type type ON we.work_entry_type_id=type.id
        """    