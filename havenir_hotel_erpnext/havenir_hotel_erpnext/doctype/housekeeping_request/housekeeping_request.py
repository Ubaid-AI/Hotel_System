# Copyright (c) 2024, Havenir and contributors
# For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document

# class HousekeepingRequest(Document):
# 	pass

import frappe
from frappe.model.document import Document

class HousekeepingRequest(Document):
    def before_submit(self):
        # Ensure housekeeping request is linked to a valid room
        if not self.room:
            frappe.throw("Room must be specified before submitting the housekeeping request.")
    
    def on_submit(self):
        # Update housekeeping status in the linked room upon submission
        room = frappe.get_doc("Rooms", self.room)
        if self.housekeeping_status in ["Pending", "In Progress"]:
            room.housekeeping_status = "Dirty"
        elif self.housekeeping_status == "Completed":
            room.housekeeping_status = "Cleaned"
        room.save()

    def on_update_after_submit(self):
        # Reflect housekeeping status changes post submission
        room = frappe.get_doc("Rooms", self.room)
        if self.housekeeping_status == "Completed":
            room.housekeeping_status = "Cleaned"
        elif self.housekeeping_status in ["Pending", "In Progress"]:
            room.housekeeping_status = "Dirty"
        room.save()

    def on_cancel(self):
        # Revert housekeeping status if the document is cancelled
        room = frappe.get_doc("Rooms", self.room)
        room.housekeeping_status = "Dirty"  # Set to a default or last known value
        room.save()
