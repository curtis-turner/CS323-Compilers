# 323 Assignment 3 Programming
# Billy Giang, Curtis Turner
# Feb 14 2017

# Sample output: for ( int tom_jones = 22 ; cout<< 2tom ;

reservedWords = {"cout<<", "for", "int", "while"}
special = {'=', '*', '-', ';', '(', ')', "<=", '+'}
identifierWords = []
counter=0
statement = raw_input("Enter a statement: ")
splitStatement = statement.split(' ')

for i in splitStatement:
	if i in special:
		print(i + "\t\tspecial symbol")
	elif i in reservedWords:
		print(i + "\t\treserved word")
		if i == "int":
			counter = counter+1
	# elif isinstance(int(i), (int, long, float, complex)):
	# 	print(i + "\tnumber")
	elif counter == 1:
		print(i + "\tidentifier")
		identifierWords.append(i)
		counter = counter - 1
	elif i in identifierWords:
		print(i + "\t\tidentifier")
	else:
		try:
			if isinstance(int(i), (int, long, float, complex)):
				print(i + "\t\tnumber")
		except:
			print(i + "\t\tnot identifier")
