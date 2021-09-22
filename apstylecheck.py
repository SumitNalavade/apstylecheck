from word2number import w2n
from num2words import num2words
import word2number

def validate_wordisnum(text):
    try:
        w2n.word_to_num(text)
    except ValueError:
        return False
    else:
        if(text.isnumeric() == True):
            return False
        else:
            return True

corrections = {}

class correction:
    def __init__(self, initial, fixed, index):
        self.initial = initial
        self.fixed = fixed
        self.index = index

def check(text):
    corrections.clear()
    sentences = text.lower().split(".")

    for j in sentences:
        j = j.replace("-", " ").replace("!","").replace("?","").replace(";","")
        textArr = j.lower().split(" ")
        if(textArr[0] == ""):
            textArr.pop(0)

        for i in textArr:
            if("," in i):
                textArr[textArr.index(i)] = i.replace(",", "")

        for index, i in enumerate(textArr):
            try:
                if(i.isnumeric() == True and textArr.index(i) == 0):
                    corrections[i] = correction(i, word2number(i), index)
                elif(validate_wordisnum(i) == True and textArr.index(i) == 0):
                    textArr.pop(textArr.index(i) + 1)
                elif(i.isnumeric() == True and (textArr[textArr.index(i) + 1] == "years" or textArr[textArr.index(i) + 1] == "year")):
                    continue
                elif(validate_wordisnum(i) == True and (textArr[textArr.index(i) + 1] == "years" or textArr[textArr.index(i) + 1] == "year")):
                    corrections[i] = correction(i, w2n.word_to_num(i), index)
                elif(i.isnumeric() == True and (textArr[textArr.index(i) + 1] != "years" or textArr[textArr.index(i) + 1] != "year")):
                    if(int(i) in range (0,10) or (int(i) >= 100)):
                        if(textArr[textArr.index(i) + 1] != "percent"):
                            corrections[i] = correction(i, num2words(i), index)
                elif(validate_wordisnum(i) == True and (textArr[textArr.index(i) + 1] != "years" or textArr[textArr.index(i) + 1] != "year")):
                        if(w2n.word_to_num(i) in range(10,100)):
                            corrections[i] = correction(i, w2n.word_to_num(i), index)
            except IndexError:
                pass

        for index, i in enumerate(textArr):
            #Warn schools should be capitalized
            if("school" in i):
                corrections[i] = correction(i, "Make sure first letter of each word in school name is capitalized", index)
            
            if(i == "its" or i == "it’s" or i == "it's"): #Check for proper use of it's
                corrections[i] = correction(i, f"check for proper use of {i}", index)

            if("effect" in i or "affect" in i): #Check for proper use of effect/affect
                corrections[i] = correction(i, f"check for proper use of {i}", index)

            seasons = ["winter", "spring", "summer", "fall"] #Check seasons capitalization
            if(i in seasons):
                corrections[i] = correction(i, "Check for proper capitalizations of seasons. Seasons should not be capitalized unless used in a title", index)

            if("%" in i):
                corrections[i] = correction(i, "% should be spelled out (percent)", index)
            try:
                w2n.word_to_num(i)
            except ValueError:
                pass
            else:
                if((textArr.index(i) != 0 and i.isnumeric() == False) and textArr[textArr.index(i) + 1] == "percent"):
                    corrections[i] = correction(i, w2n.word_to_num(i), index)

            titles = ["senior","junior","sophomore","freshman","freshmen","principal","principle"]
            if(i in titles):
                corrections[i] = correction(i, "check for correct capitalization of title", index) 

    return corrections
