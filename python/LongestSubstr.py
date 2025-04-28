"""
Function to find the longest substring in alphabetical order

"""

def findSubstring(arg):
    longest=""
    s=arg[0]
    for i in range(0,len(arg)-1):
        if arg[i] < arg[i+1]:
          s+= arg[i+1]
          if len(longest) < len(s):
            longest=s
        else:
            s = arg[i+1]
    return longest
           
          
    
print (findSubstring ("abcamdnakdnabcdefgh")) 





    