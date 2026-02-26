**HRM Backend – Django + FastAPI + PostgreSQL**

This project is a lightweight HRM (Human Resource Management) Backend System built using:

Django (ORM)

FastAPI (High-performance APIs)

PostgreSQL (Database)

Poetry (Dependency Management)

📁 Project Structure

After cloning, your project structure should look like this:

 hrm_backend/
    ├── core/
    ├── config/
    ├── manage.py
    └── main.py
🛠️ Setup Instructions (Run Locally)
1️⃣ Create Main Folder

First create a folder named:

hrm_backend

Then clone the repository inside it:

git clone <your-repository-url>
2️⃣ Create .env File

After cloning, create a .env file in the root directory and add the following keys:

SECRET_KEY=supersecretkey

POSTGRES_DB_NAME=..
POSTGRES_HOST=..
POSTGRES_USERNAME=...
POSTGRES_PASSWORD=..
POSTGRES_PORT=..

⚠️ Make sure to replace the values with your actual PostgreSQL credentials.

3️⃣ Install Dependencies Using Poetry

Install dependencies:

poetry install

Activate virtual environment:

poetry shell
4️⃣ Run the Backend Server

**Inside poetry shell, run:**

uvicorn hrm_backend.main:app --host 127.0.0.1 --port 8001 --reload

Now your backend will be running at:

http://127.0.0.1:8001
🌍 Live Deployment

**🔗 Live API URL (Temporary Deployment):**
Deployed via Vercel frontend with backend exposed using LocalExpose.
https://vite-react-ten-coral-37.vercel.app/

⚠️ Note:

The backend is currently exposed using LocalExpose.

This live URL is temporary and available only for 2 days.

Initially attempted deployment on Render, but due to free-tier limitations (shell access issues and configuration errors), LocalExpose was used as a temporary workaround to keep the project live. 
As we have the limited time so that's why i choose that way.

Future improvement: Proper deployment on Render/Railway with production-ready configuration.

⚙️ Tech Stack

Django

FastAPI

PostgreSQL

Poetry

Uvicorn

📌 Notes

Ensure PostgreSQL service is running before starting the backend.

Make sure your .env file is properly configured.

Do not commit .env file to GitHub (add it to .gitignore).
