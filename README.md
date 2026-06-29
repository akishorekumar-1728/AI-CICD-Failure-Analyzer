# 🤖 AI CI/CD Failure Analyzer

A smart DevOps tool that automatically detects GitHub Actions CI/CD failures and uses AI to analyze root causes and suggest fixes.

---

## 🚀 Live Demo

https://ai-cicd-failure-analyzer.onrender.com/

---

## 📌 Features

- 🔁 Real-time GitHub Actions monitoring via Webhooks
- 📊 Tracks CI/CD builds (Success / Failed)
- 🤖 AI-powered failure analysis and explanation
- 🧠 Automatic root cause detection using LLM
- 🗄️ SQLite database storage for build history
- 🔍 Search builds by repository name
- 🌐 Flask-based web dashboard

---

## 🏗️ Tech Stack

- Python (Flask)
- GitHub Actions
- GitHub Webhooks
- SQLite Database
- HTML/CSS (Frontend)
- OpenAI / LLM API (for analysis)
- Render (Deployment)

---

## ⚙️ How It Works

1. GitHub Actions runs CI/CD pipeline
2. GitHub sends webhook to Flask server
3. Flask stores build status in database
4. AI analyzes failure logs
5. Dashboard displays results in real-time

---

## 📊 Dashboard Preview

- Total Builds
- Successful Builds
- Failed Builds
- Recent Build History
- AI Failure Explanation

---

## 📸 Screenshots

### 1. Dashboard Overview

![alt text](<Screenshot 2026-06-29 133526.png>)

### 2. AI Failure Analysis Section

![alt text](<Screenshot 2026-06-29 133552.png>) ![alt text](<Screenshot 2026-06-29 133542.png>)

### 3. GitHub Actions Page

![alt text](<Screenshot 2026-06-29 133715.png>)

### 4.Webhook Activity (GitHub Settings)

## ![alt text](<Screenshot 2026-06-29 133655.png>)

## 🧪 Example Failure Detected

```

ModuleNotFoundError: No module named 'requests'

```

### AI Analysis:

- Missing dependency in requirements.txt
- Fix: Add `requests` to requirements file and reinstall dependencies

---

## 📁 Project Structure

```

AI-CICD-Failure-Analyzer/
│
├── app.py
├── database.py
├── llm_helper.py
├── ai_helper.py
├── requirements.txt
├── templates/
├── logs/
└── failures.db

```

---

## 🔥 Key Highlights

- Fully automated CI/CD monitoring system
- Real-world DevOps debugging tool
- AI-assisted error resolution
- Production-style webhook integration

---

## 📈 Future Improvements

- Slack / Email alerts for failures
- Graph-based analytics dashboard
- Multi-repo support
- Advanced AI fix suggestions (auto PR generation)

---

## 👨‍💻 Author

A Kishore Kumar  
GitHub: https://github.com/akishorekumar-1728

---

## ⭐ If you like this project

Give a star ⭐ and feel free to contribute!
