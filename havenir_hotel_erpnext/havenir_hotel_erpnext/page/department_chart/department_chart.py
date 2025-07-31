import frappe
from frappe.query_builder.functions import Count


@frappe.whitelist()
def get_children(parent=None, company=None, exclude_node=None):
	filters = [["disabled", "=", 0]]
	# if company and company != "All Companies":
	# 	filters.append(["company", "=", company])

	if parent and company and parent != company:
		filters.append(["parent_department", "=", parent])
	else:
		filters.append(["parent_department", "=", ""])

	if exclude_node:
		filters.append(["name", "!=", exclude_node])

	departments  = frappe.get_all(
		"Department",
		fields=[
			"department_name  as name",
			"name as id",
			"lft",
			"rgt",
			"parent_department",
			"is_group as title",
		],
		filters=filters,
		order_by="name",
	)

	for department  in departments:
		department.connections = get_connections(department.id, department.lft, department.rgt)
		department.expandable = bool(department.connections)

	return departments


def get_connections(employee: str, lft: int, rgt: int) -> int:
	Department = frappe.qb.DocType("Department")
	query = (
		frappe.qb.from_(Department)
		.select(Count(Department.name))
		.where((Department.lft > lft) & (Department.rgt < rgt) & (Department.disabled == 0))
	).run()

	return query[0][0]
