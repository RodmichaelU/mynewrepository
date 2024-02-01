from github import Github

# or using an access token
g = Github("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")
repo = g.get_repo("adriannejulie/mynewrepository")

main_branch = repo.get_branch('main')

## Complete your tasks from here

# Get all branches you have created for your public repo
print("\nAll branches: ")
branches = list(repo.get_branches())
for branch in branches:
    print(branch.name)

# Get all pull requests you have created
print("\nPull requests:")
#pulls = repo.get_pulls(state='open', sort='created', base='master')
for pr in repo.get_pulls('all'):
    print(pr)

#Get a list of commits you have created in your main branch
commits = repo.get_commits(sha=main_branch.commit.sha)
print("\nAll Commits:")
for commit in commits:
    print(f"Commit SHA: {commit.sha}")
    print(f"Author: {commit.commit.author.name}")
    print(f"Date: {commit.commit.author.date}")
    print(f"Message: {commit.commit.message}")
    print("------------------------")
