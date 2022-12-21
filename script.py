import requests
import json
import os

BASE_URI = "https://api.github.com"
owner = os.environ.get("REPO_OWNER")
repo = os.environ.get("REPO_NAME")
token = os.environ.get("GITHUB_TOKEN")
pull_number = os.environ.get("PR_NUMBER")

MERGE_PR = os.environ.get("MERGE_PR")
CLOSE_PR = os.environ.get("CLOSE_PR")
PR_DESCRIPTION = os.environ.get("PR_DESCRIPTION")
BASE = os.environ.get("BASE_REF")
HEAD = os.environ.get("HEAD_REF")
print(BASE)
print(HEAD)

# BASE_URI="https://api.github.com"
# owner="naveen-k-u-n"
# repo="naveen-k-u-n/workflow-py"
# pull_number = 5
# MERGE_PR = false
# CLOSE_PR = false
# BASE = true
# HEAD = false
# PR_DESCRIPTION = false

def merge():
    print("PR has Approved.")
    # merge API
    url = BASE_URI+"/repos/" + repo + "/pulls/" + str(pull_number) + "/merge"
    data = json.dumps({"merged": True})
    headers = {'Authorization': 'token '+token}
    res = requests.put(url, data, headers=headers)
    print(f"merge API status code: {res}")

    #  merge API comment
    url = BASE_URI+"/repos/" + repo + "/issues/" + str(pull_number) + "/comments"
    data = json.dumps({"body": "Pull Request Merged!"})
    res = requests.post(url, data, headers=headers)
    print(f"merge API comment status code: {res}")


def close():
    print("PR has Closed manually by comments.")
    # closed API
    url = BASE_URI + "/repos/" + repo + "/pulls/" + str(pull_number)
    data = json.dumps({ "state": "closed" })
    headers = {'Authorization': 'token ' + token}
    res = requests.patch(url, data, headers=headers)
    print(f"Close API status code: {res}")

    # closed API comment
    url = BASE_URI + "/repos/" + repo + "/issues/" + str(pull_number) + "/comments"
    data = json.dumps({"body":"Pull Request Closed!"})
    res = requests.post(url, data, headers=headers)
    print(f"close API comment status code: {res}")

def target():
    url = BASE_URI + "/repos/" + repo + "/pulls/" + str(pull_number)
    data = json.dumps({"state": "closed"})
    headers = {'Authorization': 'token ' + token}
    res = requests.patch(url, data, headers=headers)
    print(f"target API status code: {res}")

    url = BASE_URI + "/repos/" + repo + "/issues/" + str(pull_number) + "/comments"
    data = json.dumps({"body": "Do not accept PR target from feature branch to master branch."})
    res = requests.post(url, data, headers=headers)
    print(f"target API comment status code: {res}")


def description():
    url = BASE_URI + "/repos/" + repo + "/pulls/" + str(pull_number)
    data = json.dumps({"state": "closed"})
    headers = {'Authorization': 'token ' + token}
    res = requests.patch(url, data, headers=headers)
    print(f"description API status code: {res}")

    url = BASE_URI + "/repos/" + repo + "/issues/" + str(pull_number) + "/comments"
    data = json.dumps({"body": "No Description on PR body. Please add valid description."})
    res = requests.post(url, data, headers=headers)
    print(f"description API comment status code: {res}")


if __name__ == '__main__':
    print('start')
    if MERGE_PR.__eq__('true'):
        merge()
    else:
        print('false merge pr')    
    if CLOSE_PR.__eq__('true'):
        close()
    else:
        print('false close pr')    
    if BASE.__eq__('true') and  HEAD.__eq__('false'):
        target()
    else:
        print("target is fine")    
    if PR_DESCRIPTION.__eq__('true'):
        description()
    else:
        print("pr description false")    
    print('end')