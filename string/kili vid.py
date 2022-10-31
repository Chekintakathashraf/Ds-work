def ask(word):
    for i in range(len(word)):
        count=0
        for j in range(len(word)):
            if word[i]==word[j]:
                count=count+1
        print(str(count)+word[i])        

ask('aaabbc')













# word="aaabbc"
# print(word[5])