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

### Main Options

The default invocation of git reset has implicit arguments of --mixed and HEAD. This means executing `git reset` is equivalent to executing `git reset --mixed HEAD`. In this form **HEAD** is the specified commit. Instead of HEAD any Git SHA-1 commit hash can be used.

![[03 (8).svg]]
### --hard

This is the most direct, <mark>DANGEROUS</mark>, and frequently used option. When passed `--hard` the [[Commit history]] ref pointers are updated to the specified commit. Then, the [[Staging Index]] and [[Working Directory]] are reset to match that of the specified commit. Any previously pending changes to the Staging Index and the Working Directory gets reset to match the state of the Commit Tree. This means any pending work that was hanging out in the Staging Index and Working Directory will be lost.

### --mixed

This is the default operating mode. The ref pointers are updated. The [[Staging Index]] is reset to the state of the specified commit. Any changes that have been undone from the Staging Index are moved to the [[Working Directory]].

#git 