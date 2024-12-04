#!/bin/bash

# Check if a commit message is provided
if [ -z "$1" ]; then
  echo "Usage: ./upload.sh <commit-message> [file-or-directory]"
  exit 1
fi

# Set variables
COMMIT_MESSAGE="$1"
FILE_OR_DIRECTORY="${2:-.}" # Default to the current directory if not specified

# Run the Git commands
git add "$FILE_OR_DIRECTORY"
if [ $? -ne 0 ]; then
  echo "Error: Failed to add files."
  exit 1
fi

git commit -m "$COMMIT_MESSAGE"
if [ $? -ne 0 ]; then
  echo "Error: Commit failed."
  exit 1
fi

git push
if [ $? -ne 0 ]; then
  echo "Error: Push failed."
  exit 1
fi

echo "Changes added, committed, and pushed successfully!"
