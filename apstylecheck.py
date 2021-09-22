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

first = {
    "initial" : "",
    "fixed" : "",
    "index" : ""
}

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
                    first.update({"initial" : i, "fixed" : word2number(i), "index" : index})
                    corrections[i] = first
                elif(validate_wordisnum(i) == True and textArr.index(i) == 0):
                    textArr.pop(textArr.index(i) + 1)
                elif(i.isnumeric() == True and (textArr[textArr.index(i) + 1] == "years" or textArr[textArr.index(i) + 1] == "year")):
                    continue
                elif(validate_wordisnum(i) == True and (textArr[textArr.index(i) + 1] == "years" or textArr[textArr.index(i) + 1] == "year")):
                    first.update({"initial" : i, "fixed" : w2n.word_to_num(i), "index" : index})
                    corrections[i] = first
                elif(i.isnumeric() == True and (textArr[textArr.index(i) + 1] != "years" or textArr[textArr.index(i) + 1] != "year")):
                    if(int(i) in range (0,10) or (int(i) >= 100)):
                        if(textArr[textArr.index(i) + 1] != "percent"):
                            first.update({"initial" : i, "fixed" : num2words(i), "index" : index})
                            corrections[i] = first
                elif(validate_wordisnum(i) == True and (textArr[textArr.index(i) + 1] != "years" or textArr[textArr.index(i) + 1] != "year")):
                        if(w2n.word_to_num(i) in range(10,100)):
                            first.update({"initial" : i, "fixed" : w2n.word_to_num(i), "index" : index})
                            corrections[i] = first
            except IndexError:
                pass

        for index, i in enumerate(textArr):
            #Warn schools should be capitalized
            if("school" in i):
                first.update({"initial" : i, "fixed" : "Make sure first letter of each word in school name is capitalized", "index" : index})
                corrections[i] = first
            
            if(i == "its" or i == "it’s" or i == "it's"): #Check for proper use of it's
                first.update({"initial" : i, "fixed" : f"check for proper use of {i}", "index" : index})
                corrections[i] = first

            if("effect" in i or "affect" in i): #Check for proper use of effect/affect
                first.update({"initial" : i, "fixed" : f"check for proper use of {i}", "index" : index})
                corrections[i] = first

            seasons = ["winter", "spring", "summer", "fall"] #Check seasons capitalization
            if(i in seasons):
                first.update({"initial" : i, "fixed" : "Check for proper capitalizations of seasons. Seasons should not be capitalized unless used in a title", "index" : index})
                corrections[i] = first

            if("%" in i):
                first.update({"initial" : i, "fixed" : "% should be spelled out (percent)", "index" : index})
                corrections[i] = first
            try:
                w2n.word_to_num(i)
            except ValueError:
                pass
            else:
                if((textArr.index(i) != 0 and i.isnumeric() == False) and textArr[textArr.index(i) + 1] == "percent"):
                    first.update({"initial" : i, "fixed" : w2n.word_to_num(i), "index" : index})
                    corrections[i] = first

            titles = ["senior","junior","sophomore","freshman","freshmen","principal","principle"]
            if(i in titles):
                first.update({"initial" : i, "fixed" : "check for correct capitalization of title", "index" : index})
                corrections[i] = first 

    return corrections
