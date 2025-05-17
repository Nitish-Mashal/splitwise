# Copyright (c) 2025, Nitish Mashal and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FriendsCircle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from splitwise.splitwise.doctype.user_friend.user_friend import UserFriend

		friends: DF.Table[UserFriend]
		user: DF.Link
	# end: auto-generated types
	pass
