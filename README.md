# 📘 Hotel Booking API Documentation

## 📌 Project Overview

The Hotel Booking API is a RESTful service built with Django & Django REST Framework (DRF) that allows users to book hotel rooms, check booking details, and manage booking statuses. The system supports room types, guest details, check-in/out dates, and provides status tracking of bookings.

## 🛠️ Tech Stack

1. Backend Framework: Django 4.x

2. API: Django REST Framework (DRF)

3. Database: SQLite (development) / PostgreSQL (production-ready)

4. Authentication: Token/JWT (optional for secured routes)

5. Optional Integrations: Email Notifications, Payment Processing

## ✅ Core Features

1. Room Booking: Create a booking by selecting room type, check-in/out dates, and guest information.

2. View Bookings: Retrieve all bookings (admin) or user-specific bookings.

3. Update Booking: Modify booking details (e.g., dates, room type).

4. Cancel Booking: Delete or mark a booking as cancelled.

5. Booking Status: Status options include pending, confirmed, and cancelled.

6. Room Types: Standard, Deluxe, Suite.

## 🗂️ Booking Data Structure

1. Field 	Type Description
2. id	 AutoField	Unique booking identifier
3. guest_name	String	Name of the guest
4. email	EmailField	Guest email
5. phone	CharField	Guest phone number
6. room_type	ChoiceField	Room Type: standard, deluxe, suite
6. check_in	DateField	Check-in date
7. check_out	DateField	Check-out date
8. number_of_guests	IntegerField	Number of guests for the booking
9. status	ChoiceField	Booking status: pending, confirmed, cancelled
10. created_at	DateTimeField	Date and time booking was created

# 📌 API Endpoints

# Method	Endpoint	Description

1. GET	/api/bookings/	Retrieve all bookings
2. POST	/api/bookings/	Create a new booking
3. GET	/api/bookings/{id}/	Retrieve a specific booking
4. PUT	/api/bookings/{id}/	Update booking details
5. DELETE	/api/bookings/{id}/	Cancel or delete booking

# 🔐 Authentication (Optional)
JWT or Token Authentication can be enforced on routes for secure access.

1. Admin users can have privileges like confirming or cancelling bookings.

# 📈 Future Enhancements

1. Payment Integration: Flutterwave, Stripe, Paystack

2. Email Notifications: Send booking confirmations and cancellations

3. Room Availability Checking: Prevent booking on unavailable dates

4. Search & Filtering: By date, guest name, room type, status

5.  Rate Limiting: To prevent API abuse

# 🚀 Deployment Options

1. Local Development: SQLite database, Django runserver

2. Production: Deployed on Render, Railway, Heroku, or AWS EC2 with PostgreSQL

## 🤝 Target Users

1.Hotel Administrators: Manage all bookings

2. Customers/Guests: Make and manage their own bookings

# 🧩 Sample JSON (Booking Creation)

{
    "guest_name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "08012345678",
    "room_type": "deluxe",
    "check_in": "2025-07-20",
    "check_out": "2025-07-25",
    "number_of_guests": 2
}


# 🧑‍💻 Developer Contact

Developer: Abayomi Robert Onawole

Email: Abayomirobertonawole@gmail.com

GitHub Repository: https://github.com/yomex96/Django_hotel-api.git
