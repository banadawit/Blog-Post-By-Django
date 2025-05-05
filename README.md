# 🎯 Django Blog Project

A simple yet functional blog application built with Django. This project allows users to create, view, and manage blog posts, with both an admin interface and clean templates for public viewing.

## ✨ Features

- **Post Management**
  - 🖊️ Create, update, and delete blog posts
  - 📄 View individual blog post details
  - 📃 List all blog posts on the homepage
  - 📆 Automatically shows post creation date

- **Admin Features**
  - 🔒 Admin interface for managing posts
  - 👤 User authentication ready (can be extended)

- **Technical Features**
  - � Clean and modular project structure (ready for scaling)
  - 🧪 Ready for REST API integration with Django REST Framework (optional)
  - 🛠️ Well-organized templates for easy customization

## 🛠️ Tech Stack

**Backend:**  
- Django (Python)

**Database:**  
- SQLite (default; easily swappable for PostgreSQL/MySQL)

**Frontend:**  
- Django Templates (HTML)
- Bootstrap-ready (easy to integrate)

**Admin Panel:**  
- Django's built-in admin (customizable)

## 🚀 Getting Started

### 🛠️ Setup Instructions

## 🚀 Getting Started

### 🛠️ Setup Instructions

Run these commands sequentially in your terminal:

```bash
# Clone repository and enter directory
git clone https://github.com/banadawit//Blog-Post-By-Django.git
cd django-blog

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create admin user (follow prompts)
python manage.py createsuperuser

# Run development server
python manage.py runserver
