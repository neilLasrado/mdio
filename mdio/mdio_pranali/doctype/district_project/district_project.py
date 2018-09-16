# -*- coding: utf-8 -*-
# Copyright (c) 2018, Rtr. Rtn. Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cstr, getdate, add_months, now

class DistrictProject(Document):
	def validate(self):
		self.set_status()

	def set_status(self):
		self.time_stamp = now()
		d = add_months(getdate(self.end_time), 1)
		deadline = cstr(getdate(d).strftime("%Y")) + "-" + cstr(getdate(d).strftime("%m")) + "-15"
		if getdate(self.time_stamp) > getdate(deadline):
			self.project_status = "Late"
		else:
			self.project_status = "On Time"
