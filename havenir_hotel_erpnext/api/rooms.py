import frappe


def get_available_rooms():
    """Return rooms with Vacant status"""
    return frappe.get_all(
        "Rooms", filters={"status": "Vacant"}, fields=["name", "room_number"]
    )
