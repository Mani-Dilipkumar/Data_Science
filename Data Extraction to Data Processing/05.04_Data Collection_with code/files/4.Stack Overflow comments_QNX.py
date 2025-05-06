import requests
import pandas as pd
import time

def fetch_qnx_questions_and_answers(tag="qnx", pagesize=100):
    """
    Fetch all questions tagged with 'qnx' from StackOverflow using the Stack Exchange API.
    Also fetches accepted answers for each question if available.
    """
    question_url = "https://api.stackexchange.com/2.3/questions"
    answer_url = "https://api.stackexchange.com/2.3/questions/{question_id}/answers"
    params = {
        "order": "desc",
        "sort": "activity",
        "tagged": tag,
        "site": "stackoverflow",
        "pagesize": pagesize,
        "filter": "withbody",
        "key": "",  # Provided key
        "client_id": ""                   # Provided client id
    }
    
    all_data = []
    page = 1

    while True:
        params["page"] = page
        print(f"Fetching page {page} of questions...")
        response = requests.get(question_url, params=params)
        
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            break
        
        data = response.json()
        items = data.get("items", [])
        
        if not items:
            break
        
        for question in items:
            question_id = question.get("question_id")
            question_title = question.get("title")
            question_link = question.get("link")
            question_score = question.get("score")
            question_creation_date = question.get("creation_date")
            question_tags = ", ".join(question.get("tags", []))
            question_body = question.get("body")
            
            # Fetch accepted answer for the question
            answer_params = {
                "order": "desc",
                "sort": "activity",
                "site": "stackoverflow",
                "filter": "withbody",
                "key": "rl_xknFMmTUGFcDYWdZ8CSzTpPS8"
            }
            
            answer_response = requests.get(answer_url.format(question_id=question_id), params=answer_params)
            answer_body = ""
            if answer_response.status_code == 200:
                answer_data = answer_response.json()
                answers = answer_data.get("items", [])
                
                for answer in answers:
                    if answer.get("is_accepted", False):
                        answer_body = answer.get("body")
                        break  # Stop once the accepted answer is found
            
            # Append the collected data
            all_data.append({
                "question_id": question_id,
                "title": question_title,
                "link": question_link,
                "score": question_score,
                "creation_date": question_creation_date,
                "tags": question_tags,
                "question_body": question_body,
                "accepted_answer_body": answer_body
            })
        
        if not data.get("has_more", False):
            break
        
        page += 1
        time.sleep(1)  # Respect API rate limits
        
    return all_data

# Fetch all questions tagged with "qnx"
qnx_data = fetch_qnx_questions_and_answers(tag="qnx", pagesize=100)
print(f"Fetched {len(qnx_data)} questions with answers.")

# Extract the fields of interest
df = pd.DataFrame(qnx_data)

# Save the DataFrame to an Excel file
output_filename = "stack_qnx.csv"
df.to_csv(output_filename, index=False)
print(f"Data saved to '{output_filename}'")
