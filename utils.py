import apis


def filterTestCasesByRepo(projectID, path, repoName):
    data = apis.getTestCasesByPath(projectID, path).get('content')

    testCases = []

    for testCase in data:
        if repoName != 'Uploaded Data' and testCase.get('testProject') is not None and testCase.get('testProject').get('name') == repoName:
            # Get external requirement IDs
            externalRequirementIssueIDs = []
            externalRequirements = apis.getExternalRequirements(projectID, testCase.get('id')).get('content')
            for issue in externalRequirements:
                externalRequirementIssueID = issue.get('issueId')
                externalRequirementIssueIDs.append(externalRequirementIssueID)
            
            # Get external Xray test IDs
            externalXrayTestIssueIDs = []
            externalXrayTests = apis.getExternalXrayTests(projectID, testCase.get('id')).get('content')
            for issue in externalXrayTests:
                externalXrayTestIssueID = issue.get('issueId')
                externalXrayTestIssueIDs.append(externalXrayTestIssueID)

            testCaseDetails = {
                "id": testCase.get('id'),
                "name": testCase.get('name'),
                "path": testCase.get('path'),
                "externalRequirementIssueID": externalRequirementIssueIDs,
                "externalXrayTestIssueID": externalXrayTestIssueIDs,
                "repoName": repoName
            }
            testCases.append(testCaseDetails)
        elif repoName == 'Uploaded Data' and testCase.get('testProject') is None:
            # Get external requirement IDs
            externalRequirementIssueIDs = []
            externalRequirements = apis.getExternalRequirements(projectID, testCase.get('id')).get('content')
            for issue in externalRequirements:
                externalRequirementIssueID = issue.get('issueId')
                externalRequirementIssueIDs.append(externalRequirementIssueID)
            
            # Get external Xray test IDs
            externalXrayTestIssueIDs = []
            externalXrayTests = apis.getExternalXrayTests(projectID, testCase.get('id')).get('content')
            for issue in externalXrayTests:
                externalXrayTestIssueID = issue.get('issueId')
                externalXrayTestIssueIDs.append(externalXrayTestIssueID)

            testCaseDetails = {
                "id": testCase.get('id'),
                "name": testCase.get('name'),
                "path": testCase.get('path'),
                "externalRequirementIssueID": externalRequirementIssueIDs,
                "externalXrayTestIssueID": externalXrayTestIssueIDs,
                "repoName": repoName
            }
            testCases.append(testCaseDetails)
        else:
            print("Given path doesn't match")
            continue

    return testCases
