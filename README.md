# ShopShore - E-commerce Website

## Table of Contents
- [Overview](#overview)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Overview

Welcome to ShopShore, an open-source e-commerce website built with Django and Bootstrap. ShopShore is designed to provide a feature-rich and user-friendly shopping experience for customers. This project was created as a learning journey and is open for contributions from the developer community.

Key Features:
- User registration and email verification.
- Well-organized product catalog.
- Secure shopping cart and checkout process.
- PayPal integration for secure payments.
- Responsive design for various devices.
- Product reviews and ratings.
- User profiles with order history.

## Demo

Explore the live demo at [hotash.xyz](https://hotash.xyz).

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: Bootstrap 5
- **Server**: VPS with NGINX and Gunicorn

## Installation

To set up ShopShore locally, follow these steps:

1. Clone the repository:
   ```shell
   git clone https://github.com/mdsajjadhossain25/shopshore.git
   ```
2. Create a virtual environment and activate it:
   ```shell
   python -m venv environment_name
   ```
3. Or you can use virtualenv to create virtual environment
  ```shell
     pip install virtualenv
     virtualenv enviroment_name
```
4. Install dependencies:
   ```shell
     pip install -r requirements.txt
   ```
5. Migrate the database:
   ```shell
     python manage.py migrate
     ```
6. Create super user:
     ```shell
       python manage.py createsuperuser
     ```
7. Run the server:
    ```shell
      python manage.py runserver
    ```
### Important note:
Make sure you add the env-sample file required code to avoid error.
### Usage:
- Visit the website at hotash.xyz.
- Browse the product catalog, add items to your cart, and proceed to checkout.
- Create an account or log in to manage your orders and profile.
- Enjoy a seamless shopping experience!
- 
### Features
- User Registration and Email Verification: New users receive email verification links to activate their accounts.
- Product Catalog: Well-organized product listings with descriptions, prices, and reviews.
- Shopping Cart: Add and manage items in your cart with ease.
- Secure Checkout: Add billing and shipping details and review your order before payment.
- Payment Integration: PayPal integration ensures secure and convenient payments.
- Responsive Design: Enjoy a seamless experience on various devices.
- Search and Navigation: Find products easily with search and filters.
- Customer Reviews: Share your thoughts by leaving product reviews.
- User Profiles: Manage your order history and profile settings.
- Marketing and Promotion: Promote featured products to attract customers.
- Open Source: This project is open-source. Contribute to its development on GitHub.
### Contributing
We welcome contributions to make ShopShore even better! Please refer to our Contribution Guidelines for details on how to get involved. See CONTRIBUTION.md





