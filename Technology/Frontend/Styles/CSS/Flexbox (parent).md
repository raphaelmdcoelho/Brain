## Flex container

![[Pasted image 20231104142437.png]]

* **display**
	This defines a flex container;
	inline or block depending on the given value. It enables a flex context for all its direct children.

```css
.container {
	display: flex; /* or inline-flex */
}
```

* **flex-direction**
	This establishes the min-axis, thus defining the direction flex items are placed in the flex container. Flexbox is (aside from optional wrapping) a single-direction layout concept. Think of flex items as primarily laying out either in horizontal rows or vertical columns.

![[Pasted image 20231104142755.png]]

```css
.container {
	flex-direction: row | row-reverse | column | column-reverse;
}
```

- `row` (default): left to right in `ltr`; right to left in `rtl`
- `row-reverse`: right to left in `ltr`; left to right in `rtl`
- `column`: same as `row` but top to bottom
- `column-reverse`: same as `row-reverse` but bottom to top

* **flex-wrap**

![[Pasted image 20231104144655.png]]

By default, flex items will all try to fit onto one line. You can change that and allow the items to wrap as needed with this property.

```css
.container {
	flex-wrap: nowrap | wrap | wrap-reverse;
}
```

- `nowrap` (default): all flex items will be on one line
- `wrap`: flex items will wrap onto multiple lines, from top to bottom.
- `wrap-reverse`: flex items will wrap onto multiple lines from bottom to top.

* **flex-flow**

This is a shorthand for the `flex-direction` and `flex-wrap` properties, which together define the flex container's main and cross axes. The default value is row nowrap.

```css
.container {
	flex-flow: column wrap;
}
```

* **justify-content**

![[Pasted image 20231104145240.png]]

#frontend #style 