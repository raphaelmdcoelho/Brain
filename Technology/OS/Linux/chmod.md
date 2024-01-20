- chmod stands for "change mode"
- To list the permissions for a file is possible to use the following command:
```bash
ls -l
```

![[Permissions information.png]]
- The first character is the file type:
	- -: file
	- d: directory
	- l: link
- the following 3 other "groups" of 3 characters are the permissions:
	- r: read
	- w: write
	- x: execute
	- -: permission is not granted
	- the first 3 permission characters are related with th file's owner.
	- the following three characters are related with the groups permission.
- the other 3 characters are for other users.

![[Linux permissions.png]]

## Changing permissions


```bash
chmod [who][+,-,=][permissions] filename
```

- The "who" parameter have four options:
	- u (user).
	- g (group)
	- o (others)
	- a (all)
- The next parameter is what you want to do:
	- +: grant permission.
	- -: remove permission.
	- =: copy permission (if I want to set the same permissions from my user to a group a can do like that <mark>g=u</mark>).
- The next one is the permission symbol (r, w, x).
- The next one is the file name.
	- e.g:

```bash
chmod u+r test.txt

chmod u+rwx test.txt
```

#linux #bash 