# Assignment Submission  
Name: Pedakanti Manoj Kumar Reddy

---

## Q1 – Web App for Mass Users Worldwide

For this question I built a small full‑stack web app and also described how I would run it at scale.

### Tech stack I chose

- **Frontend**: React.js  
  I used React to build a simple single‑page UI where I can add a user (name + email) and see the list of users.

- **Backend**: Python with Flask  
  The backend is a small Flask API. It exposes:
  - `GET /api/users` – returns all users as JSON.
  - `POST /api/users` – takes `name` and `email`, validates them, saves to the DB and returns the created user.
  I added `flask-cors` so the React app (running on a different port) can call the API.

- **Database**: PostgreSQL (in Docker) and SQLite (local fallback)  
  I used `flask-sqlalchemy` to define a `User` model with `id`, `name`, and `email`.  
  - When I run with Docker, the backend connects to a Postgres container using `DATABASE_URL`.  
  - When I run without Docker, it falls back to a local SQLite file (`users.db`).

### How I run the web app

**With Docker (recommended):**

```bash
cd webapp
docker compose up --build
```

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000/api/users`

Docker Compose starts three services together:
- `db` – Postgres database
- `backend` – Flask API (talks to Postgres)
- `frontend` – React app (talks to the API)

**Without Docker (uses SQLite):**

Terminal 1 – backend:

```bash
cd webapp/backend
pip install -r requirements.txt
python app.py
```

Terminal 2 – frontend:

```bash
cd webapp/frontend
npm install
npm run dev
```

### How I would scale this for worldwide users

If I had to serve a large number of users globally, I would:
- Keep **React** on the frontend and deploy it on a service like Vercel or Netlify.
- Run the **Flask** backend (or a Node.js/Express backend) in containers on AWS/GCP, behind a load balancer.
- Use a managed relational DB like **AWS RDS (PostgreSQL)**, with read replicas in multiple regions.
- Put a **CDN** (e.g. Cloudflare) in front of the static assets for faster delivery.
- Use **Docker** and **Docker Compose / orchestration** to keep environments consistent.

---

## Q2 – Automated Multi‑Step Form Filling

For this question I used **Python + Selenium** to automate filling and submitting a web form.

### Tools and idea

- **Language**: Python  
- **Library**: Selenium  
  Selenium lets my Python script control a real browser (open pages, type into inputs, click buttons, wait for elements).

### What my script does

The script in `automation/form_automation.py`:
- Opens the DemoQA practice form: `https://demoqa.com/automation-practice-form`.
- Fills in:
  - First name, last name
  - Email
  - Phone number
  - Address
- Selects the gender radio button (using an explicit wait and a JavaScript click to avoid click interception by ads).
- Scrolls down and clicks the **Submit** button.
- Prints `"Form submitted successfully!"` and closes the browser.

### Running the automation without Docker

```bash
cd automation
pip install -r requirements.txt
python form_automation.py
```

This expects Chrome + ChromeDriver to be available on the machine.

### Running the automation with Docker and Selenium container

I also containerised this so it runs in a controlled environment:

- `automation/Dockerfile` builds a Python image that runs `form_automation.py`.
- `automation/docker-compose.yml` defines two services:
  - `selenium`: runs a Selenium server + Chromium browser (`seleniarm/standalone-chromium`), and exposes a noVNC UI on `http://localhost:7900`.
  - `automation`: runs my Python script and connects to Selenium using WebDriver (`SELENIUM_REMOTE_URL=http://selenium:4444/wd/hub`).

Commands:

```bash
cd automation
docker-compose up selenium          # starts Selenium + browser
```

Then, in another terminal:

```bash
cd automation
docker-compose up --build automation
```

If I open `http://localhost:7900/?autoconnect=1&resize=scale` in my browser, I can actually watch the Chromium browser inside the container filling and submitting the form.

### Why I chose Selenium

- I am comfortable with Python.
- Selenium is a standard tool for web automation and testing.
- It can wait for dynamic elements, interact with complex pages, and supports multiple browsers (Chrome, Firefox, etc.).
- By combining Selenium with Docker, I can run the same automation reliably on different machines.
