# Copyright 2023 Domatix - Carlos Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import _, fields, models


class SaleSubscriptionTag(models.Model):
    _name = "sale.subscription.tag"
    _description = "Tags for sale subscription"

    name = fields.Char("Tag name", required=True)

    def copy(self, default=None):
        """Add '(copy)' suffix when duplicating a tag."""
        # English-only comment: Keep consistency with other models.
        default = dict(default or {})
        if "name" not in default and self.name:
            default["name"] = _("%s (copy)") % (self.name,)
        return super().copy(default)
