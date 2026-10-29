import frappe
from frappe.utils import today

def get_upcoming_bookings():
    bk = frappe.qb.DocType("Booking")

    return (
        frappe.qb.from_(bk)
        .select(
            bk.name,
            bk.member,
            bk.resource,
            bk.booking_date,
            bk.start_time
        )
        .where(
            (bk.booking_date >= today()) &
            (bk.status.isin(["Pending Confirmation", "Confirmed"]))
        )
        .orderby(bk.booking_date)
        .run(as_dict=True)
    )

