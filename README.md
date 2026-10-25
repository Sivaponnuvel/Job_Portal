# 💼 JobPortal – Full Stack Job Portal

## 📌 Project Description

This is a **JobPortal** web application built using **React.js, Vite, Tailwind CSS, Django, Django REST Framework, and PostgreSQL**.

The project provides a simple job application platform where users can register, log in, browse available job opportunities, and apply for jobs. It integrates a React frontend with a Django REST API to manage user information, job listings, and job applications.

---

## 🚀 Features

### 📝 User Registration
* User registration with username, email, and password
* Form validation using required fields
* Registration API integration with Django REST Framework
* Display registration success and error messages

### 🔐 User Login
* User login using username and password
* Login API integration with Django
* Store user ID and username in `localStorage`
* Redirect to the jobs page after successful login
* Display login status messages

### 💼 Job Listings
* Fetch jobs dynamically from the Django REST API
* Display job title and company name
* Show job location and salary range
* Display job posting date
* Navigate to individual job application pages

### 📩 Job Application
* Apply for jobs using the Apply Now button
* Dynamic job routing using React Router
* Retrieve job ID using `useParams()`
* Use the logged-in user's ID when submitting applications
* Display application success and error messages
* Handle API request errors
* Prevent duplicate applications through backend validation

### 🧭 Navigation
* Page navigation using React Router DOM
* Navigate between registration, login, jobs, and application pages
* Back to Jobs navigation
* Display logged-in user's name and profile initial

---

## 🛠️ Technologies Used

* React.js
* Vite
* JavaScript (ES6+)
* Tailwind CSS
* React Router DOM
* Python
* Django
* Django REST Framework
* PostgreSQL
* HTML5
* CSS3
* Fetch API
* Git and GitHub

---

## 🗄️ Database

PostgreSQL is used as the relational database for storing application data.

The project uses Django models and Django REST Framework serializers to manage data.

Main data entities include:

* `User` – Stores user account information
* `Job` – Stores available job details
* `Application` – Stores job application records

---

## 🔄 REST API Operations

### Create (POST)
* Register a new user
* Log in through the login API
* Submit a job application

### Read (GET)
* Test the backend API
* Fetch available job listings

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/hello` | Test Django API |
| POST | `/register` | Register a user |
| POST | `/login` | Authenticate a user |
| GET | `/jobs` | Retrieve job listings |
| POST | `/apply` | Submit a job application |

---

## 🧩 Project Structure

```text
Job_Portal/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── RegisterPage.jsx
│   │   ├── LoginPage.jsx
│   │   ├── JobListPage.jsx
│   │   └── ApplyJobPage.jsx
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   └── ...
│
├── .gitignore
└── README.md
```

*Note: The backend structure is representative. Update it if your Django application uses separate folders for models, serializers, views, and URLs.*

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Sivaponnuvel/Job_Portal.git
```

### 2. Open the project folder

```bash
cd Job_Portal
```

### 3. Create and activate a Python virtual environment

```bash
python -m venv env
```

For Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

### 4. Install backend dependencies

```bash
pip install django djangorestframework django-cors-headers psycopg2-binary
```

### 5. Configure PostgreSQL

Create a PostgreSQL database and configure the database credentials in Django's `settings.py`.

### 6. Run database migrations

Navigate to the directory containing `manage.py`:

```bash
cd backend
python manage.py migrate
```

### 7. Start the Django backend

```bash
python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000/
```

### 8. Install frontend dependencies

Open another terminal:

```bash
cd frontend
npm install
```

### 9. Start the React application

```bash
npm run dev
```

Open the local URL displayed by Vite, usually:

```text
http://localhost:5173/
```

---

## ✨ Key Functionalities

* React Functional Components
* React Hooks (`useState`, `useEffect`, `useActionState`)
* Dynamic Routing using React Router DOM
* REST API Integration
* Fetch API and JSON data handling
* User state storage using `localStorage`
* Django REST Framework serializers
* PostgreSQL database integration
* Form validation and API error handling
* Dynamic job application submission
* Duplicate application validation
* Responsive UI using Tailwind CSS
* Component-based architecture
* Frontend and backend integration

---

## 📌 Future Improvements

* 🔐 Secure authentication using Django's authentication system
* 🚪 User logout functionality
* 👤 User profile management
* 🔍 Search and filter jobs
* 📄 Detailed job descriptions
* 📋 My Applications page
* 📊 Track application status
* 🏢 Recruiter dashboard
* ➕ Recruiters can post and manage jobs
* 🛡️ Protected routes and API authorization
* 🧪 Automated testing
* 🌐 Deploy the application online

---

## 🙋‍♂️ Author

**Sivaponnuvel S**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
