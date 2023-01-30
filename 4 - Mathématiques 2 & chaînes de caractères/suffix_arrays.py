
# Python3 program for building suffix 
# array of a given text
 
# Class to store information of a suffix
class suffix:
     
    def __init__(self):
         
        self.index = 0
        self.rank = [0, 0]
 
# This is the main function that takes a 
# string 'txt' of size n as an argument, 
# builds and return the suffix array for
# the given string
def buildSuffixArray(txt, n):
     
    # A structure to store suffixes 
    # and their indexes
    suffixes = [suffix() for _ in range(n)]
 
    # Store suffixes and their indexes in
    # an array of structures. The structure
    # is needed to sort the suffixes alphabatically
    # and maintain their old indexes while sorting
    for i in range(n):
        suffixes[i].index = i
        suffixes[i].rank[0] = (ord(txt[i]) -
                               ord("a"))
        suffixes[i].rank[1] = (ord(txt[i + 1]) -
                        ord("a")) if ((i + 1) < n) else -1
 
    # Sort the suffixes according to the rank
    # and next rank
    suffixes = sorted(
        suffixes, key = lambda x: (
            x.rank[0], x.rank[1]))
 
    # At this point, all suffixes are sorted 
    # according to first 2 characters.  Let 
    # us sort suffixes according to first 4
    # characters, then first 8 and so on
    ind = [0] * n  # This array is needed to get the
                   # index in suffixes[] from original
                   # index.This mapping is needed to get
                   # next suffix.
    k = 4
    while (k < 2 * n):
         
        # Assigning rank and index 
        # values to first suffix
        rank = 0
        prev_rank = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        ind[suffixes[0].index] = 0
 
        # Assigning rank to suffixes
        for i in range(1, n):
             
            # If first rank and next ranks are 
            # same as that of previous suffix in
            # array, assign the same new rank to 
            # this suffix
            if (suffixes[i].rank[0] == prev_rank and
                suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
                prev_rank = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
                 
            # Otherwise increment rank and assign    
            else:  
                prev_rank = suffixes[i].rank[0]
                rank += 1
                suffixes[i].rank[0] = rank
            ind[suffixes[i].index] = i
 
        # Assign next rank to every suffix
        for i in range(n):
            nextindex = suffixes[i].index + k // 2
            suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] \
                if (nextindex < n) else -1
 
        # Sort the suffixes according to
        # first k characters
        suffixes = sorted(
            suffixes, key = lambda x: (
                x.rank[0], x.rank[1]))
 
        k *= 2
 
    # Store indexes of all sorted 
    # suffixes in the suffix array
    suffixArr = [0] * n
     
    for i in range(n):
        suffixArr[i] = suffixes[i].index
 
    # Return the suffix array
    return suffixArr
 
# A utility function to print an array
# of given size
def printArr(arr, n):
     
    for i in range(n):
        print(arr[i], end = " ")
         
    print()
 
# Driver code
if __name__ == "__main__":
     
    txt = "banana"
    n = len(txt)
     
    suffixArr = buildSuffixArray(txt, n)
     
    print("Following is suffix array for", txt)
     
    printArr(suffixArr, n)
 
# This code is contributed by debrc
