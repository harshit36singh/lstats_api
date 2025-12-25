import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

@app.get("/leetcode/{username}")
def get_user_stats(username: str):
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        username
        submitStats: submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
        profile {
          ranking
          reputation
          userAvatar
        }
        badges {
          id
          name
          shortName
          icon
          displayName
        }
        userCalendar {
          submissionCalendar
        }
       
      }
      allQuestionsCount {
        difficulty
        count
      }
    }
    """
    variables = {"username": username}
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Origin": "https://leetcode.com",
    }

    response = requests.post(
        LEETCODE_GRAPHQL,
        json={"query": query, "variables": variables},
        headers=headers
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="LeetCode API error")

    data = response.json().get("data", {})
    matched_user = data.get("matchedUser")
    all_questions = data.get("allQuestionsCount", [])

    if not matched_user:
        raise HTTPException(status_code=404, detail="User not found")

    stats = matched_user["submitStats"]["acSubmissionNum"]
    solved = {item["difficulty"]: item["count"] for item in stats}
    total_questions = {item["difficulty"]: item["count"] for item in all_questions}

    calendar_str = matched_user["userCalendar"]["submissionCalendar"]
    calendar_data = json.loads(calendar_str) if calendar_str else {}
    active_days = sum(1 for count in calendar_data.values() if count > 0)

    badges = matched_user.get("badges", []) 

    return {
        "username": matched_user["username"],
        "ranking": matched_user["profile"]["ranking"],
        "reputation": matched_user["profile"]["reputation"],
        "profilePic": matched_user["profile"]["userAvatar"],
        "badges": badges,
        "easySolved": solved.get("Easy", 0),
        "mediumSolved": solved.get("Medium", 0),
        "hardSolved": solved.get("Hard", 0),
        "totalSolved": sum(solved.values()),
        "easyTotal": total_questions.get("Easy", 0),
        "mediumTotal": total_questions.get("Medium", 0),
        "hardTotal": total_questions.get("Hard", 0),
        "overallTotal": sum(total_questions.values()),
        "calendar": matched_user["userCalendar"]["submissionCalendar"],
        "activeDays": active_days,
    
    }

