from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def format_gemma_comment(gemma_comment):
    """Formats the comment generated by Gemma."""
    return f"\n{gemma_comment}\n\n" if gemma_comment else "# About Your Commit:\n Error: Gemma output is missing or empty.\n\n"

def format_measures(measures_data):
    """Formats the measures data into a readable string."""
    if not measures_data:
        return "Error: Measures data is missing or empty."
    return "\n".join(
        f"- {measure['metric']}: {measure['value']}" + (" (Best Value)" if measure.get('bestValue') else "")
        for measure in measures_data
    )

def format_issues(issues_list):
    """Formats the issues list into a readable string."""
    if not issues_list:
        return "# Issues\nError: Issues list is missing or empty.\n\n"
    return "\n".join(f"{issue}" for issue in issues_list)

def format_similarity(similarity_percentage):
    """Formats the similarity percentage text."""
    return f"\n{similarity_percentage}\n\n" if similarity_percentage else "# Similarity Percentage\n Error: Similarity percentage is missing or empty."

def create_github_check_run(owner_repo_name, sha, token, output_text):
    """Creates a check run on GitHub with the given details."""
    url = f'https://api.github.com/repos/{owner_repo_name}/check-runs'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': 'Commit Power',
        'head_sha': sha,
        'status': 'completed',
        'conclusion': 'success',
        'output': {
            'title': 'Check Result',
            'summary': 'Score:',
            'text': output_text
        }
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response

@app.route('/', methods=['POST'])
def create_check_run():
    try:
        # Extract data from request
        data = request.json
        issues_list = data.get('issues_list', [])
        measures_data = data.get('measures_data', [])
        token = data.get('token', '')
        sha = data.get('sha', '')
        owner_repo_name = data.get('owner_repo_name', '')
        gemma_comment = data.get('gemma_comment', '')
        similarity_percentage = data.get('similarity_percentage', '')

        # Format the data
        gemma_comment_text = format_gemma_comment(gemma_comment)
        formatted_measures = format_measures(measures_data)
        formatted_issues = format_issues(issues_list)
        similarity_percentage_text = format_similarity(similarity_percentage)

        # Create the full output text
        output_text = (
            "![image](https://github.com/user-attachments/assets/4c64b855-b5e6-40ec-8958-9f9d1bc4cd76)\n" +
            gemma_comment_text +
            f"\n\n# Similartiy Percentage\n{similarity_percentage_text}\n\n" +
            f"# Measures\n{formatted_measures}\n\n" +
            f"# Issues\n{formatted_issues}\n\n"
        )

        # Send request to create the check run on GitHub
        create_github_check_run(owner_repo_name, sha, token, output_text)

        return jsonify({'message': 'Event received'}), 200

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Request error occurred: {req_err}'}), 500
    except KeyError as key_err:
        return jsonify({'error': f'Key error: {key_err}'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8087)
