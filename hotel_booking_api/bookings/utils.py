from django.core.mail import send_mail
from django.conf import settings

def send_review_notification(review):
    subject = f"New Review Submitted by {review.guest_name}"
    message = (
        f"A new review has been submitted:\n\n"
        f"Guest: {review.guest_name}\n"
        f"Room Type: {review.room_type}\n"
        f"Rating: {review.rating}\n"
        f"Comment: {review.comment}\n"
    )
    recipient_list = ['abayomischolarship@gmail.com']  # Change to actual admin email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
