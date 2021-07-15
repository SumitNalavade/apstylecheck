from namesparser import HumanNames
from word2number import w2n
from nameparser import HumanName

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

def check_Age(text):
    text = text.replace("-", " ")
    textArr = text.split(" ")

    for i in textArr:
        try:
            w2n.word_to_num(i)
        except ValueError:
            pass
        else:
            if(textArr[textArr.index(i) + 1] == "year" or textArr[textArr.index(i) + 1] == "years"):
                corrections[i] = "should be a numeric number"

def check_School(text):
    textArr = text.split(" ")

    if("school" in textArr or "School" in textArr):
        corrections[""] = "Make sure first letter of each word in school name is capitalized"

def check_Apple(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i == "IOS" or i == "Iphone" or i == "Ipad" or i == "Imac"):
            corrections[i] = "should be lowercase"

def check_its(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i == "its" or i == "it's"):
            corrections[i] = f"check for proper use of {i}"

def check_Effect(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i == "effect" or i == "affect"):
            corrections[i] = f"check for proper use of {i}"

def check_Titles(text):
    textArr = text.split(" ")

    for i in textArr:
        i = HumanName(i).as_dict()

        if(i["title"] != "" and i["title"][0].islower() == True):
            corrections[i["title"]] = "should be capitalized"

def check_Seasons(text):
    textArr = text.split(" ")

    seasons = ["Winter", "Spring", "Summer", "Fall", "Autumn"]

    for i in textArr:
        if(i in seasons):
            corrections[i] = "Check for proper capitalization. Seasons should only be capitalized if used in a title"

def check_Percentage(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i == "percent" and textArr.index(i) == 1):
            corrections[i] = "should be a symbol (%)"
        else:
            if("%" in i):
                corrections[i] = "should be spelled out"

#Remember to remove special charachters from string