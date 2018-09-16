frappe.listview_settings['District Project'] = {
    add_fields: ["reporting_status"],

    get_indicator: function(doc) {
        if (doc.reporting_status == "Late") {
            return [__("Late"), "orange", "status,=,Late"];
        } else if (doc.reporting_status == "On Time") {
            return [__("On Time"), "green", "status,=,On Time"];
        }
    }
};