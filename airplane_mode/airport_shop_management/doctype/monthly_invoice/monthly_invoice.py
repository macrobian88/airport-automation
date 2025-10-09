# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MonthlyInvoice(Document):
	"""
	Monthly Invoice doctype for Airport Shop Management
	"""
	pass


def get_permission_query_conditions(user):
	"""
	Get permission query conditions for Monthly Invoice
	
	Args:
		user (str): User for whom to get permissions
		
	Returns:
		str: SQL conditions or None
	"""
	if not user:
		user = frappe.session.user
		
	# Allow all users to access all monthly invoices for now
	# You can customize this based on your business logic
	return None


def has_permission(doc, user):
	"""
	Check if user has permission for specific Monthly Invoice document
	
	Args:
		doc: Monthly Invoice document
		user (str): User to check permissions for
		
	Returns:
		bool: True if user has permission, False otherwise
	"""
	if not user:
		user = frappe.session.user
		
	# Allow all users to access all monthly invoices for now
	# You can customize this based on your business logic
	return True
