import os
from github import Github
from datetime import datetime, timedelta

g = Github(os.environ["GITHUB_TOKEN"])
repo_name = os.environ.get("REPO_NAME")
pr_number = int(os.environ.get("PR_NUMBER"))

repo = g.get_repo(repo_name)
pr = repo.get_pull(pr_number)
pulls = repo.get_pulls(state='open')
stale_days: int(os.environ.get("STALE_DAYS"))
stale_close_days: int(os.environ.get("STALE_CLOSE_DAYS"))

print("repo_name:",repo)
print("pr_number:",pr.number)
print("pulls:",pulls)
print("stale_days:",stale_days)
print("stale_close_days:",stale_close_days)


# define the number of days after which a pull request is considered stale
stale_no_days = stale_days
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
stale_no_close_days = stale_close_days

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
