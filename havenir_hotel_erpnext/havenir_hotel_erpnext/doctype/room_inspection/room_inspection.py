# Copyright (c) 2024, Havenir and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class RoomInspection(Document):
# 	pass


import frappe
from frappe.model.document import Document

class RoomInspection(Document):
    def before_save(self):
        # Ensure the room is in Checked In status before allowing inspection
        room = frappe.get_doc("Rooms", self.room)
        if room.room_status != "Checked In":
            frappe.throw(f"Room {self.room} must be in 'Checked In' status before inspection.")

    def before_submit(self):
        # Ensure that the inspection status is either "Clear" or "Damaged" before submitting
        if self.inspection_status not in ["Clear", "Damaged"]:
            frappe.throw("Inspection must be completed (Clear or Damaged) before submitting.")

    def on_submit(self):
        # Update the room's inspection status
        room = frappe.get_doc("Rooms", self.room)
        room.inspection_status = self.inspection_status
        room.save()

        frappe.msgprint(f"Room {self.room} inspection status updated to {self.inspection_status}.")

    def on_cancel(self):
        # Revert the inspection status to "Not Inspected" when cancelled
        room = frappe.get_doc("Rooms", self.room)
        room.inspection_status = "Not Inspected"
        room.save()

        frappe.msgprint(f"Room {self.room} inspection status reverted to 'Not Inspected'.")
