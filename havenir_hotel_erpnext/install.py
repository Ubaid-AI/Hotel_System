# install.py in havenir_hotel_erpnext/havenir_hotel_erpnext/

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def create_custom_fields():
    frappe.msgprint("Creating Custom Fields for Sales Invoice and Payment Entry")
    custom_fields = {
        "Sales Invoice": [
            {
                "fieldname": "check_in_id",
                "label": "Check In ID",
                "fieldtype": "Data",
                "insert_after": "customer_name",  # Ensure this field exists
                "reqd": 0,
                "description": "Reference ID for Check-In",
            },
            {
                "fieldname": "check_out_id",
                "label": "Check Out ID",
                "fieldtype": "Data",
                "insert_after": "check_in_id",
                "reqd": 0,
                "description": "Reference ID for Check-Out",
            },
        ],
        "Payment Entry": [
            {
                "fieldname": "check_in_id",
                "label": "Check In ID",
                "fieldtype": "Link",
                "options": "Hotel Check In",
                "insert_after": "party_name",  # Adjust based on actual field layout
                "reqd": 0,
                "description": "Reference ID for Check-In",
            },
            {
                "fieldname": "guest_name",
                "label": "Guest Name",
                "fieldtype": "Data",
                "insert_after": "check_in_id",
                "reqd": 0,
                "description": "Reference ID for Check-Out",
            },
            {
                "fieldname": "guest_id",
                "label": "Guest ID",
                "fieldtype": "Link",
                "options": "Hotel Guests",
                "insert_after": "guest_name",  # Adjust based on actual field layout
                "reqd": 0,
                "description": "",
            },
        ]
    }

    for doctype, fields in custom_fields.items():
        for field in fields:
            create_custom_field(doctype, field)

    frappe.db.commit()

def before_install():
    check_if_erpnext_installed()

def check_if_erpnext_installed():
    if "erpnext" not in frappe.get_installed_apps():
        frappe.throw("Please install the ERPNext app first before installing Hotel MS app.")
