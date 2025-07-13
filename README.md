Blog App 📝

A full-stack Blog Application built with Django, Django REST Framework, HTML, CSS, and JavaScript. This app allows users to create, manage, and share blog posts with a clean, responsive interface and a robust RESTful API. Whether you're a writer or a developer, this app provides a seamless experience for blogging with features like user authentication, search functionality, and a dark mode toggle.

✨ Features
User Authentication: Secure login and post ownership using Django's authentication system.
CRUD Operations: Create, read, update, and delete blog posts through an intuitive UI and API.
Search Functionality: Easily find posts by searching titles or content.
Responsive Design: Clean and modern interface with a dark mode toggle for enhanced user experience.
RESTful API: Built with Django REST Framework for efficient data interaction.
Database Management: Structured storage for posts with fields for title, content, author, and timestamps.

🛠️ Technologies Used
Backend: Django, Django REST Framework, Python
Frontend: HTML, CSS, JavaScript
Database: SQLite (via Django ORM)
Version Control: Git, GitHub

🚀 Getting Started
Prerequisites
Python 3.8+
Django 4.x
Django REST Framework
Git

Installation
Clone the repository:
git clone https://github.com/your-username/blog-app.git
cd blog-app


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Apply migrations:
python manage.py migrate


Run the development server:
python manage.py runserver


Access the app:Open your browser and go to http://127.0.0.1:8000.


📂 Project Structure
blog-app/
├── blog/
│   ├── __init__.py
│   ├── admin.py        # Django admin configuration
│   ├── apps.py        # App configuration
│   ├── models.py      # Database models (Post)
│   ├── serializers.py # API serializers
│   ├── tests.py      # Test cases
│   ├── urls.py       # URL routing
│   ├── views.py      # API and view logic
├── templates/
│   ├── index.html     # Homepage with post listing
│   ├── post.html      # Post creation and display page
├── manage.py
└── README.md

🖥️ Usage

Create a Post: Log in, navigate to the "New Post" page, and publish your content.
Search Posts: Use the search bar to filter posts by title or content.
Manage Posts: Edit or delete your posts via the UI or API.
API Access: Interact with the RESTful API at /api/posts/ for programmatic access.

🛡️ API Endpoints

GET /api/posts/: List all posts (filtered by authenticated user).
POST /api/posts/: Create a new post.
GET /api/posts//: Retrieve a specific post.
PUT /api/posts//: Update a post.
DELETE /api/posts//: Delete a post.

🌟 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a Pull Request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙌 Acknowledgments

Built with love for learning and sharing knowledge.
Thanks to the Django and Django REST Framework communities for their amazing tools and documentation.


⭐ Star this repo if you find it useful!📬 For questions or feedback, open an issue or reach out via LinkedIn.
