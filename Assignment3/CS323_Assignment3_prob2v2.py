#CS323 Assignment3p2
#Authors: Curtis Turner, Billy Giang

def accepted(word):
    state = 'S'
    count = 0
    while(count < len(word)):
        for i in word:
            if state == 'S':
                if i == 'a':
                    state = 'A'
                    count += 1
                elif i == 'b':
                    state = 'B'
                    count += 1
                else:
                    return False

            if state == 'A':
                if i == 'a':
                    state = 'A'
                    count += 1
                elif i == 'b':
                    state = 'X'
                    count += 1
                else:
                    return False

            if state == 'B':
                if i == 'b':
                    state = 'B'
                    count += 1
                elif i == '$':
                    return True
                else:
                    return False
            
    if state == 'X' or state == 'B':
        return True

def main():
    file = open('data.txt', 'r')
    choice = True
    while(choice):
        userWord = file.readline()
        if userWord == '':
            choice = False
        userWord = userWord.strip('\n')
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
    
