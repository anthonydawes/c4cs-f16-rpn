#!/usr/bin/env python3

#adawes hw5
#original code: ppannuto

import operator

# define operators
operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}

# define calculate function
def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

# define main and call calculate
def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("Result: ", result)

if __name__ == '__main__':
	main()
