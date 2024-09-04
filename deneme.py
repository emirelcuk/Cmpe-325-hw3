from flask import Flask, request, jsonify
import requests
import logging 
 
app = Flask(__name__)
   
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
  
@app.route('/', methods=['POST']) 
def webhook(): 
    try:

        
       

 



def fetch_jira(commit_message):
    try:
        response = requests.post('http://jira_service:8084', json={'commit_message': commit_message})
        response.raise_for_status()
        jira_issue = response.json().get('jira_issue')
        return jira_issue
    except requests.RequestException as e:
        logging.error(f"Error fetching JIRA issue: {e}", exc_info=True)
        return None

def text_embedding(commit_message, jira_tasks):
    try:
        response = requests.post('http://embedding_service:8085', json={'commit_message': commit_message, 'jira_tasks': jira_tasks})
        response.raise_for_status()
        similarity_percentage = response.json().get('similarity_percentage')
        return similarity_percentage
    except requests.RequestException as e:
        logging.error(f"Error in text embedding: {e}", exc_info=True)
        return None

def check_run(token, sha, owner_repo_name, gemma_output,similarity_percentage, issues_list, measures_data):
    try:
        response = requests.post('http://check_run_service:8087', json={
            'token': token,
            'sha': sha,
            
            'measures_data': measures_data
        })
        response.raise_for_status()
        return "Check-run successfully executed"
    except requests.RequestException as e:
        logging.error(f"Error in check run: {e}", exc_info=True)
        return None

def sonarqube(owner_repo_name):
    try:
        response = requests.post('http://sonarscanner_service:8088', json={'owner_repo_name': owner_repo_name})
        response.raise_for_status()
        issues_list = response.json().get('issues_list')
        measures_data = response.json().get('measures_data')
        return issues_list, measures_data
    except requests.RequestException as e:
        logging.error(f"Error fetching SonarQube data: {e}", exc_info=True)
        return None, None

if __name__ == '__main__':
    app.run(debug=True, port=8080 , host="0.0.0.0")
