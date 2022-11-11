"""
https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as a ``Map<String,List>with two key-value pairs:"pos"and"peaks". If there is no peak in the given array, simply return {"pos" => [], "peaks" => []}`.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

Have fun!
"""

def get_plateaus(arr):
    
    #parse for plateau
    plateaus = []
    plateausIndexArray = []
    inPlateau = False
    for pos, value in enumerate(arr):

        #Add if actually in plateau
        if(inPlateau):
            plateausIndexArray.append(pos)
        
        #Avoid out of bounds
        if(pos < len(arr)-1 ): 
            nextValue = arr[pos+1]
        else:
            nextValue = None

        #Check if in plateau
        if (value == nextValue):
            if (not inPlateau):
                #Get beggining of plateau
                plateausIndexArray.append(pos)
                inPlateau = True
                  
        elif(inPlateau):
            plateaus.append({"value": value ,"indexes":plateausIndexArray})
            plateausIndexArray = []
            inPlateau = False
        
        #If last index and still in plateau
        if(pos == len(arr)-1 and inPlateau):
            plateaus.append({"value": value ,"indexes":plateausIndexArray})
            plateausIndexArray = []
    return plateaus

def is_value_greatest_between(value, valueBefore, valueAfter):
    if( valueAfter is not None and valueBefore is not None ):
    #If the value is greater than both right and left values
        if(value > valueBefore and value > valueAfter):
            return True
    
    return False


def pick_peaks(arr):
    print("Picking peaks for\n",arr)
    assert isinstance(arr, list)
    posList   = []
    peaksList = []
    #Get indexes to filter out of plateaus from array
    plateaus = get_plateaus(arr)
    print("Plateaus gotten from array", [plateau["indexes"] for plateau in plateaus])
    #Get peaks
    posI = 0
    while posI < len(arr):
        #Initialization
        value = arr[posI]
        valueBefore = None
        valueAfter = None

        #Avoid assigning valueBefore if arr[posI-1] == -1
        if(posI > 0):
            valueBefore = arr[posI-1]

        #Avoid assigning valueAfter if arr[posI+1] > array length
        if(not posI >= len(arr)-1 ):
            valueAfter = arr[posI+1]
        
        #P lateaus 
        breakFromPlateauCheck = False
        for plateau in plateaus:
            plateau = plateau["indexes"]
            if(posI == plateau[0]):

                #Il veut la position du premier nombre du plateau
                #Gets value after the plateau for comparison
                if(posI + len(plateau) > len(arr)-1):
                    breakFromPlateauCheck= True
                    posI += len(plateau)-1
                    break
                valueAfter = arr[posI + len(plateau)]
        
                if(is_value_greatest_between(value,valueBefore,valueAfter)):
                    peaksList.append(value)
                    posList.append(posI)
                    breakFromPlateauCheck = True
                    posI += len(plateau)-1
                    break
                posI += len(plateau)-1
        if breakFromPlateauCheck:
            continue
   

        if(is_value_greatest_between(value,valueBefore,valueAfter)):
            peaksList.append(value)
            posList.append(posI)

        
        posI +=1
    posI += 1
    return {"pos": posList, "peaks": peaksList}
tests = [1,2,3,6,4,1,2,3,2,1] ,[3,2,3,6,4,1,2,3,2,1,2,3],[3,2,3,6,4,1,2,3,2,1,2,2,2,1],[2,1,3,1,2,2,2,2,1],[2,1,3,1,2,2,2,2],[2,1,3,2,2,2,2,5,6],[2,1,3,2,2,2,2,1],[1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3],[18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7],[],[1,1,1,1]
#tests = [2,1,3,1,2,2,2,2,1], []
results ={"pos":[3,7], "peaks":[6,3]},{"pos":[3,7], "peaks":[6,3]},{"pos":[3,7,10], "peaks":[6,3,2]},{"pos":[2,4], "peaks":[3,2]},{"pos":[2], "peaks":[3]},{"pos":[2], "peaks":[3]},{"pos":[2], "peaks":[3]},{"pos":[2,7,14,20], "peaks":[5,6,5,5]},{'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]},{"pos":[],"peaks":[]},{"pos":[],"peaks":[]}
#results ={"pos":[2,4], "peaks":[3,2]}, {"pos":[], "peaks":[]}
 
for i,test in enumerate(tests):
    print("================================")
    print(i)
    print("length:",len(test))
    print(pick_peaks(test))
    print(results[i])


