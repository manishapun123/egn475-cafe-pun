# EGN 475 Week 1 Assignment 1.1

A small Flask app with a home page and an about page.

## Set up on Windows

From this folder in the VS Code terminal:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, use the VS Code Command Prompt terminal and run:

```cmd
.venv\Scripts\activate
```

## Run the app

With the virtual environment active:

```powershell
flask --app app run --debug
```

Open these URLs in a browser:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/about
The app.py file includes comments explaining the Flask application, routes, functions, and return statements. Both the home page and about page were tested successfully.
## Week 2 – Project Selection and Planning

### Project Name
Café Calle Ocho

### Selected Option
Option A – Café Calle Ocho, Little Havana.

### Why I Chose This Project
I chose Café Calle Ocho because I am interested in building a café ordering system. I want to make it easier for customers to place orders and for kitchen staff to track orders from received to picked up.
### Problem Statement

Café Calle Ocho currently needs a simple way to manage customer orders and communicate order progress between customers and kitchen staff. This can cause long waiting times, confusion about order details, and difficulty tracking orders. Our prototype will provide a digital menu, allow customers to customize and place dine-in or takeout orders, and help kitchen staff update orders from received to preparing, ready, and picked up. This will make ordering faster, reduce confusion, and improve the customer experience.
### Target Personas

**Customer – Maria Rodriguez:** A regular customer who wants to order Cuban coffee and food quickly, customize her order, and pick it up without waiting in a long line.

**Staff Member – Carlos Martinez:** A kitchen employee who wants to receive orders, prepare food and drinks, and update order statuses easily.

### Must-Have Features

1. Digital menu with food, drinks, and snack categories.
2. Menu item details with prices and dietary information.
3. Options to customize size, milk, and add-ons.
4. Ability to place dine-in and takeout orders.
5. Checkout showing order items, quantities, and total price.
6. Kitchen order board showing received, preparing, ready, and picked up.
7. Order history for customers.

### Features Not Included in This Prototype

1. Online payments through the app.
2. Food delivery and delivery tracking.
3. SMS or email order notifications.
4. Customer loyalty points and rewards.