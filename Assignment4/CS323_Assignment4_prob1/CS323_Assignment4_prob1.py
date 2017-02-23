#CS323 Assignment 4 Problem 1
#Authors: Curtis Turner, Billy Giang+

#CS323 Assignmen 4 Problem 1
#Authors: Curtis Turner, Billy Giang, David Horning

def accepted(word):
    state = 'S'
    count = 0
    while(count < len(word)):
        for i in word:
            if state == 'S':
                if i == 'a':
                    state = 'S'
                    count += 1
                elif i == 'b':
                    state = 'B'
                    count += 1
                elif i == 'c':
                    state = 'C'
                    count += 1
                else:
                    return False

            if state == 'D':
                if i == 'b':
                    state = 'D'
                    count += 1
                elif i == 'a':
                    state = 'B'
                    count += 1
                elif i == 'c':
                    state = 'C'
                    count += 1
                else:
                    return False
                
            if state == 'C':
                if i == 'a':
                    state = 'S'
                    count += 1
                elif i == 'b' or i == 'c':
                    state = 'D'
                    count += 1
                elif i == '$':
                    return True
                else:
                    return False

            if state == 'B':
                if i == 'b':
                    state = 'B'
                    count += 1
                elif i == 'a':
                    state = 'C'
                    count += 1
                elif i == 'c':
                    state = 'D'
                    count += 1
                elif i == '$':
                    return True
                else:
                    return False
            
    if state == 'C' or state == 'B':
        return True

def main():
    file = open('CS323_Assignment4_data.txt', 'r')
    choice = True
    while(choice):
        userWord = file.readline()
        if userWord == '':
            choice = False
        userWord = userWord.strip('\n')
        userWord = userWord + '$'
        print(userWord)
        if accepted(userWord):
            print('accepted')
        else:
            print('Word not accepted')

        cont = input('would you like to continue? enter y or n >> ')
        if cont == 'y' or cont == 'Y':
            choice = True
        elif cont == 'n' or cont == 'N':
            print('Closing program')
            file.close()
            choice = False
        else:
            print('invalid input closing program')
            file.close()
            choice = False

if __name__ == '__main__':
    main()
    
