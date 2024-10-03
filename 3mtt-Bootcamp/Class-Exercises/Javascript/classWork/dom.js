let myBtn;
myBtn = document.getElementById('btn');

myBtn.addEventListener('click', btnClick);

function btnClick() {
	let quoteArray = [
		'No food for lazy man',
		'Good things don\'t come easy',
		'Once the mind is defeated, the body is'
	];

	// Get a random index
	let randomIndex = Math.floor(Math.random() * quoteArray.length);
	let randomQuote = quoteArray[randomIndex]; // Get the random quote

	// console.log(randomQuote);   - not neccessary

	// Update the innerHTML to the random quote
	let myQuote = document.getElementById('quote');
	myQuote.innerHTML = randomQuote; // Display the random quote
	myQuote.style.color = 'Red';
}

let myBtnAuto;
myBtnAuto = document.getElementById('btnAuto');

myBtn.addEventListener('click', btnClickAuto);

function btnClickAuto(){
	setInterval(function() {
		btnClick();
		
	}, 1000);
}
