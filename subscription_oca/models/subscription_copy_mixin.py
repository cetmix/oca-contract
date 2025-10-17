# Copyright (C) 2025 Cetmix OÜ
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models


class SubscriptionCopyMixin(models.AbstractModel):
    """Mixin for '(copy)' suffix behavior on record duplication."""

    _name = "subscription.copy.mixin"
    _description = "Mixin for subscription copy behavior"

    def copy(self, default=None):
        """Add '(copy)' suffix when duplicating a record."""
        default = dict(default or {})
        if "name" not in default and self.name:
            default["name"] = _("%s (copy)") % (self.name,)
        return super().copy(default)
