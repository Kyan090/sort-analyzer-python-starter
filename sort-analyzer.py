# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")




# Bubble Sort
def bubbleSort(anArray):
    indexLength = len(anArray) - 1
    sorted = False


    while sorted == False:
        sorted = True
        for i in range (0, indexLength):
            if anArray[i] > anArray[i+1]:
                sorted = False
                anArray[i], anArray[i+1] = anArray[i+1], anArray[i]
    return anArray



# selection sort
def selectiobnSort(anArray):


    for i in range(0, len(anArray) -1) :
        minValue = i


        for x in range(i+1, len(anArray)):
            if anArray[x] < anArray[minValue]:
                minValue = x


        if minValue != i:
            anArray[minValue], anArray[i] = anArray[i], anArray[minValue]
   
    return anArray





# insertion Sort
def insertionSort(anArray):


    for i in range(0, len(anArray) ):
        insertPos = anArray[i]


        while anArray[i - 1] > insertPos and i > 0:
            anArray[i], anArray[i -1] = anArray[i -1], anArray[i]
            i = i -1
   
    return anArray



# Bubble Sort Times

startTime = time.time()
bubbleSort(randomData)
endTime = time.time()
totalTime = endTime - startTime
print("Bubble sort Random Data: %s seconds" %totalTime  )


startTime = time.time()
bubbleSort(reversedData)
endTime = time.time()
totalTime = endTime - startTime
print("Bubble sort Reversed Data: %s seconds" %totalTime  )


startTime = time.time()
bubbleSort(nearlySortedData)
endTime = time.time()
totalTime = endTime - startTime
print("Bubble sort Nearly Sorted Data: %s seconds" %totalTime  )


startTime = time.time()
bubbleSort(fewUniqueData)
endTime = time.time()
totalTime = endTime - startTime
print("Bubble sort Few Unique Data: %s seconds" %totalTime  )



# Selection Sort Time 

startTime = time.time()
selectiobnSort(randomData)
endTime = time.time()
totalTime = endTime - startTime
print("Selection Sort Random Data: %s seconds" %totalTime  )


startTime = time.time()
selectiobnSort(reversedData)
endTime = time.time()
totalTime = endTime - startTime
print("Selection Sort Reversed Data: %s seconds" %totalTime  )


startTime = time.time()
selectiobnSort(nearlySortedData)
endTime = time.time()
totalTime = endTime - startTime
print("Selection Sort Nearly Sorted Data: %s seconds" %totalTime  )


startTime = time.time()
selectiobnSort(fewUniqueData)
endTime = time.time()
totalTime = endTime - startTime
print("Selection Sort Few Unique Data: %s seconds" %totalTime  )


# Insertion Sort Time 

startTime = time.time()
insertionSort(randomData)
endTime = time.time()
totalTime = endTime - startTime
print("Insertion Sort Random Data: %s seconds" %totalTime  )


startTime = time.time()
insertionSort(reversedData)
endTime = time.time()
totalTime = endTime - startTime
print("Insertion Sort Reversed Data: %s seconds" %totalTime  )


startTime = time.time()
insertionSort(nearlySortedData)
endTime = time.time()
totalTime = endTime - startTime
print("Insertion Sort Nearly Sorted Data: %s seconds" %totalTime  )


startTime = time.time()
insertionSort(fewUniqueData)
endTime = time.time()
totalTime = endTime - startTime
print("Insertion Sort Few Unique Data: %s seconds" %totalTime  )