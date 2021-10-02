d={}

def chat_freq(st) :
    '''
    This function will return a dictionary with the key a the identical characters of string
    and the value of the key as the frequency of the character in the string
    '''
    # For looping through the input string
    for i in st :
        # Checking if the chatacter is present as a key in the list if not initialize the key with value 1
        if i not in d.keys() :
            d[i]=1
        # Else add the key value with previous key value and 1
        else :
            d[i]=d[i]+1

chat_freq('abbabcbdbabdbdbabababcbcbab')
print(d)

