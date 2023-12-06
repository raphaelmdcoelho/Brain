***spyOn*** 

Creates a mock function similar to `jest.fn` but also tracks calls to `object[methodName]`. Returns a Jest `mock function`.

```javascript
const video = {  
	play() {  
		return true;  
	},  
};  
  
module.exports = video;
```

```javascript
const video = require('./video');  
  
afterEach(() => {  
// restore the spy created with spyOn  
	jest.restoreAllMocks();  
});  
  
test('plays video', () => {  
	const spy = jest.spyOn(video, 'play');  
	const isPlaying = video.play();
  
	expect(spy).toHaveBeenCalled();  
	expect(isPlaying).toBe(true);  
});
```

#Javascript #test #jest.