# Product Review System (BackendEng Assignment)

A Django REST Framework API for managing products and user reviews with role-based access for admins and regular users.

---

## Features

-  **User Authentication**: Register, login, logout using Django's built-in auth system
-  **Admin Access**:
  - Create, update, delete products
-  **Regular User Access**:
  - View product list and details
  - Submit one review per product
-  **Product Ratings**:
  - Each product shows an average rating
  - Reviews include 1–5 rating and feedback
- **Public Access**:
  - Anyone can browse products and see reviews


## ⚙ Setup Instructions

```bash
git clone https://github.com/sachu1548/Product_Review.git
cd Product_Review
python -m venv env
source env/bin/activate       # On Windows: .\env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
