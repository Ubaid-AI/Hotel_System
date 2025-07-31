# Copyright (c) 2024, Havenir and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class MaintenanceRequest(Document):
# 	pass

import frappe
from frappe.model.document import Document

class MaintenanceRequest(Document):
    def before_save(self):
        # Validate room status before saving the maintenance request
        room = frappe.get_doc("Rooms", self.room)
        if room.room_status != "Available":
            frappe.throw(f"Room {self.room} is currently not available for maintenance. Please check out first.")

    def before_submit(self):
        # Validate room status before creating a maintenance request
        # room = frappe.get_doc("Rooms", self.room)
        # if room.room_status != "Available":
        #     frappe.throw(f"Room {self.room} is currently not available for maintenance. Please check out first.")

        # Automatically set room status to Maintenance
        room = frappe.get_doc("Rooms", self.room)
        room.room_status = "Maintenance"
        room.save()

    def on_submit(self):
        # Log maintenance assignment
        frappe.msgprint(f"Maintenance request for Room {self.room} has been assigned to {self.assigned_to}.")

    def on_update_after_submit(self):
        # Reflect maintenance status changes on the linked room
        room = frappe.get_doc("Rooms", self.room)
        if self.maintenance_status == "In Progress":
            room.room_status = "Maintenance"
        elif self.maintenance_status == "Completed":
            room.room_status = "Available"  # Maintenance completed, room is now available
        room.save()

    def on_cancel(self):
        # Revert room status if the maintenance request is cancelled
        room = frappe.get_doc("Rooms", self.room)
        if room.room_status == "Maintenance":
            room.room_status = "Available"  # Assume room becomes available after cancellation
        room.save()
