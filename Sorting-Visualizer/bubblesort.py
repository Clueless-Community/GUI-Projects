import time

max_time = 0.250
# compares neighbouring elements in the array
def bubbleSort(arr,displayArray,speedInput,pauseBool):

    swapCount = 0
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr)-1):
           
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapCount+=1
                colorArray = ['blue' if x==j or x==j+1 else 'red' for x in range(len(arr))]
                for clr in range(1,i+1):
                    colorArray[-clr] = 'green'

                displayArray(arr,colorArray,swapCount)
                time.sleep(max_time - (speedInput*max_time/100))
                swapped = True

        if swapped == False:
            break

    colorArray = ['green' for i in range(len(arr))]
    displayArray(arr,colorArray,swapCount)
    print("Sorted arr : ",arr)
