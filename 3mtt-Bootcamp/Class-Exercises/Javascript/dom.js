const myText = document.getElementById('text');

myText.addEventListener('click', alertNote);
myText.innerHTML = 'i changed Text';		//changes text
myText.style.color = 'red';		//changes text color
myText.style.backgroundColor = 'grey';		//changes background to grey

let myBtn;
myBtn = document.getElementById('btn');

myBtn.style.backgroundColor = 'orange';
myBtn.style.color = 'white';

function alertNote() {
	alert('i am a DOM Text');
}

/*
 ----- DOM Manipulation Explanation  ----------
DOM manipulation involves using JavaScript to interact with, modify, or respond to elements and events in the HTML document. This can include:
	- Selecting elements
	- Changing content (text, HTML)
	- Modifying attributes (like classes or IDs)
	- Adding or removing elements
	- Responding to user input (like clicks or keypresses)
	- Changing styles dynamically

In your code:
	- You are selecting an element.
	- You are adding behavior (an event listener).
	- You are responding to user interaction (a click event).

Thus, this is a valid example of DOM manipulation!


 ----- Virtual DOM -------
	- The virtual DOM is an abstraction or lightweight copy of the real DOM, 
	often used in libraries or frameworks like React. Changes are first made to the virtual DOM, 
	and only the differences (or diffs) between the virtual and real DOM are applied to the actual DOM. 
	This makes updates more efficient, as the virtual DOM minimizes costly real DOM updates.
	- The virtual DOM itself is never displayed; it is used to optimize performance by reducing 
	the number of direct interactions with the real DOM.

Example: of manipu;ation in the virtual DOM, using react
	function MyComponent() {
  return (
    <div id="text" onClick={() => alert('I am a big Text')}>
      Click me!
    </div>
  );
}

*/