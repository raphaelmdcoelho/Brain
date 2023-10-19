### Working Directory

* This tree is in sync with filesystem.
* Represents the immediate changes.
* `git status` displays the current status of the working directory.
* `git checkout -- ...` is used to discharge changes in the working directory.

### Staging Index

* Thisbtree tracks the working directory changes, that have been promoted with `git add`.
* It stores the changes to the next commit.
* This tree is a internal complex cache mechanism.
* To see the state of staging index is possible ti use the following command: `git ls-files [-s | --stage]`.
* `git reset HEAD ...` can be used to upstage a file.

### Commit history

* `git commit` add changes to the permanent snapshot that lives in the Commit History.
* `git log` displays the Commit History.

#git