#!/bin/sh
# $ sh git-author-rewrite.sh
# $ git push --force --tags origin 'refs/heads/*'
git filter-branch --env-filter '

OLD_EMAIL="old@domain.tld"
CORRECT_NAME="My Name"
CORRECT_EMAIL="new@domain.tld"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
