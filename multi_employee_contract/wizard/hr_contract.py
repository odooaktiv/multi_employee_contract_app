# -*- coding: utf-8 -*-

from openerp import models, api, _
from openerp import exceptions


class HrContract(models.Model):
    _inherit = 'hr.contract'

    @api.multi
    @api.constrains('employee_id')
    def _check_contract_for_same_employee(self):
        if self.employee_id:
            contract_id = self.env['hr.contract'].search([('id', '!=', self.id), ('employee_id', '=', self.employee_id.id), ('state', 'not in', ['close'])])
            if contract_id:
                raise exceptions.ValidationError(_('Contract can be only created if in expired state.'))
