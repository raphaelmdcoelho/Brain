```html
<body>
	<div class="parent">
		Parent
		<div class="child-one child">One</div>
		<div class="child-two child">Two</div>
		<div class="child-three child">Three</div>
	</div>
</body>
```

```css
.parent {

}

.child-one {

}

.child-two {

}

.child-three {

}
```

![[Pasted image 20231104140215.png]]

```css
.child-one {
	position: relative;
}
```

![[Pasted image 20231104140215.png]]

It remains the same, because the relative position acts the same way as static position, but now you can apply the properties Top, Left, Right and Bottom

```css
.child-one {
	position: relative;
	left: 10px;
}
```

![[Pasted image 20231104140508.png]]

```css
.child-one {
	position: absolute;
}
```

![[Pasted image 20231104140731.png]]

position `absolute` removes the element from document flow.

```css
.child-one {
	position: absolute;
	top: 10px;
}
```

![[Pasted image 20231104140928.png]]

Now it is 10 pixels bellow the top of browser windows.

```css
.parent {
	position: relative;
}

.child-one {
	position: absolute;
	top: 10px;
}
```

![[Pasted image 20231104141246.png]]

As we can see here, the absolute positions will be relative to some, if doesn't exist a element with position relative, the position will be from the window. Setting the parent element to have position relative (this is the most useful use of relative position), now the child-one element will be relative to the parent. (parent can assume different position like absolute to this work).

```css
.parent {
	position: relative;
}

.child-one {
	position: fixed;
	top: 0px;
}
```

![[Pasted image 20231104141656.png]]

```css
.parent {
	position: relative;
}

.child-one {
	position: sticky;
	top: 0px;
}
```

Here, nothing special occurs, but scrolling down the page, when hitting the top of window, the child-one element will be sticky to the screen and will not be vanished.

#frontend #style 