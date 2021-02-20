
print("===================")
print("tests.py")
print("===================")

from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):

    # Overload Section
    def setUp(self):
        print("TRANSACTION CASE")

        super().setUp()

        self.PurchaseOrder = self.env["purchase.order"]

    def test_function_a_decorator(self):
        # function_A can be executed only by base.group_multi_company

        self.env.user.groups_id -= self.env.ref("base.group_multi_company")
        with self.assertRaises(AccessError):
            self.PurchaseOrder.function_A_decorator()

        self.env.user.groups_id += self.env.ref("base.group_multi_company")
        self.PurchaseOrder.function_A_decorator()

    def test_function_b_overloaded_no_redecorated(self):
        # function_B can be executed only by base.group_multi_company

        self.env.user.groups_id -= self.env.ref("base.group_multi_company")
        with self.assertRaises(AccessError):
            self.PurchaseOrder.function_B_overloaded_no_redecorated()

        self.env.user.groups_id += self.env.ref("base.group_multi_company")
        self.PurchaseOrder.function_B_overloaded_no_redecorated()

    def test_function_c_overloaded_with_new_group(self):
        # function_C can finally be executed only by base.group_multi_currency

        self.env.user.groups_id -= self.env.ref("base.group_multi_company")
        self.env.user.groups_id -= self.env.ref("base.group_multi_currency")
        with self.assertRaises(AccessError):
            self.PurchaseOrder.function_C_overloaded_with_new_group()

        self.env.user.groups_id += self.env.ref("base.group_multi_company")
        with self.assertRaises(AccessError):
            self.PurchaseOrder.function_C_overloaded_with_new_group()

        self.env.user.groups_id -= self.env.ref("base.group_multi_company")
        self.env.user.groups_id += self.env.ref("base.group_multi_currency")
        self.PurchaseOrder.function_C_overloaded_with_new_group()

    def test_function_d_overloaded_group_removed(self):
        # function_D can finally be executed all people

        self.env.user.groups_id -= self.env.ref("base.group_multi_company")
        self.env.user.groups_id -= self.env.ref("base.group_multi_currency")
        self.PurchaseOrder.function_D_overloaded_group_removed()
