There are cases where you might want to override the styles of child components or elements that are not directly part of the component's template. That's where `::ng-deep` comes into play. It allows you to pierce through the view encapsulation boundary and style child components or elements that are otherwise encapsulated.

```css
::ng-deep .some-class { /* styles that will affect .some-class inside child components */ }
```

#frontend #style 