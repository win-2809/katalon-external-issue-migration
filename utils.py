import apis


def filterTestCasesByRepo(projectID, path, repoID):
    data = apis.getTestCasesByPath(projectID, path).get('content')

    testCases = []

    for testCase in data:
        if repoID != '' and testCase.get('testProject') is not None and testCase.get('testProject').get('id') == int(repoID):
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
                "repoName": testCase.get('testProject').get('name')
            }
            testCases.append(testCaseDetails)
        elif repoID == '' and testCase.get('testProject') is None:
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
                "repoName": 'Uploaded Data'
            }
            testCases.append(testCaseDetails)
        else:
            print("Given path doesn't match")
            continue

    return testCases
