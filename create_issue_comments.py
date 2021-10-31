import argparse
import os

import frontmatter
from github import Github

def get_args():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("repo",
                        help="The repository to act on")
    parser.add_argument("token",
                        help="The GitHub Access token")
    parser.add_argument("paths", nargs="+",
                        help="Paths to look for files that need comments")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    github = Github(args.token)

    repo = github.get_repo(args.repo)
    label = repo.get_label("Comments")

    for path in args.paths:
        for file_name in os.listdir(path):
            if file_name.endswith(".md"):
                file_path = path.join(path, file)
                if os.path.isfile(file_path):
                    with open(file_path "w") as f:
                        post = frontmatter.load(f)
                        if "comment_id" not in post:
                            issue = repo.create_issue(title="Comment thread for {title}".format(
                                title=post["title"]
                            ), labels=[label])
                            post["comment_id"] = issue.number
                            frontmatter.dump(post, f)
