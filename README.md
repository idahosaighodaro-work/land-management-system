# 🦅 EagleEye: Land Management System

EagleEye is a geo-intelligence platform designed to empower users with coordinate-based land analysis, subscription access, and secure user management. Built with FastAPI, SQLAlchemy, and MySQL, this system integrates technical excellence with a deeper mission to serve and uplift.

---

## ⚙️ Project Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/idahosaighodaro-work/land-management-system.git
cd land-management-system
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory with the following:
```
DATABASE_URL=mysql+pymysql://<user>:<password>@<host>/<database>
SECRET_KEY=your_secret_key
```

Replace `<user>`, `<password>`, `<host>`, and `<database>` with your actual MySQL credentials.

---

## 🗄️ Database Setup

### 1. Create the MySQL Database
Log into MySQL and run:
```sql
CREATE DATABASE eagleeye_db;
```

### 2. Apply Migrations (if using Alembic)
```bash
alembic upgrade head
```

If you're not using Alembic, ensure your models are synced manually or via a script.

---

## 🚀 Run the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the interactive API documentation.

---

## 🧪 What Testers Should Focus On

### ✅ Core Features
- **User Registration & Login**  
  - Validate input handling and error messages  
  - Confirm JWT authentication flow

- **Subscription Management**  
  - Test subscription creation and access control  
  - Ensure correct user status updates

- **Coordinate-Based Land Analysis**  
  - Input coordinates and verify analysis results  
  - Check for edge cases and invalid inputs

---

### 🐞 Bug Reports & Suggestions
Please report:
- UI/UX issues or confusing flows
- API errors or unexpected behavior
- Performance bottlenecks or slow responses

Use GitHub Issues and label them as `bug`, `enhancement`, or `question`.

---

## 🙏 Purpose Behind the Platform

EagleEye is more than a tool — it's a mission. Built to serve those who cannot build for themselves, this platform reflects a commitment to excellence, clarity, and faith. Every line of code is written with intention to glorify God and uplift others.

---

## 🤝 Contributing

If you'd like to contribute:
1. Fork the repo
2. Create a feature branch
3. Submit a pull request with clear documentation

---

## 📫 Contact

For questions, feedback, or collaboration:
**Email:** idahosa@eagleeye.io  
**GitHub:** [@idahosaighodaro-work](https://github.com/idahosaighodaro-work)

---

> _“Unless the Lord builds the house, the builders labor in vain.” — Psalm 127:1_

```

---

Let me know if you'd like to add screenshots, diagrams, or a testing checklist. This README is ready to guide your testers with clarity and purpose.
