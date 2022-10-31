# to get ascii value we use     ord()
# to get letter                 chr()


def codeletter(word,key):
    newkey = key%26
    list = word
    ans=''

    for i in range(len(list)):
        letterposition = ord(list[i])+newkey
        if letterposition <= 122:
            ans=ans+chr(letterposition)
            
        else:
            ans=ans+chr(96+letterposition%122)
    
    print(ans)       

codeletter('abcd',2) 