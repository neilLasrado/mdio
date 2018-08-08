# -*- coding: utf-8 -*-
# Copyright (c) 2018, Rtr. Rtn. Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Registrations(Document):
	def on_submit(self):
		user = frappe.new_doc("User")
		user.update({
			"first_name": self.first_name,
			"last_name": self.last_name,
			"email": self.email,
			"send_welcome_email": 1
		})
		user.save()
		user.update({
			"roles": [
				{"role": "DRR"}
			]
		})
		user.save()
		permission = frappe.new_doc("User Permission")
		permission.user = user.name
		permission.allow = "District"
		permission.for_value = self.district
		permission.save()
