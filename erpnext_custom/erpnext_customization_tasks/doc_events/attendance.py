# Copyright (c) 2023, Shaima'a Khashan and contributors
# For license information, please see license.txt
from frappe.utils.data import time_diff_in_hours


def get_status(doc, method):
    if not doc.check_in or not doc.check_out:
        doc.status = "Absent"


def get_hours(doc, method):
    doc.set("hours", float(time_diff_in_hours(doc.check_out, doc.check_in)))
