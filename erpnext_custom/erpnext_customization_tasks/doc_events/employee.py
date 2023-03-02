# Copyright (c) 2023, Shaima'a Khashan and contributors
# For license information, please see license.txt
import frappe


def validate_create_task(doc, method):
    if doc.status == 'Left':
        task_doc = frappe.new_doc("Task")
        task_doc.set("subject", "End of Service For Employee :"+str(doc.employee_name))
        task_doc.set("employee_responsible", doc.employee_responsible)
        task_doc.insert()
