# CRM Django project
This is a simple CRM project using Django. It is a simple project that allows you to manage your customers and their orders.

# Installation
1. Clone the repository
2. Create .env file in the root directory and add the following variables
```
SECRET_KEY=your_secret_key
DEBUG=True
```
3. Cd into crm_project directory
```bash
cd crm_project
```
4. Run the following command to install the required packages
```bash
pip install -r requirements.txt
```
5. Run project
```bash
python manage.py migrate
python manage.py runserver
```

# Deployment
The project is deployed on Render. You can access it [here](https://crm-django-x29q.onrender.com/admin/)

Link API: [API](https://crm-django-x29q.onrender.com/api/)

Link Swagger: [Swagger](https://crm-django-x29q.onrender.com/api/swagger/)

