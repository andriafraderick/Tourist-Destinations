

## Project Overview
A comprehensive Django REST Framework application for managing tourist destinations with a beautiful, modern UI inspired by TripAdvisor.

## Features
- ✅ Full CRUD operations using Generic API Views
- ✅ User authentication with dependent dropdown (Country → State → District)
- ✅ Advanced search and filtering
- ✅ Pagination (12 items per page)
- ✅ Google Maps integration
- ✅ Image upload support
- ✅ RESTful API endpoints
- ✅ MySQL database backend

## Prerequisites
- Python 3.8 or higher
- MySQL Server (via XAMPP or standalone)
- pip (Python package manager)

## Step-by-Step Installation

### 1. Set Up MySQL Database

1. Start XAMPP and ensure Apache and MySQL are running
2. Open phpMyAdmin (http://localhost/phpmyadmin)
3. Create a new database named `tourist_destination`:
   ```sql
   CREATE DATABASE tourist_destination CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

### 2. Create Project Structure

Create the following directory structure:

```
tourist_destinations/
├── tourist_destinations/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── destinations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
├── accounts/
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── destinations/
│   │   ├── destination_list.html
│   │   ├── destination_detail.html
│   │   ├── destination_form.html
│   │   └── destination_confirm_delete.html
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       └── profile.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── media/
├── manage.py
└── requirements.txt
```

### 3. Set Up Virtual Environment

```bash
# Navigate to project directory
cd tourist_destinations

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

Create `requirements.txt` with:
```
Django==4.2.7
djangorestframework==3.14.0
mysqlclient==2.2.0
django-cors-headers==4.3.0
Pillow==10.1.0
django-filter==23.3
```

Install packages:
```bash
pip install -r requirements.txt
```

**Note:** If `mysqlclient` installation fails on Windows:
- Download the appropriate wheel file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
- Install: `pip install mysqlclient-2.x.x-cpxx-cpxxm-win_amd64.whl`

### 5. Create Django Project

```bash
django-admin startproject tourist_destinations .
python manage.py startapp destinations
python manage.py startapp accounts
```

### 6. Configure Files

Copy all the provided code files to their respective locations:

1. **tourist_destinations/settings.py** - Main settings
2. **tourist_destinations/urls.py** - Main URL configuration
3. **destinations/models.py** - Database models
4. **destinations/serializers.py** - API serializers
5. **destinations/views.py** - View logic
6. **destinations/urls.py** - Destination URLs
7. **destinations/admin.py** - Admin configuration
8. **accounts/views.py** - Authentication views
9. **accounts/urls.py** - Account URLs
10. All HTML templates in `templates/` folder
11. **static/css/styles.css** - Styling
12. **static/js/main.js** - JavaScript functionality

### 7. Create Required Files

Create empty `__init__.py` files in:
- `tourist_destinations/`
- `destinations/`
- `accounts/`

Create `destinations/apps.py`:
```python
from django.apps import AppConfig

class DestinationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'destinations'
```

Create `accounts/apps.py`:
```python
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
```

### 8. Create Media and Static Directories

```bash
mkdir media
mkdir media/destinations
mkdir static
mkdir static/css
mkdir static/js
mkdir static/images
```

### 9. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 10. Create Superuser

```bash
python manage.py createsuperuser
```

Enter username, email (optional), and password.

### 11. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 12. Add Sample Data

Start the development server:
```bash
python manage.py runserver
```

Access admin panel at http://127.0.0.1:8000/admin/

### 13. Access the Application

- **Homepage:** http://127.0.0.1:8000/
- **Destinations:** http://127.0.0.1:8000/destinations/list/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **API Endpoints:**
  - Countries: http://127.0.0.1:8000/api/countries/
  - States: http://127.0.0.1:8000/api/states/
  - Districts: http://127.0.0.1:8000/api/districts/
  - Destinations: http://127.0.0.1:8000/api/api/destinations/

## API Endpoints

### Countries
- `GET /api/countries/` - List all countries
- `POST /api/countries/` - Create country
- `GET /api/countries/{id}/` - Get country details
- `PUT /api/countries/{id}/` - Update country
- `DELETE /api/countries/{id}/` - Delete country

### States
- `GET /api/states/` - List all states
- `GET /api/states/?country={id}` - Filter by country
- `POST /api/states/` - Create state
- `GET /api/states/{id}/` - Get state details
- `PUT /api/states/{id}/` - Update state
- `DELETE /api/states/{id}/` - Delete state

### Districts
- `GET /api/districts/` - List all districts
- `GET /api/districts/?state={id}` - Filter by state
- `POST /api/districts/` - Create district
- `GET /api/districts/{id}/` - Get district details
- `PUT /api/districts/{id}/` - Update district
- `DELETE /api/districts/{id}/` - Delete district

### Destinations
- `GET /api/api/destinations/` - List all destinations (paginated)
- `GET /api/api/destinations/?search={query}` - Search destinations
- `GET /api/api/destinations/?weather={type}` - Filter by weather
- `GET /api/api/destinations/?state={id}` - Filter by state
- `POST /api/api/destinations/` - Create destination (requires authentication)
- `GET /api/api/destinations/{id}/` - Get destination details
- `PUT /api/api/destinations/{id}/` - Update destination
- `DELETE /api/api/destinations/{id}/` - Delete destination

## Features Demonstration

### 1. User Registration & Login
1. Navigate to http://127.0.0.1:8000/accounts/register/
2. Create a new account
3. Login with credentials

### 2. Add Destination
1. Click "Add Destination" in navbar
2. Select Country (triggers state dropdown)
3. Select State (triggers district dropdown)
4. Select District
5. Fill in other details
6. Upload image (optional)
7. Submit

### 3. Search & Filter
1. Go to Destinations page
2. Use search box for keywords
3. Filter by weather type
4. Filter by country
5. Results update automatically

### 4. View & Edit
1. Click on any destination card
2. View full details
3. Click "Edit" (if owner)
4. Update information
5. Save changes

### 5. Pagination
- Browse through multiple pages
- 12 destinations per page
- Page navigation at bottom

## Troubleshooting

### MySQL Connection Error
```
django.db.utils.OperationalError: (2003, "Can't connect to MySQL server")
```
**Solution:** Ensure MySQL server is running in XAMPP

### mysqlclient Installation Error
**Solution:** 
- Windows: Use wheel file from lfd.uci.edu
- Mac: `brew install mysql` then `pip install mysqlclient`
- Linux: `sudo apt-get install python3-dev libmysqlclient-dev`

### Static Files Not Loading
**Solution:**
```bash
python manage.py collectstatic
```
Ensure DEBUG=True in settings.py for development


### Run Development Server
```bash
python manage.py runserver

🧪 Testing the API

You can test API endpoints using:

Test with cURL:
curl http://127.0.0.1:8000/api/countries/

Test Creating a Destination
curl -X POST http://127.0.0.1:8000/api/api/destinations/ \
-H "Content-Type: application/json" \
-d '{
  "place_name": "My Beach",
  "weather": "sunny",
  "state": 1,
  "district": 2,
  "description": "A beautiful beach"
}'

Test with Postman / Thunder Client

Import API endpoints
Add authentication headers
Test CRUD operations

🛡️ Security Notes

Before going to production:

1. Set DEBUG=False
2. Add Allowed Hosts
ALLOWED_HOSTS = ['your-domain.com']

3. Use Environment Variables

(Do NOT hardcode passwords)

4. Use HTTPS

Use Cloudflare or hosting provider SSL.

✨ Future Enhancements

You can extend the project with:

🌍 Interactive map view with markers

📌 Favorite destinations (Like button)

⭐ Reviews & Ratings

🧳 Wishlist / itinerary planner

🔍 Advanced filters (price, season, activity type)

📍 Auto-detect user's country using IP

🔐 JWT Authentication for mobile apps

📊 Admin dashboard with charts

🔄 Infinite scrolling UI

🤝 Contributing

Contributions are welcome!

Fork the project

Create a feature branch

git checkout -b feature/amazing-feature


Commit changes

Create a Pull Request

👍 Credits

Django REST Framework

Bootstrap

Google Maps Platform

Unsplash (Preview Images)

📜 License

This project is licensed under the MIT License.
You are free to modify and distribute as long as you include attribution.

🎉 Final Notes

Thank you for exploring TravelHub – Tourist Destinations Platform!

If you like this project, don’t forget to ⭐ star the repository on GitHub.
Happy coding! 🚀🌍✨
