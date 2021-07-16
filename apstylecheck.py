from word2number import w2n
from num2words import num2words
from nameparser import HumanName

corrections = {}

def check_School(text):
    textArr = text.split(" ")

    if("school" in textArr or "School" in textArr):
        corrections[""] = "Make sure first letter of each word in school name is capitalized"


def check_Company(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i == "IOS" or i == "Iphone" or i == "Ipad" or i == "Imac"):
            corrections[i] = i.lower()
    corrections[" "] = "Make sure company/social media names are uppercase"


def check_its(text):
    textArr = text.split(" ")

    for i in textArr:
        if(i == "its" or i == "it's"):
            corrections[i] = f"check for proper use of {i}"


def check_Effect(text):
    textArr = text.split(" ")

    for i in textArr:
        if(("effect") in i or ("affect") in i):
            corrections[i] = f"check for proper use of {i}"


def check_Titles(text):
    textArr = text.split(" ")

    for i in textArr:
        i = HumanName(i).as_dict()

        if(i["title"] != ""):
            corrections[i["title"]
                        ] = "check for proper capitalization of title"


def check_Seasons(text):
    textArr = text.split(" ")

    seasons = ["Winter", "Spring", "Summer", "Fall", "Autumn"]

    for i in textArr:
        if(i in seasons):
            corrections[i] = "Check for proper capitalization. Seasons should only be capitalized if used in a title"


def check_Percentage(text):
    textArr = text.split(" ")

    for i in textArr:
        if("%" in i):
            corrections[i] = "% should be spelled out (percent)"

    for i in textArr:
        if((i.isnumeric() == True and textArr.index(i) == 0) and textArr[textArr.index(i) + 1] == "percent"):
            corrections[i] = "should be spelled out"
        else:
            try:
                w2n.word_to_num(i)
            except ValueError:
                pass
            else:
                if(textArr.index(i) != 0 and i.isnumeric() == False):
                    corrections[i] = "should be a numeric number"

# Remember to remove special charachters from string
# Add check_Nums method
