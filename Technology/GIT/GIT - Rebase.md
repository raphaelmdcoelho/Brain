### Concepts

Rebasing is the process of moving or combining a sequence of commits to a new base commit. Rebasing is most useful and easily visualized in the context of a feature branching workflow.

![[Pasted image 20231007215906.png]]

Rebase itself has 2 main modes: <mark>"manual"</mark> and <mark>"interactive"</mark>.

The primary reason for rebasing is to maintain a linear project history.

You should <mark>NEVER</mark> rebase commits once they've been pushed to a public repository.

### Iteractive

```bash
git rebase -i HEAD~3
```

#git 