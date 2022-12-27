from github import Github


g = Github(access_token)

repo_name = 'naveen-k-u-n/workflow-py'
PR_NUMBER=6

repo = g.get_repo(repo_name)
pr = repo.get_pull(PR_NUMBER)

# Add comments on PR
pr.create_issue_comment('testing for merge')

# Close PR
pr.edit(state='closed')

# Merge PR
pr.merge(merge_method = 'merge', commit_message ='Pull Request Approved and Merged!')

print(repo)
print(pr)