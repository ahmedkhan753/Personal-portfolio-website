
Ahmed's Portfolio Website

This is a personal portfolio website built with Flask and styled using HTML and CSS. The site includes multiple sections like Home, Projects, About, and Contact. Visitors can browse through the content and use the contact form to send messages directly to my email.


---

Features

Simple and responsive layout

Internal CSS for styling (no external stylesheets)

Contact form that sends messages to Gmail using SMTP

Navigation between pages handled through Flask routing

Easily customizable HTML templates



---

Project Structure

portfolio/
│
├── static/
│   └── images/             # For profile pictures or project screenshots
│
├── templates/
│   ├── index.html          # Home page
│   ├── about.html          # About section
│   ├── projects.html       # Projects portfolio
│   └── contact.html        # Contact form page
│
├── app.py                  # Flask application logic
├── .env                    # Environment variables (email credentials)
├── .gitignore              # Hides .env, users.db, etc.
└── requirements.txt        # Python dependencies


---

Getting Started

1. Clone the repository

git clone https://github.com/your-username/portfolio.git
cd portfolio

2. Install the dependencies

pip install -r requirements.txt

3. Set up environment variables

Create a .env file in the root folder and add your Gmail and app password:

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_generated_app_password

> Note: You must enable 2-Step Verification in your Google Account and generate an App Password to use with SMTP.



4. Run the Flask app

python app.py

Open your browser and go to http://localhost:5000


---

Notes

If your images don’t load, make sure they are in the static/images folder and referenced like this in your HTML:

<img src="{{ url_for('static', filename='images/your-image.jpg') }}">

All routes (Home, Projects, About, Contact) are handled inside app.py with corresponding templates in the templates/ folder.


---
