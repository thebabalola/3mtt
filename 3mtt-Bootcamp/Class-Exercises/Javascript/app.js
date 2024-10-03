//alert('Hey look up')  //Pop up for notfications or errors (to appear on your web page)

console.log('i dey like disturbance');

var names = 'Babalola T';
let occupation = 'Programmer';
const stacks = 'full stack';

console.log(names + ' is a ' + stacks + ' ' + occupation);



function jsfunc(){
	var names = 'Babalola K';
	let occupation = 'Administrator';
	const stacks = 'Salesforce';

	console.log(names + ' is a ' + stacks + ' ' + occupation);
}

jsfunc();



function cal() {
	let numb1 = 22;
	let numb2 = 3;
	let result = numb1 + numb2;

	return result;
}

console.log(cal());



function myCal(num1, num2) {
	let result = num1 + num2;

	return result;
}

console.log(myCal(2, 5));



function getProvision() {
	let mumsChoice = 'Jago';

	if (mumsChoice == 'Jago'){
		return 'Kindly buy Jago';
	}
	else if (mumsChoice == 'Dano'){
		return 'you can get Dano too';
	}
	else {
		return 'come back without buying';
	}
}

console.log(getProvision())



function getGroceries(grocery, buyer, quan1, quan2) {

	let quantity = myCal(quan1, quan2); //calls the cal func into the getGroceries func

	if (grocery == 'beans'){
		return buyer + ' we have beans in store';
	}
	else if (grocery == 'rice'){
		return buyer + ' i really dont need rice too';
	}
	else if (grocery == 'garri'){
		return buyer + ' Garri is very much needed' + ', buy ' + quantity + ' congo';
	}
	else {
		return 'come back without buying';
	}
}
let errandsBoy = 'Akin'
let neededGrocery = 'garri';
console.log(getGroceries(neededGrocery, errandsBoy, 3, 4));
document.write(getGroceries(neededGrocery, errandsBoy, 3, 4)); // shows this on the html webpage



function testArray() {
	const myColors = ['Red', 'Green', 'Yellow', 'Grey', 'Blue', 'White', 'Indigo'];

	for (let color of myColors){
		console.log(`i need this' ${color}`);
	}

	// return colors
}



function testArray() {
	const myColors = ['Red', 'Green', 'Yellow', 'Grey', 'Blue', 'White', 'Indigo'];

	// Correcting 'Colors' to 'myColors'
	for (let color of myColors) {
		console.log(`I need this ${color}`); //outputs all the colors
	}

	for (i = 3; i < myColors.length; i++){
		console.log(myColors[i])  //outputs the elements of the color Array from above index 3
	}
	return myColors
}

testArray()