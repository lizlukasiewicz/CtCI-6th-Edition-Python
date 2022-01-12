"""
# Implement a function which, given an array of numbers, determines which of the numbers is the second smallest
# Assumptions
# For arrays with fewer than two elements, the function should return 0
# For the sake of simplicity, repeated numbers are assumed to be distinct, e.g. secondSmallest( {-1, -1, 2, 3} ) should return -1.

def second_smallest(array):
    # initiate counter variable at zero 
    counter = 0 
    #loop the array and find the min
    for num in array:
        n = len(array)
        while n > 0:
            if num < array[n]:
                minimum = num
                n -= 1
            else: 
                n -= 1
                continue
    
    #while counter < 1:
        #firstmin = min(array)
    # remove the minimum value
        #array.remove(firstmin)
        # add 1 counter
        #counter +=1
    if counter == 1:
    # if counter ==1
        print(min(array))
    #return minimum value 
    
test = [3, 4, 5, 2, 1]
second_smallest(test)
"""

"""
# Problem description
# Given a list of student test scores, find the best average grade.

# Assumptions

# Each student may have more than one test score in the list.

# Each element in the input array is a two-element array of the form [student name, test score], e.g. [ "Bobby", "87" ].

# Test scores may be positive or negative integers.

# If you end up with an average grade that is not an integer, you should use a floor function to return the largest integer less than or equal to the average.

# Return 0 for an empty input.

# Input:  [["Bob","87"], ["Mike", "35"],["Bob", "52"], ["Jason","35"], ["Mike", "55"], ["Jessica", "77"]]
"""
def average_grade(array):
    if len(array) == 0 :
        return 0
    averages=[]
    # loop through the array to find largest average
    hash_table={}
    for person in array:
        if person in hash_table:
            print(person)
        else:
            hash_table[person] = int(person[1])
            averages.append(person)
        
        # if first value if each array is equal to the next
        # i = 0
        # while i < len(array):
        #     average = 0
        #     if grades[0] == :
        #         average +=1
        #         score = average /(array[i].int(grades[1]) + array[i+1].int(grades[1]))
        #         i +=1
        #     else:
        #         averages.append(grades[0], int(grades[1])
        #         i += 1
    highest = max(averages)
    return 
                
    # find the average of the two scores int()
    # append that value with the name into averages
    
    # find the maximum value of the test scores in averages max()
    # return that value and name 
