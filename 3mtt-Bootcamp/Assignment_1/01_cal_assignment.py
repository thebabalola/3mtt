# ----- Simple Calculator -----

# Gets user input
num1 = int(input('Enter your first number: '))
operators = input('Enter operation (+, -, *, /, %, **): ')
num2 = int(input('Enter your second number: '))

def cal(numOne, numTwo, oper):
	'''Posibile arthimetic operation to be carried out'''
	if (type(numOne) == int or type(numOne) == float) and (type(numTwo) == int or type(numTwo) == float):
		if oper == '+':
			result = numOne + numTwo
			print(result)
			return result
		elif oper == '-':
			result = numOne - numTwo
			print(result)
			return result
		elif oper == '*':
			result = numOne * numTwo
			print(result)
			return result
		elif oper == '/':
			result = numOne / numTwo
			print(result)
			return result
		elif oper == '%':
			result = numOne % numTwo
			print(result)
			return result
		elif oper == '**':
			result = numOne ** numTwo
			print(result)
			return result
		else:
			return 'operation inavlid'
	
cal(num1, num2, operators)  # Function call
