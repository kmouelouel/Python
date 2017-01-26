#regular Expression
import re
def main():
    line="I think that I understand the regular expression"
    matchresult=re.match(r'think',line,re.M|re.I)
    if (matchresult):
        print("match found :" + matchresult.group())
    else:
        print("No match was found")
        
    searchresult=re.search(r'think',line,re.M|re.I)
    if (searchresult):
        print("Search found :" + searchresult.group())
    else:
        print("No match was found")

main()
