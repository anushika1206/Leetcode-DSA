import requests
import os

url = "https://leetcode.com/graphql"

headers = {
    "Content-Type": "application/json",
    "Cookie": "LEETCODE_SESSION=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMTc4MTc2NjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1MTMzODA3MjFkZjlmYTEzMDI5YjA1NTBmZTg0ODc4ZmJjMDlmZmFiYTI4N2QxZjA5ZmQyYTFlZjRiODlhMjAiLCJzZXNzaW9uX3V1aWQiOiI3MzNkZDkyZCIsImlkIjoxNzgxNzY2NSwiZW1haWwiOiJhbnVzaGlrYTA2MTJAZ21haWwuY29tIiwidXNlcm5hbWUiOiJBbnVfMTIwNiIsInVzZXJfc2x1ZyI6IkFudV8xMjA2IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTc3ODA4ODM3MywiaXAiOiIyNDA5OjQwZDE6MTBiNDo0ZjNlOjhjZDE6Y2Q1Yjo3ODIxOjQxM2YiLCJpZGVudGl0eSI6ImI4NzU0M2VjYmMwYmE2MTBkOWYwNmY5ZjJjNDMyYTQ2IiwiZGV2aWNlX3dpdGhfaXAiOlsiOWM1ODNjYjZhZWI4M2RjYjA4M2UxYzM5MjRkNjE0ZDQiLCIyNDA5OjQwZDE6MTBiNDo0ZjNlOjhjZDE6Y2Q1Yjo3ODIxOjQxM2YiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.LCer0cwEo0UpB1f7sdjReHV6mwUo7NnQ_haTx8QEEgU; csrftoken=DDlz0sxphgDNAOIJn27EqlxvhvJSnsvL"
}

def get_code(submission_id):
    query = {
        "query": """
        query getSubmission($id: Int!) {
          submissionDetails(submissionId: $id) {
            code
          }
        }
        """,
        "variables": {
            "id": submission_id
        }
    }

    response = requests.post(url, json=query, headers=headers)
    data = response.json()

    # Debug once
    # print("DEBUG:", data)

    try:
        return data["data"]["submissionDetails"]["code"]
    except:
        print("Error fetching code for ID:", submission_id)
        return ""
    
def save_code(title, code, lang):
    folder = title.replace(" ", "-")
    os.makedirs(folder, exist_ok=True)

    ext = {
        "cpp": "cpp",
        "python": "py",
        "java": "java"
    }.get(lang, "txt")

    with open(f"{folder}/solution.{ext}", "w", encoding="utf-8") as f:
        f.write(code)



query = {
    "query": """
    query {
      submissionList(offset: 0, limit: 5) {
        submissions {
          id
          title
          titleSlug
          lang
        }
      }
    }
    """
}

response = requests.post(url, json=query, headers=headers)

data = response.json()

submissions = data["data"]["submissionList"]["submissions"]

for sub in submissions:
    sub_id = int(sub["id"])
    title = sub["title"]
    lang = sub["lang"]

    print(f"Fetching: {title}")

    code = get_code(sub_id)

    if code:   # ✅ only save if code exists
        save_code(title, code, lang)

