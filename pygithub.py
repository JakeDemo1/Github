from github import Github
import os
from pprint import pprint
import requests 
import json

# script that loops over repos and their branches to protect or not protect
access_token = ITSASECRET
at = Github(access_token)
for repo in at.get_user().get_repos():
    for branch in repo.get_branches():
        b = repo.get_branch(branch.name)
        if b.protected:
            print(b.name, "protected") 
        else:
            print(b.name, "now being protected")
            b.edit_protection(required_approving_review_count=1, enforce_admins=True, require_code_owner_reviews=True)
            repo.open_issues(assignee="moss203", body="added protection", title="protection",)


