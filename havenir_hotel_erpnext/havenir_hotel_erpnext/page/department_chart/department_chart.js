
// "havenir_hotel_erpnext.havenir_hotel_erpnext.page.department_chart.department_chart.get_children";
// frappe.pages['department-chart'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'None',
// 		single_column: true
// 	});
// }

frappe.pages["department-chart"].on_page_load = function (wrapper) {
		frappe.ui.make_app_page({
			parent: wrapper,
			title: __("Department Chart"),
			single_column: true,
		});
	
		$(wrapper).bind("show", () => {
			frappe.require("hierarchy-chart.bundle.js", () => {
				let department_chart;
				let method = "havenir_hotel_erpnext.havenir_hotel_erpnext.page.department_chart.department_chart.get_children";
	
				if (frappe.is_mobile()) {
					department_chart = new hrms.HierarchyChartMobile("Department", wrapper, method);
				} else {
					department_chart = new hrms.HierarchyChart("Department", wrapper, method);
				}
	
				frappe.breadcrumbs.add("HR");
				department_chart.show();
			});
		});
	};
