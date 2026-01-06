# 📂 Projects Repository

This repository contains a collection of small-to-medium Python projects built as part of continuous learning and practical experimentation. Each folder represents a standalone project focused on a specific concept such as APIs, automation, email handling, or data processing.

The projects are intentionally modular and beginner-to-intermediate friendly, with an emphasis on **clean Python**, **real-world use cases**, and **hands-on practice**.

---

## 📁 Project Overview

### 1️⃣ `api_endpoints`

**Focus:** API fundamentals and endpoint handling

This project explores how to create, structure, and consume API endpoints using Python. It is designed to strengthen understanding of:

* RESTful API concepts
* Request/response cycles
* JSON handling
* Route definitions and parameter passing

**Key Concepts:**

* HTTP methods (GET, POST, etc.)
* Endpoint design
* API testing and debugging

---

### 2️⃣ `quizzler-app-start`
**Focus:** Application logic and user interaction
This is a quiz-based application that demonstrates how to structure application logic, manage state, and interact with user inputs. It is often used as a stepping stone toward GUI or API-driven applications.

**Key Concepts:**
* Object-oriented programming (OOP)
* Data structures
* Game / quiz logic
* Incremental feature building
---

### 3️⃣ `smtp_mailer`
**Focus:** Email automation using SMTP
This project demonstrates how to send emails programmatically using Python’s SMTP libraries. It is useful for automation tasks such as notifications, alerts, and scheduled messages.

**Key Concepts:**
* SMTP protocol
* Secure email authentication
* Environment variables for credentials
* Error handling for email delivery

**Typical Use Cases:**
* Automated emails
* Notifications
* Simple mailing scripts

---

### 4️⃣ `stock_news_api`
**Focus:** External API integration & automation
This project integrates stock market data with news APIs to fetch real-time or recent information about companies. It showcases how multiple APIs can be combined to build meaningful automation workflows.

**Key Concepts:**
* Third-party API integration
* API keys & environment variables
* Data filtering and formatting
* Conditional logic based on data changes

**Typical Use Cases:**
* Stock alerts
* Market monitoring
* Data-driven notifications

---

### 5️⃣ `weather_api`
**Focus:** Consuming public APIs and data parsing
This project fetches and processes weather data from an external API. It reinforces the fundamentals of making API requests and handling structured responses.

**Key Concepts:**
* API requests using Python
* JSON parsing
* Error handling
* Data extraction and presentation

**Typical Use Cases:**
* Weather lookups
* Automation scripts
* API practice projects

### 6️⃣ `habit_tracker`

**Focus:** State management and persistence
This project implements a simple habit tracking application to practice working with state, user input, and data persistence. It focuses on translating real-world behaviour (daily habits) into structured application logic.

**Key Concepts:**
* CRUD-style operations
* Data persistence (files or lightweight storage)
* Input validation
* Application flow control

**Typical Use Cases:**
* Personal productivity tools
* Learning stateful application design

---

## 🛠️ Repository Structure
```
PythonProject2/
│
├── projects/
│   ├── api_endpoints/
│   ├── habit_tracker/
│   ├── quizzler-app-start/
│   ├── smtp_mailer/
│   ├── stock_news_api/
│   └── weather_api/
│
├── __init__.py
├── .gitignore
├── README.md
└── .venv/
```
---
## 🛠️ Technologies Used
* Python 3
* REST APIs
* JSON
* SMTP
* Environment Variables
---


## 🚀 How to Use
### 1️⃣ Clone the repository
```bash

git clone https://github.com/Iyanuvicky22/pet_projects.git
cd pet_projects

```
---
### 2️⃣ Create and activate a virtual environment
**Windows:**
```bash

python -m venv .venv
.venv\Scripts\activate

```
**macOS / Linux:**
```bash

python3 -m venv .venv
source .venv/bin/activate

```
You should see `(.venv)` in your terminal once activated.

---
### 3️⃣ Install dependencies using `requirements.txt`
All shared dependencies for the projects are defined in the root `requirements.txt` file.

From the project root:
```bash

pip install -r requirements.txt

```
This ensures everyone runs the projects with the same package versions.

---
### 4️⃣ Run a project
Navigate into any project directory under `projects/` and run the main script.
Example:
```bash

cd projects/weather_api
python main.py

```
---
### 5️⃣ Adding or updating dependencies
If you install a new package:
```bash

pip install <package-name>

```
Update the dependency list:

```bash

pip freeze > requirements.txt

```

---
## Sites with API's token requirements
* `habit_tracker`: https://pixe.la/v1/
* `stock_news_api`: https://www.alphavantage.co/query,  https://newsapi.org/v2/everything, https://www.twilio.com/en-us
* `weather_api`: https://api.openweathermap.org
- Kindly do well to go through each website's documentation to understand the api usage.
---

---
## SMTP Email Usage
```
https://smtpbd.com/how-to-find-smtp-server-username-and-password/
```
---

---
## 📌 Notes
* Each project is self-contained.
* You have to get your API keys and credentials for each project for them to work. 
* Using Environment variables for sensitive data is very much recommended.
---

---
## 📈 Purpose

These projects are part of an ongoing **learning-by-building** approach, aimed at strengthening Python development, automation, and API integration skills through practical examples.
Feel free to explore, extend, or refactor any project as needed.

---

## Author
**The_VikingLord**
iyanuvicky@gmail.com
