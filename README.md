Assignment Submission  
Name: Pedakanti Manoj Kumar Reddy

--------------------------------------------------
Q1 – Web App
--------------------------------------------------

For this part I built a small full‑stack user app.

Frontend: React  
I used React to build a simple page where I can add a user (name + email) and see the list of users. The frontend calls the backend API using fetch.

Backend: Flask (Python)  
The backend is a basic Flask API with two main routes:
- GET /api/users – returns all users as JSON.
- POST /api/users – takes name and email from the request body, does a small validation and saves the user.
Cors is enabled so the React app (running on a different port) can call the API without issues.

Database: Postgres (Docker) and SQLite (local)  
I used SQLAlchemy with a simple User model (id, name, email). When I run with Docker, the backend connects to a Postgres container using an environment variable. When I run locally without Docker, it uses a SQLite file.

How to run with Docker:
1) cd webapp
2) docker compose up --build

Then:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000/api/users

How to run without Docker:

Backend:
1) cd webapp/backend
2) pip install -r requirements.txt
3) python app.py

Frontend:
1) cd webapp/frontend
2) npm install
3) npm run dev

Short note on scale:  
For more users, I would containerise the backend and database and run multiple instances behind a load balancer, and use a managed Postgres service. The code here is small, but the idea is to keep things stateless in the app and put the state in the database.

--------------------------------------------------
Q2 – Automated Multi‑Step Form Filling
--------------------------------------------------

For this part I used Python and Selenium to automate filling and submitting a web form.

I wrote a script that:
- Opens the DemoQA practice form page.
- Fills first name, last name, email, phone and address.
- Selects the gender radio button.
- Scrolls to the bottom and clicks the submit button.
- Prints a message and closes the browser.

Running without Docker:
1) cd automation
2) pip install -r requirements.txt
3) python form_automation.py

(This expects Chrome and ChromeDriver to be installed on the machine.)
