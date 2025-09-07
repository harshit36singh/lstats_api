from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Origin": "https://leetcode.com",
        "Cookie": "LEETCODE_SESSION=your_session_cookie_here;"
    }

    response = requests.post(LEETCODE_GRAPHQL, json={"query": query, "variables": variables}, headers=headers)
    
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

    contest_data = matched_user.get("userContestRanking", {})
    badge_data = matched_user.get("contestBadge", {})

    return {
        "username": matched_user["username"],
        "ranking": matched_user["profile"]["ranking"],
        "reputation": matched_user["profile"]["reputation"],

        # Solved counts
        "easySolved": solved.get("Easy", 0),
        "mediumSolved": solved.get("Medium", 0),
        "hardSolved": solved.get("Hard", 0),
        "totalSolved": sum(solved.values()),

        # Total question counts
        "easyTotal": total_questions.get("Easy", 0),
        "mediumTotal": total_questions.get("Medium", 0),
        "hardTotal": total_questions.get("Hard", 0),
        "overallTotal": sum(total_questions.values()),

        # Calendar
        "calendar": matched_user["userCalendar"]["submissionCalendar"],

        # Contest info
        "contestRating": contest_data.get("rating"),
        "contestAttended": contest_data.get("attendedContestsCount"),
        "contestGlobalRanking": contest_data.get("globalRanking"),
        "contestTopPercentage": contest_data.get("topPercentage"),

        # Badge
       
    }
