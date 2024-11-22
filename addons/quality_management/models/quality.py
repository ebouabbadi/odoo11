from odoo import models, fields, api

class QualityCheck(models.Model):
    _name = 'quality.check'
    _description = 'Quality Check'

    name = fields.Char(string='Check Name', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    lot_id = fields.Many2one('stock.production.lot', string='Lot/Serial Number')
    status = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ], string='Status', default='pass', required=True)
    notes = fields.Text(string='Notes')
    check_date = fields.Date(string='Check Date', default=fields.Date.context_today)

    @api.onchange('status')
    def _onchange_status(self):
        """Set default note when status is 'fail'."""
        if self.status == 'fail' and not self.notes:
            self.notes = 'Follow up required.'
