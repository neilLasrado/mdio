# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"District": {
			"color": "#9b59b6",
			"icon": "icon-globe",
			"icon": "octicon octicon-globe",
			"link": "List/District",
			"doctype": "District",
			"type": "list"
		},
		
		"Project": {
			"color": "#c23c59",
			"icon": "octicon octicon-rocket",
			"label": _("Project"),
			"link": "List/Project",
			"doctype": "Project",
			"type": "list"
		}
	}
