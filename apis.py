import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()
username = os.environ['username']
apiKey = os.environ['apiKey']
hostURL = os.environ['hostURL']

def getTestCasesByPath(projectID, path):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        "type": "TestCase",
        "conditions": [
            # Get test object by project ID (required)
            {
                "key": "Project.id",
                "operator": "=",
                "value": f"{projectID}"
            },
            # Get test object by path (required)
            {
                "key": "path",
                "operator": "=",
                "value": f"{path}"
            }
        ],
        "pagination": {
            "page": 0,
            "size": 300,
            # Short list of test object by a field
            "sorts": [
                "id, asc"
            ]
        }
    }

    response = requests.post(f"{hostURL}/api/v1/search", headers=headers, auth=HTTPBasicAuth(username, apiKey), json=data).json()

    return response

def getExternalRequirements(projectID, testCaseID):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        "type": "ExternalRequirement",
        "conditions": [
            # Get test object by project ID (required)
            {
                "key": "Project.id",
                "operator": "=",
                "value": f"{projectID}"
            },
            # Get test object by test case ID (required)
            {
                "key": "TestCase.id",
                "operator": "=",
                "value": f"{testCaseID}"
            }
        ],
        "pagination": {
            "page": 0,
            "size": 300,
            # Short list of test object by a field
            "sorts": [
                "id, asc"
            ]
        }
    }

    response = requests.post(f"{hostURL}/api/v1/search", headers=headers, auth=HTTPBasicAuth(username, apiKey), json=data).json()

    return response

def getExternalXrayTests(projectID, testCaseID):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        "type": "ExternalXrayTest",
        "conditions": [
            # Get test object by project ID (required)
            {
                "key": "Project.id",
                "operator": "=",
                "value": f"{projectID}"
            },
            # Get test object by test case ID (required)
            {
                "key": "TestCase.id",
                "operator": "=",
                "value": f"{testCaseID}"
            }
        ],
        "pagination": {
            "page": 0,
            "size": 300,
            # Short list of test object by a field
            "sorts": [
                "id, asc"
            ]
        }
    }

    response = requests.post(f"{hostURL}/api/v1/search", headers=headers, auth=HTTPBasicAuth(username, apiKey), json=data).json()

    return response

def updateExternalRequirements(externalIssueID, objectID, projectID):
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "issueId": f"{externalIssueID}",
        "objectType": "TEST_CASE",
        "objectId": f"{objectID}"
    }

    response = requests.post(f"{hostURL}/api/v1/external-issue?projectId=" + f"{projectID}", headers=headers, auth=HTTPBasicAuth(username, apiKey), json=data).json()

    return response

def updateExternalXrayTests(externalIssueID, objectID, projectID):
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "issueId": f"{externalIssueID}",
        "objectType": "XRAY_TEST_CASE",
        "objectId": f"{objectID}"
    }

    response = requests.post(f"{hostURL}/api/v1/external-issue?projectId=" + f"{projectID}", headers=headers, auth=HTTPBasicAuth(username, apiKey), json=data).json()

    return response