import os
from github import Github
from datetime import datetime, timedelta

# get the pull request number and repository name
#pr_number = os.environ["PR_NUMBER"]
pull_number = int(os.environ.get("PR_NUMBER"))
repo_name = os.environ["GITHUB_REPOSITORY"]

# create a PyGithub instance using the GitHub token
g = Github(os.environ["GITHUB_TOKEN"])

# get the pull request object
repo = g.get_repo(repo_name)
pr = repo.get_pull(pull_number)

#access_token = os.environ.get("GITHUB_TOKEN")
#g = Github(access_token)
#repo_name = os.environ.get("REPO_NAME")
#pull_number = int(os.environ.get("PR_NUMBER"))

#g = Github(os.environ["GITHUB_TOKEN"])
#repo = os.environ.get("REPO_NAME")
pulls = repo.get_pulls(state='open')

print("repo_name:",repo)
print("pulls:",pulls)

# define the number of days after which a pull request is considered stale
stale_days = 15
# get the current date
now = datetime.now()
# iterate over the pull requests
for pr in pulls:
    # calculate the time difference between the last update of the pull request and the current date
    time_diff = now - pr.updated_at
    # check if the time difference is greater than the stale days
    if time_diff > timedelta(days=stale_days):
        print("Pull request", pr.number, "is stale!")
        pr.create_issue_comment('This PR is stale because it has been open 15 days with no activity. Remove stale label or comment or this will be closed in 2 days.')
        pr.add_to_labels('Stale')

# iterate over each pull request
stale_close_days = 1

for pr in pulls:
    # check if the stale label is applied
    if "Stale" in [label.name for label in pr.labels]:
        # calculate the time difference between the last update of the pull request and the current date
        time_diff = now - pr.updated_at
        # check if the time difference is greater than the stale days
        if time_diff > timedelta(days=stale_close_days):
            print("Pull request", pr.number, "is stale and closed!")
            # close the pull request
            pr.edit(state="closed")
            pr.create_issue_comment('This PR was closed because it has been stalled for 2 days with no activity.')

print("pr_updated_at:",pr.updated_at)
print("pr_labels:",pr.labels)
