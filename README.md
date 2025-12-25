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
GET /{username}
```

Retrieves comprehensive LeetCode statistics for the specified user.

**Parameters:**
- `username` (path parameter) - LeetCode username

**Example Request:**
```bash
curl https://your-api-url.herokuapp.com/harshit36singh
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
curl http://localhost:5000/your-leetcode-username
```

## 💻 Usage Examples

### Python

```python
import requests

username = "harshit36singh"
response = requests.get(f"https://your-api-url.herokuapp.com/{username}")
data = response.json()

print(f"Total Solved: {data['totalSolved']}")
print(f"Acceptance Rate: {data['acceptanceRate']}%")
print(f"Ranking: {data['ranking']}")
```

### JavaScript (Node.js)

```javascript
const fetch = require('node-fetch');

async function getLeetCodeStats(username) {
  const response = await fetch(`https://your-api-url.herokuapp.com/${username}`);
  const data = await response.json();
  
  console.log(`Total Solved: ${data.totalSolved}`);
  console.log(`Acceptance Rate: ${data.acceptanceRate}%`);
  console.log(`Ranking: ${data.ranking}`);
}

getLeetCodeStats('harshit36singh');
```

### JavaScript (Browser/React)

```javascript
fetch('https://your-api-url.herokuapp.com/harshit36singh')
  .then(response => response.json())
  .then(data => {
    console.log('LeetCode Stats:', data);
    document.getElementById('totalSolved').textContent = data.totalSolved;
    document.getElementById('ranking').textContent = data.ranking;
  })
  .catch(error => console.error('Error:', error));
```

### cURL

```bash
# Basic request
curl https://your-api-url.herokuapp.com/harshit36singh

# Pretty print JSON
curl https://your-api-url.herokuapp.com/harshit36singh | jq .

# Save to file
curl https://your-api-url.herokuapp.com/harshit36singh > stats.json
```

### GitHub Profile README

Display your LeetCode stats in your GitHub profile:

```markdown
## 📊 My LeetCode Stats

![LeetCode Stats](https://your-api-url.herokuapp.com/harshit36singh)

<!-- Or use it with a stats card generator -->
```

---

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
- Initializes Flask server and configures CORS
- Defines the main API endpoint (`/{username}`)
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

## 🎨 Use Cases

### 1. **Portfolio Website**
Display your coding achievements on your personal website:

```html
<div id="leetcode-stats">
  <h2>My Coding Journey</h2>
  <p>Total Problems Solved: <span id="total-solved">Loading...</span></p>
  <p>Global Ranking: <span id="ranking">Loading...</span></p>
</div>

<script>
  fetch('https://your-api-url.herokuapp.com/your-username')
    .then(res => res.json())
    .then(data => {
      document.getElementById('total-solved').textContent = data.totalSolved;
      document.getElementById('ranking').textContent = data.ranking;
    });
</script>
```

### 2. **GitHub Profile README**
Showcase your LeetCode progress:

```markdown
## 💻 Coding Stats

- 🎯 Total Problems Solved: 250
- 🏆 LeetCode Ranking: #50,000
- ✅ Acceptance Rate: 65.4%
- 🔥 Contribution Points: 500

*Stats fetched via custom API*
```

### 3. **Discord Bot**
Create a bot that displays LeetCode stats:

```python
import discord
import requests

@bot.command()
async def leetcode(ctx, username):
    response = requests.get(f'https://your-api-url.herokuapp.com/{username}')
    data = response.json()
    
    embed = discord.Embed(title=f"LeetCode Stats - {username}")
    embed.add_field(name="Total Solved", value=data['totalSolved'])
    embed.add_field(name="Ranking", value=data['ranking'])
    
    await ctx.send(embed=embed)
```

### 4. **Slack Integration**
Daily stats reminder for your team:

```python
from slack_sdk import WebClient
import requests

def send_leetcode_stats(username):
    response = requests.get(f'https://your-api-url.herokuapp.com/{username}')
    data = response.json()
    
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel='#coding',
        text=f"📊 {username}'s LeetCode: {data['totalSolved']} solved!"
    )
```

### 5. **Mobile App**
React Native or Flutter app integration:

```javascript
// React Native
const fetchStats = async (username) => {
  try {
    const response = await fetch(`https://your-api-url.herokuapp.com/${username}`);
    const data = await response.json();
    setStats(data);
  } catch (error) {
    console.error('Error fetching stats:', error);
  }
};
```

### 6. **Analytics Dashboard**
Track multiple users' progress:

```python
import pandas as pd
import requests

usernames = ['user1', 'user2', 'user3']
stats = []

for username in usernames:
    response = requests.get(f'https://your-api-url.herokuapp.com/{username}')
    stats.append(response.json())

df = pd.DataFrame(stats)
print(df[['username', 'totalSolved', 'ranking']])
```

---

## 🔧 Configuration

### CORS Configuration

The API allows cross-origin requests from any domain. To restrict access:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["https://your-domain.com"],
        "methods": ["GET"],
        "allow_headers": ["Content-Type"]
    }
})
```

### Rate Limiting (Optional)

Add rate limiting to prevent abuse:

```bash
pip install Flask-Limiter
```

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@app.route('/<username>')
@limiter.limit("10 per minute")
def get_stats(username):
    # ... existing code
```

---

## 🐛 Error Handling

The API returns appropriate error responses:

### User Not Found
```json
{
  "status": "error",
  "message": "User not found",
  "username": "invalid_user"
}
```

### Internal Server Error
```json
{
  "status": "error",
  "message": "Failed to fetch data from LeetCode",
  "details": "Connection timeout"
}
```

---






