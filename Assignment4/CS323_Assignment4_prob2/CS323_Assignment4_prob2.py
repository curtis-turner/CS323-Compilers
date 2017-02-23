#CS323 Assignment 4 Problem 2
def cleanUp(data):
    out = open('newdata.txt', 'a')
    for i in range(len(data)):
        #print(data[i])
        if data[i] == '/' and data[i+1] == '/':
            print('we got to this if state')
            break
        else:
            out.write(str(data[i]))
            
##        elif data[i] in special:
##            output.write(' ' + data[i] + ' ')
##        elif data[i] in reservedWords:
            

               
def main():
    fileData = []
    inFile = open('data.txt', 'r')
    while True:
        l = inFile.readline()
        fileData.append(l)
        if('' == l):
            print('File Finished')
            break
        
    print(fileData)
    if '\n' in fileData:
        fileData.remove('\n')
        
    print(fileData)
    
    for i in fileData:
        cleanUp(i)

if __name__ == '__main__':
    main()


##reservedWords = {"cout<<", "for", "int", "while"}
##special = {'=', '*', '-', ';', '(', ')', "<=", '+'}
##identifierWords = []
##counter=0
##statement = raw_input("Enter a statement: ")
##splitStatement = statement.split(' ')
##
##for i in splitStatement:
##	if i in special:
##		print(i + "\t\tspecial symbol")
##	elif i in reservedWords:
##		print(i + "\t\treserved word")
##		if i == "int":
##			counter = counter+1
##	# elif isinstance(int(i), (int, long, float, complex)):
##	# 	print(i + "\tnumber")
##	elif counter == 1:
##		print(i + "\tidentifier")
##		identifierWords.append(i)
##		counter = counter - 1
##	elif i in identifierWords:
##		print(i + "\t\tidentifier")
##	else:
##		try:
##			if isinstance(int(i), (int, long, float, complex)):
##				print(i + "\t\tnumber")
##		except:
##			print(i + "\t\tnot identifier")

