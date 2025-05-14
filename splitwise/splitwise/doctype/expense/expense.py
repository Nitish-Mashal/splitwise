# Copyright (c) 2025, Nitish Mashal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Expense(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from splitwise.splitwise.doctype.expense_split.expense_split import ExpenseSplit

		amended_from: DF.Link | None
		amount: DF.Currency
		currency: DF.Link
		date: DF.Date
		description: DF.Data
		notes: DF.SmallText | None
		paid_by: DF.Link
		split_method: DF.Literal["Equally", "Manual"]
		splits: DF.Table[ExpenseSplit]
	# end: auto-generated types

	def before_save(self):
		self.apply_split()

	def apply_split(self):
		if self.split_method == "Equally":
			self.calculate_equal_split()
		else:
			# Manual split
			pass

	def calculate_equal_split(self):
		num_splits = len(self.splits)
		if num_splits == 0:
			frappe.throw("At least one split is required.")

		split_amount = self.amount / num_splits

		for s in self.splits:
			s.amount = split_amount
