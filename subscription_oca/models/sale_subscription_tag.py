# Copyright 2023 Domatix - Carlos Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class SaleSubscriptionTag(models.Model):
    _name = "sale.subscription.tag"
    _inherit = ["subscription.copy.mixin"]
    _description = "Tags for sale subscription"

    name = fields.Char("Tag name", required=True)
