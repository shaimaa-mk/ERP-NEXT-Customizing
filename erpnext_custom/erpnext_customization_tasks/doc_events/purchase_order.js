


setup: function(frm) {

		if (frm.doc.is_old_subcontracting_flow) {
			frm.set_query("reserve_warehouse", "supplied_items", function() {
				return {
					filters: {
						"company": frm.doc.company,
						"name": ['!=', frm.doc.supplier_warehouse],
						"is_group": 0
					}
				}
			});
		}

		frm.set_indicator_formatter('item_code',
			function(doc) { return (doc.qty<=doc.received_qty) ? "green" : "orange" })

		frm.set_query("expense_account", "items", function() {
			return {
				query: "erpnext.controllers.queries.get_expense_account",
				filters: {'company': frm.doc.company}
			}
		});

		frm.set_query("fg_item", "items", function() {
			return {
				filters: {
					'is_stock_item': 1,
					'is_sub_contracted_item': 1,
					'default_bom': ['!=', '']
				}
			}
		});
	},