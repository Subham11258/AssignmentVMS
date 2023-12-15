# AssignmentVMS

**Introduction**
The Vendor Management System, developed using Django, is a web application designed for streamlined vendor relationship management. It includes functionalities for managing vendor profiles, tracking purchase orders, and evaluating vendor performance.

Users can create, update, and delete vendor profiles, monitor purchase orders, and assess vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

Roadmap
Start and Plan: Understand the project scope and set up the basic structure.
Vendor Setup: Create a system to manage vendor information and test it.
Purchase Order Management: Develop purchase order forms and check their functionality.
Performance Evaluation: Add a scoring system for vendors and calculate scores dynamically.
Historical Tracking: Include a history feature to track vendor performance over time.
Testing Phase: Conduct thorough testing, find and fix bugs.
Deployment: Put the system online for use.
Maintenance: Keep an eye on the system, fix issues, and assist users.
Features
User/Admin can add or remove vendors.
Vendors can see the list of different members.
Admin can give the perfect calculations for performance.
Easy to use.
API endpoints can be checked using Django ORM.
No need for any tools for API endpoint checking.
API Reference
Vendor Profile Management:
POST /api/vendors/: Create a new vendor.
GET /api/vendors/: List all vendors.
GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
PUT /api/vendors/{vendor_id}/: Update a vendor's details.
DELETE /api/vendors/{vendor_id}/: Delete a vendor.
Purchase Order Tracking:
POST /api/purchase_orders/: Create a purchase order.
GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
PUT /api/purchase_orders/{po_id}/: Update a purchase order.
DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
Historical Performance:
GET /api/vendors/{vendor_id}/performance
Tech Stack
Stack: Python, Django, dbsqlite3
Server: localhost:8000
Installation
bash
virtualenv env
source venv/Scripts/activate
pip install django
pip install djangorestframework
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
**Access URLs:**

http://localhost:8000/vendors/ - for vendor list
http://localhost:8000/admin - for admin
Deployment
To deploy this project on git:

**Company**
This project is assigned by:

FATMUG, Delhi, India


**Support**
email: subhamguptaslg.1996@gmail.com
