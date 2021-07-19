from word2number import w2n
from num2words import num2words

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

def check(text):
    corrections.clear()
    sentences = text.lower().split(".")

    for j in sentences:
        j = j.replace("-", " ").replace("!","").replace("?","").replace(";","")
        textArr = j.lower().split(" ")
        if(textArr[0] == ""):
            textArr.pop(0)

        #Warn to check all company and social media names
        corrections[""] = "Make sure all company/social media names are capitalized"

        for i in textArr:
            if("," in i):
                textArr[textArr.index(i)] = i.replace(",", "")

        for i in textArr:
            try:
                if(i.isnumeric() == True and textArr.index(i) == 0):
                    corrections[i] = num2words(i)
                elif(validate_wordisnum(i) == True and textArr.index(i) == 0):
                    textArr.pop(textArr.index(i) + 1)
                elif(i.isnumeric() == True and (textArr[textArr.index(i) + 1] == "years" or textArr[textArr.index(i) + 1] == "year")):
                    continue
                elif(validate_wordisnum(i) == True and (textArr[textArr.index(i) + 1] == "years" or textArr[textArr.index(i) + 1] == "year")):
                    corrections[i] = w2n.word_to_num(i)
                elif(i.isnumeric() == True and (textArr[textArr.index(i) + 1] != "years" or textArr[textArr.index(i) + 1] != "year")):
                    if(int(i) in range (0,10) or (int(i) >= 100)):
                        if(textArr[textArr.index(i) + 1] != "percent"):
                            corrections[i] = num2words(i)
                elif(validate_wordisnum(i) == True and (textArr[textArr.index(i) + 1] != "years" or textArr[textArr.index(i) + 1] != "year")):
                        if(w2n.word_to_num(i) in range(10,100)):
                            corrections[i] = w2n.word_to_num(i)
            except IndexError:
                pass

        for i in textArr:
            #Warn schools should be capitalized
            if("school" in i):
                corrections[" "] = "Make sure first letter of each word in school name is capitalized"
            
            if(i == "its" or i == "it’s" or i == "it's"): #Check for proper use of it's
                corrections[i] = f"check for proper use of {i}"

            if("effect" in i or "affect" in i): #Check for proper use of effect/affect
                corrections[i] = f"check for proper use of {i}"

            seasons = ["winter", "spring", "summer", "fall"] #Check seasons capitalization
            if(i in seasons):
                corrections[i] = "Check for proper capitalizations of seasons. Seasons should not be capitalized unless used in a title"

            if("%" in i):
                corrections[i] = "% should be spelled out (percent)" #The symbol should never exist

            try:
                w2n.word_to_num(i)
            except ValueError:
                pass
            else:
                if((textArr.index(i) != 0 and i.isnumeric() == False) and textArr[textArr.index(i) + 1] == "percent"):
                    corrections[i] = w2n.word_to_num(i) #Percentage numbers should always be figures

            titles = ["senior","junior","sophomore","freshman","freshmen","principal","principle"]
            if(i in titles):
                corrections[i] = "check for correct capitalization of title"
                        
    return corrections
