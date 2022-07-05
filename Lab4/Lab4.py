def microwave(time):

    #Gets the user input and stores the minutes and seconds as variables.
    minutes = int(time[:time.find(':')])
    seconds = int(time[time.find(':') + 1:])
    new_minutes = minutes

    #As long as there are minutes remaining the program will continue to print
    #the count down. If it is the first minute then the seconds will start at
    #the user input. #If not then the program will count down from 59.
    while minutes >= 0:
        if new_minutes != minutes:
            timer = 59
            while timer >= 0:
                print('{}:{:02d}'.format(minutes, timer))
                timer = timer - 1
        else:
            timer = seconds
            while timer >= 0:
                print('{}:{:02d}'.format(minutes, timer))
                timer = timer - 1
        minutes = minutes - 1

def phonebook(phonebook):

    for i in phonebook:

        phone_number = i[1]
        area_code = phone_number[:3]
        favorites = i[2][0]

        if area_code == "214" and favorites:
            print(i)

def twelveA():
    
    list = [10,9,8,7]
    for i in range(len(list)):
        print(f"Index: {i} Value: {list[i]}")

def twelveB(word):
    length = len(word)
    for index in range(length // 2):
        if word[index] != word[length - index - 1]:
            return False
    
    return True

def twelveC():
    listA = [10, 45, 123, 1200]
    listB = [43, 124, 125321, 2, 54]
    listC = [10]
    listD = [10, 22]

    if len(listA) == 1:
        return True
    else:
        for i in range(1,len(listB)):
            if listB[i] <= listB[i-1]:
                return False
    
    return True

def twelveD():

    list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    for i in range(len(list)):
        if i % 2 == 0:
            print(list[i])

def twelveE():
    duplicates = []
    values = [4, 1, 7, 3, 1, 61, 1, 9, 0, 4]
    removed_dupes = []
    for item in values:
        if item not in duplicates:
            removed_dupes.append(item)
            duplicates.append(item)
    
    return removed_dupes

def main():

    microwave("12:59")
    pb = [["ashley", "214-141-1421", [True, False]] , ["john", "821-212-1245", [False, False]], ["darius", "214-212-1245", [False, False]]]
    phonebook(pb)

    a = twelveA()
    b = twelveB()
    c = twelveC()
    d = twelveD()
    e = twelveE()

if __name__ == "__main__":
    main()