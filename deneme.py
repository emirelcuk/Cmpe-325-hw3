from flask import Flask, request, jsonify
import requests
import logging 

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
 
@app.route('/', methods=['POST'])
def webhook():
    try:
        event = request.headers.get('X-GitHub-Event')
        payload = request.json
        if event == 'push':
            owner_repo_name = payload['repository']['full_name']
            sha = payload['after']
          
            logging.info(f"Measures data: {measures_data}")
            check_run(token, sha, owner_repo_name, gemma_output, similarity_percentage, issues_list, measures_data)
            return jsonify({'status': 'received'}), 200




def gemma2(commit_message, commit_code):
    try:
        new_int = 0
        response = requests.post('http://gemma2_service:8083', json={'commit_message': commit_message, 'commit_code': commit_code})
        response.raise_for_status()
        gemma_comment = response.json().get('gemma_comment')
        return {"gemma_output":gemma_output,"gemma_comment":gemma_comment}
    except requests.RequestException as e:
        print("error")
        logging.error(f"Error in Gemma2: {e}", exc_info=True)
        return None

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
            'owner_repo_name': owner_repo_name,
            'gemma_output': gemma_output["gemma_output"],
            'gemma_comment':gemma_output["gemma_comment"],
            'similarity_percentage': similarity_percentage,
            'issues_list': issues_list,
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
