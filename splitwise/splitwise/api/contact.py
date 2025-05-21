# import frappe

# @frappe.whitelist(allow_guest=True)
# def submit_contact(name, mobile, email, message):
#     # Save to Communication Doctype or your custom one
#     doc = frappe.get_doc({
#         "doctype": "Communication",
#         "subject": f"Contact from {name}",
#         "content": f"<b>Mobile:</b> {mobile}<br><b>Email:</b> {email}<br><br>{message}",
#         "sender": email,
#         "communication_type": "Communication"
#     })
#     doc.insert(ignore_permissions=True)
#     return {"status": "success", "message": "Message submitted"}

# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def submit_contact():
#     data = frappe.local.form_dict
#     name = data.get("name")
#     mobile = data.get("mobile")
#     email = data.get("email")
#     message = data.get("message")

#     if not (name and mobile and email):
#         return {"message": "Required fields missing"}

#     # You can also store this in a custom Doctype instead of logs
#     frappe.sendmail(
#         recipients=[frappe.db.get_single_value("Website Settings", "email_recipient") or "your@email.com"],
#         sender=email,
#         subject="New Contact Form Submission",
#         message=f"<b>Name:</b> {name}<br><b>Mobile:</b> {mobile}<br><b>Email:</b> {email}<br><b>Message:</b><br>{message or '-'}"
#     )

#     return {"message": "Message submitted"}

# Importing necessary modules from the Frappe framework
import frappe
from frappe import _

# Declares a whitelisted function that can be accessed via REST API (e.g., from a frontend form)
@frappe.whitelist(allow_guest=True)
def submit_contact():
    # Retrieves data from the request (typically sent via POST from a form)
    data = frappe.local.form_dict

    # Extracts individual fields from the form submission
    name = data.get("name")
    mobile = data.get("mobile")
    email = data.get("email")
    message = data.get("message")

    # Validates that the required fields are provided: name, mobile, and email
    if not (name and mobile and email):
        return {"message": "Required fields missing"}

    # If validation passes, an email is sent to a specific recipient
    # This is useful for alerting the admin or support team of a new contact form submission
    frappe.sendmail(
        recipients=["your@email.com"],  # Replace with the actual recipient email address
        sender=email,  # The sender's email is taken from the form input
        subject="New Contact Form Submission",  # Subject of the email
        message=f"""  # HTML body of the email containing form submission details
            <b>Name:</b> {name}<br>
            <b>Mobile:</b> {mobile}<br>
            <b>Email:</b> {email}<br>
            <b>Message:</b> {message or "-"}  # If message is empty, show a dash
        """
    )

    # Return a success message as JSON response
    return {"message": "Message submitted"}