# 📊 LStats API - LeetCode Statistics API

A lightweight FastApi-based RESTful API that fetches and displays LeetCode user statistics. Perfect for showcasing your coding achievements on portfolios, GitHub profiles, or personal websites.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)


---

## 🎯 Overview

**LStats API** provides a simple and efficient way to retrieve LeetCode profile statistics without the complexity of GraphQL queries. This API serves as a RESTful wrapper around LeetCode's GraphQL endpoint, making it easy to integrate coding statistics into any application.

### ✨ Key Features

- 🚀 **Fast & Lightweight** - Built with Flask for optimal performance
- 📊 **Comprehensive Stats** - Get detailed problem-solving statistics
- 🎨 **Easy Integration** - RESTful API design for simple consumption
- 📱 **No Authentication Required** - Public endpoint for easy access

---

## 📑 Table of Contents

- [API Endpoints](#-api-endpoints)
- [Response Format](#-response-format)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Use Cases](#-use-cases)

---

## 🔌 API Endpoints

### Get User Statistics

```
GET /leetcode/{username}
```

Retrieves comprehensive LeetCode statistics for the specified user.

**Parameters:**
- `username` (path parameter) - LeetCode username

**Example Request:**
```bash
curl https://your-api-url.herokuapp.com/leetcode/harshit36singh
```

---

## 📦 Response Format

```json
{
  "status": "success",
  "username": "harshit36singh",
  "totalSolved": 250,
  "totalQuestions": 2500,
  "easySolved": 100,
  "totalEasy": 600,
  "mediumSolved": 120,
  "totalMedium": 1300,
  "hardSolved": 30,
  "totalHard": 600,
  "acceptanceRate": 65.4,
  "ranking": 50000,
  "contributionPoints": 500,
  "reputation": 10,
  "submissionCalendar": {
    "1640995200": 5,
    "1641081600": 3
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Request status (success/error) |
| `username` | string | LeetCode username |
| `totalSolved` | number | Total problems solved |
| `totalQuestions` | number | Total problems on LeetCode |
| `easySolved` | number | Easy problems solved |
| `totalEasy` | number | Total easy problems |
| `mediumSolved` | number | Medium problems solved |
| `totalMedium` | number | Total medium problems |
| `hardSolved` | number | Hard problems solved |
| `totalHard` | number | Total hard problems |
| `acceptanceRate` | number | Overall acceptance rate (%) |
| `ranking` | number | Global ranking |
| `contributionPoints` | number | LeetCode contribution points |
| `reputation` | number | User reputation score |
| `submissionCalendar` | object | Daily submission count (timestamp: count) |

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Development Setup

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/harshit36singh/lstats_api.git
cd lstats_api
```

2️⃣ **Create Virtual Environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Application**

```bash
python apileetcode.py
```

5️⃣ **Test the API**

Open your browser or use curl:

```bash
curl http://localhost:5000/leetcode/your-leetcode-username
```

## 📂 Project Structure

```
lstats_api/
│
├── __pycache__/                # Python bytecode cache
│   └── ...
│
├── apileetcode.py              # Main FastApi application
│   ├── FastAPi app initialization
│   ├── CORS configuration
│   ├── API endpoint definitions
│   ├── LeetCode GraphQL queries
│   └── Error handling
│
├── requirements.txt            # Python dependencies
│   ├── FastApi
│   ├── FastApi-CORS
│   ├── requests
│   ├── gunicorn
│   └── other dependencies
│
├── Procfile                    # Heroku deployment config
│   └── web: unicorn apileetcode:app
│
├── runtime.txt                 # Python version specification
│   └── python-3.x.x
│
├── .gitignore                  # Git ignore rules
│
└── README.md                   # Project documentation (this file)
```

### File Descriptions

#### `apileetcode.py`
The core FastApi application that:
- Initializes FastApi server and configures CORS
- Defines the main API endpoint (`/leetcode/{username}`)
- Queries LeetCode's GraphQL API
- Parses and formats response data
- Handles errors and edge cases

## 🛠️ Tech Stack

### Backend Framework
- **FastApi** - Lightweight Python web framework

### HTTP Client
- **Requests** - HTTP library for GraphQL queries

### APIs
- **LeetCode GraphQL API** - Data source for user statistics

---
