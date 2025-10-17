# Copyright 2023 Domatix - Carlos Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class SaleSubscriptionCloseReason(models.Model):
    _name = "sale.subscription.close.reason"
    _description = "Close reason model"
    _order = "sequence, name, id"

    name = fields.Char(required=True)
    sequence = fields.Integer()

    def copy(self, default=None):
        """Add '(copy)' suffix when duplicating a close reason."""
        default = dict(default or {})
        if "name" not in default and self.name:
            default["name"] = _("%s (copy)") % (self.name,)
        return super().copy(default)
