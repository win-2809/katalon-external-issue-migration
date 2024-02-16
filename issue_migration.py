import apis
import utils
import os
from dotenv import load_dotenv

load_dotenv()
username = os.environ['username']
projectID = os.environ['projectID']
sourcePath = os.environ['sourcePath']
destinationPath = os.environ['destinationPath']
sourceRepoName = os.environ['sourceRepoName']
destinationRepoName = os.environ['destinationRepoName']

def getSourceTestCases():
    testCases = utils.filterTestCasesByRepo(projectID, sourcePath, sourceRepoName)
    print("Source Test Cases: ")
    print(testCases)
    return testCases

def getDestinationTestCases():
    testCases = utils.filterTestCasesByRepo(projectID, destinationPath, destinationRepoName)
    print("Destination Test Cases: ")
    print(testCases)
    return testCases

def updateExternalIssues():
    sourceTestCases = getSourceTestCases()
    destinationTestCases = getDestinationTestCases()
    
    for destinationTestCase in destinationTestCases:
        for sourceTestCase in sourceTestCases:
            if sourceTestCase.get('name') == destinationTestCase.get('name'):
                destinationTestCase.get('externalRequirementIssueID').extend(item for item in sourceTestCase.get('externalRequirementIssueID') if item not in destinationTestCase.get('externalRequirementIssueID'))
                destinationTestCase.get('externalXrayTestIssueID').extend(item for item in sourceTestCase.get('externalXrayTestIssueID') if item not in destinationTestCase.get('externalXrayTestIssueID'))
                
    print("Updated Test Cases: ")
    print(destinationTestCases)
    
    for destinationTestCase in destinationTestCases:
        for issue in destinationTestCase.get('externalRequirementIssueID'):
            apis.updateExternalRequirements(issue, destinationTestCase.get('id'), projectID)
            
        for issue in destinationTestCase.get('externalXrayTestIssueID'):
            apis.updateExternalXrayTests(issue, destinationTestCase.get('id'), projectID)
    
    print("Process finished!")
    
    return {
        "status": "200",
        "message": "Success"
    }
    
def main():
    updateExternalIssues()