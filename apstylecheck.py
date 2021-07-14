from word2number import w2n

corrections = {}

def check_NumsToStartSentence(text):
    textArr = text.split(" ")

    if(textArr[0].isnumeric() == True):
        corrections[textArr[0]] = "should be spelled out"
    
def check_GeneralNums(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i.isnumeric() and (int(i) in range(0, 10) or int(i) >= 100)):
            corrections[i] = "should be spelled out"
        else:
            try:
                w2n.word_to_num(i)
            except ValueError:
                pass
            else:
                corrections[i] = "should be a numeric number"

check_GeneralNums("There are ten questions on the quiz")
print(corrections)
