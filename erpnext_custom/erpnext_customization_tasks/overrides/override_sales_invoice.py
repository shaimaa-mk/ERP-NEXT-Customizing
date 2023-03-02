# Copyright (c) 2023, Shaima'a Khashan and contributors
# For license information, please see license.txt

from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from frappe.utils import formatdate
from frappe import _
import frappe


class CustomSalesInvoice(SalesInvoice):

    def add_remarks(self):
        if not self.remarks:
            if self.po_no and self.po_date:
                self.remarks = _("Against Customer Order {0} dated {1}").format(
                    self.po_no, formatdate(self.po_date)
                )
            else:
                items = ""
                if not self.remarks:
                    for item in self.get("items"):
                        items = str(items) + str(item.item_name) + "\n"
                    self.remarks = str(items)

    def validate_pos_paid_amount(self):
        if len(self.payments) == 0 and self.is_pos:
            frappe.throw(_("At least one mode of payment is required for POS invoice."))

        if len(self.payments) > 0 and self.is_pos:
            for payment in self.payments:
                if payment.amount == 0:
                    frappe.throw(_("Payment Amount Is Required For Each Payment Method!."))
