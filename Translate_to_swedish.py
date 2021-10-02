di={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(ls):
    '''
    This function will translate the english words to swedish
    with a small bilingual lexicon as python dictonary to compare
    and return the converted english words.
    '''
    # For iterating through list ls
    for i in range(len(ls)) :
        # For iterating through di keys
        for j in di.keys() :
            # If list elements is equal to key then replace the key value
            if j == ls[i] :
                ls[i]=di[j]

    return ls

print(translate(['happy','new','year']))