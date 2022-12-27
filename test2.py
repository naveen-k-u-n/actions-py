from github import Github


g = Github(access_token)

repo_name = 'naveen-k-u-n/workflow-py'
pull_number = 7

repo = g.get_repo(repo_name)
pr = repo.get_pull(pull_number)

# Add comments on PR
pr.create_issue_comment('testing2')

# Close PR
# pr.edit(state='closed')

# Merge PR
# pr.merge(merge_method = 'merge', commit_message ='Pull Request Approved and Merged!')

print(repo)
print(pr)