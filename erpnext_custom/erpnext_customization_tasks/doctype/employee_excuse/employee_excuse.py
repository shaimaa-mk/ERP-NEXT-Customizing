# Copyright (c) 2023, Shaima'a Khashan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import time_diff_in_hours


class EmployeeExcuse(Document):

	def validate(self):
		self.validate_max_hours()

	def validate_max_hours(self):
		if self.to_time and self.from_time:
			hours = float(time_diff_in_hours(self.to_time, self.from_time))
			if hours > 2:
				frappe.throw("Excuse Time Allowed Just 2 hours, No More.")
			self.hours = hours

	def on_submit(self):
		self.create_attendance()

	def create_attendance(self):
		attendance_doc = frappe.new_doc("Attendance")
		attendance_doc.set("employee", self.employee)
		attendance_doc.set("attendance_date", self.excuse_date)
		attendance_doc.set("status", "Present")
		attendance_doc.insert()

