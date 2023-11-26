import requests

# Replace YOUR_USERNAME and YOUR_TOKEN with your GitHub username and access token
username = 'br5kly'
token = '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'
repo_name = 'hy'

# API endpoint for creating a repository
url = f'https://api.github.com/user/repos'

# Request headers with authentication
headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/json',
}

# Request payload with the repository name
data = {
    'name': repo_name,
}

# Make the POST request to create the repository
response = requests.post(url, headers=headers, json=data)

# Check if repository creation was successful
if response.status_code == 201:
    print(f'Repository "{repo_name}" created successfully!')
else:
    print(f'Error creating repository: {response.status_code} - {response.text}')
