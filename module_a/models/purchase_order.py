# # Copyright (C) 2021-Today: GRAP (<http://www.grap.coop/>)
# # @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# # License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# from odoo import api, models


# class PurchaseOrder(models.Model):
#     _inherit = "purchase.order"

#     @api.allowed_groups("base.group_multi_company")
#     def function_A_decorator(self):
#         pass

#     @api.allowed_groups("base.group_multi_company")
#     def function_B_overloaded_no_redecorated(self):
#         pass

#     @api.allowed_groups("base.group_multi_company")
#     def function_C_overloaded_with_new_group(self):
#         pass

#     @api.allowed_groups("base.group_multi_company")
#     def function_D_overloaded_group_removed(self):
#         pass
