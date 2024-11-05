from stackapi import StackAPI
from datetime import datetime
import time

# Set up the StackAPI client
site = StackAPI('mattermodeling', key='API_Key', access_token='App_Access_Token')
site.max_pages = 2  # Adjust as needed, you will need the API key and access_token if you need max_pages > 25
site.page_size = 100  # Maximize the number of results per request

# Function to fetch answers for a given question
def fetch_best_answer(question_id):
    answers = site.fetch(f'questions/{question_id}/answers', sort='votes', filter='withbody')
    if 'items' in answers and answers['items']:
        # Look for accepted answer first
        for answer in answers['items']:
            if answer.get('is_accepted'):
                return answer['body']
        # If no accepted answer, return the one with the highest votes
        return answers['items'][0]['body']
    return None

# Function to fetch questions and their best answers
def fetch_questions_with_answers(from_date, to_date):
    questions_data = []
    questions = site.fetch('questions', fromdate=from_date, todate=to_date, min=1, sort='votes', filter='withbody')
    for question in questions['items']:
        question_title = question.get('title')
        question_body = question.get('body')
        question_id = question.get('question_id')
        best_answer = fetch_best_answer(question_id)

        if best_answer:
            questions_data.append({
                'title': question_title,
                'body': question_body,
                'best_answer': best_answer
            })
        time.sleep(0.2)  # Add delay to prevent rate limiting
    return questions_data

# Save data to a .txt file
def save_to_txt(data, filename='Q&A.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(f"Question: {entry['title']}\n")
            f.write(f"Body: {entry['body']}\n")
            f.write(f"Best Answer: {entry['best_answer']}\n")
            f.write("\n" + "="*80 + "\n\n")

# Define the date range and fetch questions and answers
from_date = int(datetime(2020, 1, 1).timestamp())
to_date = int(datetime(2024, 11, 5).timestamp())

questions_data = fetch_questions_with_answers(from_date, to_date)
save_to_txt(questions_data)
print("Data saved to Q&A.txt")
