#Let's say the HR team of a company has goodies set of size N each with a different price tag for each goodie. Now the HR team has to distribute the goodies among the M employees in the company such that one employee receives one goodie. Find out the goodies the HR team can distribute so that the difference between the low price goodie and the high price goodie selected is minimum.

import sys;
 
# arr[0..n-1] represents sizes of packets
# m is number of students.
# Returns minimum difference between maximum
# and minimum values of distribution.
def findMinDiff(goddie_prices, n, m):
 
    
    if (m==0 or n==0):
        return 0
 
    # Sort the given packets
    arr=list(goddie_prices.values())
    arr.sort()#sort array
 
    
    
    if (n < m):
        return -1
 
    
    min_diff = sys.maxsize
 
    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.


    i=0
    item=[]
    while(i+m-1<n ):
     
        diff = arr[i+m-1] - arr[i]
        if (diff < min_diff):
            min_diff = diff
            lowest=i
            highest=i+m-1
        i+=1

    b=[]
    godd={}
    b.append(arr[lowest:highest+1])
    #difference between the low price goodie and the high price goodie selected is minimum.
    key_list = list(goddie_prices.keys())
    val_list = list(goddie_prices.values())
    for ind in b:
        for i in ind:
            key=key_list[val_list.index(i)]
            godd[key]=i
    print(godd)
    return min_diff
# Driver Code
if __name__ == "__main__":

    goodie=['fitbit plus','ipods','mi bands','cult pass','mac book pro','digital camera','alexa','sandwich','microwave oven','Scale']
    prices=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
    m = int(input("Number of Employees : "))#no employee
    n = len(prices)#no of goodies
    goodie_prices=dict(zip(goodie,prices))#array is appended to dictionary using zip
    d=findMinDiff(goodie_prices, n, m)

    print("Minimum difference is",d)
