# Copyright 2023 Domatix - Carlos Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleSubscriptionCloseReason(models.Model):
    _name = "sale.subscription.close.reason"
    _inherit = ["subscription.copy.mixin"]
    _description = "Close reason model"
    _order = "sequence, name, id"

    name = fields.Char(required=True)
    sequence = fields.Integer()
