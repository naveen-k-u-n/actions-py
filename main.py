import os
from github import Github
from datetime import datetime, timedelta

# env values
g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo(os.environ['REPO_NAME'])
pulls = repo.get_pulls(state='open')
MERGE_PR = os.environ.get("MERGE_PR")
CLOSE_PR = os.environ.get("CLOSE_PR")

print("repo:",repo)
print("pulls:",pulls)

# 1.Check if there are any open pull requests
if pulls.totalCount == 0:
    print('No open pull requests, exiting...')
    exit()

# 2.Add "Stale" label to the PR if no active from 15 days
stale_days = 15
now = datetime.now()
for pr in pulls:
    try:
        time_diff = now - pr.updated_at
        # check if the time difference is greater than the stale_days
        if time_diff > timedelta(days=stale_days):
            print("Pull request", pr.number, "is stale!")
            pr.create_issue_comment('This PR is stale because it has been open 15 days with no activity. Remove stale label or comment/update PR otherwise this will be closed in next 2 days.')
            pr.add_to_labels('Stale')
    except Exception as e:
        print('Error occurred while processing pull request:', pr.number)
        print('Error:', e)

# 3.close staled PR if 2 days of no activity
stale_close_days = 2
for pr in pulls:
    # check if the Stale label is applied on PR
    if "Stale" in [label.name for label in pr.labels]:
        try:
            time_diff = now - pr.updated_at
            # check if the time difference is greater than the stale_close_days
            if time_diff > timedelta(days=stale_close_days):
                print("Pull request", pr.number, "is stale and closed!")
                pr.edit(state="closed")
                pr.create_issue_comment('This PR was closed because it has been stalled for 2 days with no activity.')
        except Exception as e:
            print('Error occurred while closing pull request:', pr.number)
            print('Error:', e)

print("pr_updated_at:",pr.updated_at)

# 4.Check if the pull request targets the master branch directly
for pull in pulls:
    if pull.base.ref == 'master' and not pull.head.ref.startswith('release/'):
        try:
            pull.edit(state='closed')
            pull.create_issue_comment('Do not accept PR target from feature branch to master branch.')
            print("Pull request", pull.number, "Do not accept PR target from feature branch to master branch.")
        except Exception as e:
            print('Error occurred while processing pull request:', pull.number)
            print('Error:', e)

# 5.Check if the pull request has a description
for pull in pulls:
    if not pull.body:
        try:
            pull.edit(state='closed')
            pull.create_issue_comment('No Description on PR body. Please add valid description.')
            print("Pull request", pull.number, "No Description on PR body. Please add valid description.")
        except Exception as e:
            print('Error occurred while processing pull request:', pull.number)
            print('Error:', e)

# 6.Check if the Approved or Close comments in the pull request comments
def merge():
    if 'PR_NUMBER' in os.environ:
        pr_number = int(os.environ['PR_NUMBER'])
        pr = repo.get_pull(pr_number)
        print("pr_number:", pr_number)
        print("pr:", pr)
        try:
            pr.create_issue_comment('This pull request was approved and merged because of a slash command.')
            pr.merge(merge_method = 'merge', commit_message ='Pull Request Approved and Merged!')
            print("Pull request:", pr, "was approved and merged because of a slash command.")
        except Exception as e:
            print(f"Failed to merge PR: {str(e)}")
            exit()

def close():
    if 'PR_NUMBER' in os.environ:
        pr_number = int(os.environ['PR_NUMBER'])
        pr = repo.get_pull(pr_number)
        print("pr_number:", pr_number)
        print("pr:", pr)
        try:
            pr.edit(state="closed")
            pr.create_issue_comment('This pull request was closed because of a slash command.')
            print("Pull request:", pr, "was closed because of a slash command.")
        except Exception as e:
            print(f"Failed to close PR: {str(e)}")

if __name__ == '__main__':
    print('start')
    if MERGE_PR.__eq__('true'):
        merge()  
    if CLOSE_PR.__eq__('true'):
        close()   
    print('end')      