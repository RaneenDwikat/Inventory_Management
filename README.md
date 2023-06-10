# Inventory Management Web Application

The Inventory Management Web Application is a Flask-based web application designed to manage the inventory of a list of products in 
respective warehouses. It is intended for use in shops or warehouses that need to keep track of various products and their locations.

### Database Tables

1. Product (product_id): Stores information about products.
2. Location (location_id): Stores information about locations.
3. ProductMovement (movement_id, timestamp, from_location, to_location, product_id, qty): Tracks the movement of products between locations.

Please note that primary keys for Product table and Location table can be of type text or varchar. However, ProductMovement generate its 
primary key automatically.

### Views

&#9675; Add/Edit/View Product: Allows users to add, and view product details.

<img src="https://github.com/RaneenDwikat/Inventory_Management/blob/main/secreenshots/products.png">

&#9675; Add/Edit/View Location: Enables users to add, and view location information.

<img src="https://github.com/RaneenDwikat/Inventory_Management/blob/main/secreenshots/locations.png">

&#9675; Add/Edit/View ProductMovement: Provides functionality to add, edit, and view product movement records.

<img src="https://github.com/RaneenDwikat/Inventory_Management/blob/main/secreenshots/movements.png">

### Report

The application offers a report feature that shows the product balance in each location. This report provides an overview of the 
quantities of products available in different locations.

<img src="https://github.com/RaneenDwikat/Inventory_Management/blob/main/secreenshots/reports.png">

## Technologies Used

- Flask: A lightweight Python web framework.
- HTML: Markup language for creating the user interface of the application.
- Bootstrap: open-source front-end framework for enhancing the visual appearance of the application.
- MySQL: store and manage the data.
