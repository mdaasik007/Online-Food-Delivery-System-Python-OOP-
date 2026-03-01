🍔 Online Food Delivery System (Python OOP Mini Project)

A simple Online Food Delivery System built using Python to demonstrate core Object-Oriented Programming (OOP) concepts like:

✅ Inheritance

✅ Aggregation

✅ Composition

✅ Encapsulation

✅ Class Relationships

This project simulates how customers place food orders, restaurants manage menus, and delivery partners deliver orders.

📌 Project Overview

This system includes:

👤 Users

Customer

Delivery Partner

🏪 Restaurant

Add menu items

Create orders

🛒 Orders

Add multiple food items

Assign delivery partner

Mark as delivered

Calculate total bill automatically

🧠 OOP Concepts Used
1️⃣ Inheritance
class User
class Customer(User)
class DeliveryPartner(User)

Customer and DeliveryPartner inherit from User.

2️⃣ Aggregation

Restaurant has MenuItems.

Order has Customer and DeliveryPartner.

Objects exist independently.

3️⃣ Composition

Order contains OrderItems.

If Order is deleted, OrderItems are also deleted.

🏗️ Class Structure
🔹 User

Base class for all users.

🔹 Customer (Inherits User)

Customer ID

Address

🔹 DeliveryPartner (Inherits User)

Partner ID

Vehicle Type

Availability Status

🔹 MenuItem

Item ID

Name

Price

🔹 OrderItem

Stores quantity

Stores price snapshot

Calculates item total

🔹 Order

Order ID

Customer

Restaurant

Order Items

Delivery Partner

Status (Pending / Delivered)

Total Amount

🔹 Restaurant

Restaurant Name

Location

Menu Items

Orders

🚀 How to Run

Install Python (3.x)

Save the file as:

online_food_delivery.py

Run:

python online_food_delivery.py
🖥️ Sample Output
Order ID: 1001
Customer: Aasik
Restaurant: Snakers
Status: Pending
Items:
   Pizza x 2 = $320
   Biriyani x 1 = $200
Total Amount: $520
Delivery Partner: Mike

After delivery:

Status: Delivered
📂 Project Structure
Online-Food-Delivery-System/
│
├── online_food_delivery.py
└── README.md
🎯 Learning Outcomes

This project demonstrates:

Real-world system design using OOP

Object relationships (IS-A & HAS-A)

Clean class modeling

Order lifecycle management

Business logic implementation

🔮 Future Improvements

Add multiple restaurants

Add payment system

Store data using files or database

Add GUI using Tkinter

Convert to Web App using Flask/Django

Add order tracking system

👨‍💻 Author

Mohammed Aasik A
