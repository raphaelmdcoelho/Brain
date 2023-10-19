***git reset*** is a similar command as ***git checkout***.

`git checkout` solely operates on the `HEAD` ref pointer, `git reset` will move the `HEAD` ref pointer and the current branch ref pointer. To better demonstrate this behavior consider the following example:

![[Pasted image 20231017225513.png]]
This example demonstrates a sequence of commits on the `main` branch. The `HEAD` ref and `main` branch ref currently point to commit d. Now let us execute and compare, both `git checkout b` and `git reset b.`

`git checkout b`

![[Pasted image 20231017225728.png]]

With `git checkout`, the `main` ref is still pointing to `d`. The `HEAD` ref has been moved, and now points at commit `b`. The repo is now in a 'detached `HEAD`' state.

`git reset b`

![[Pasted image 20231017225839.png]]
Comparatively, `git reset`, moves both the `HEAD` and branch refs to the specified commit.

In addition to updating the commit ref pointers, `git reset` will modify the state of the three trees. The ref pointer modification always happens and is an update to the third tree, the Commit tree. The command line arguments `--soft, --mixed`, and `--hard` direct how to modify the Staging Index, and Working Directory trees.

#git 