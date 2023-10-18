# a python solution that reads the US Constitution, prompts for a search term, then displays the relevant sections.
# Read the Constitution from the internet 

import requests
response = requests.get (' https://www.usconstitution.net/const.txt')
Constitutionfilestring = response.text 

filestringlist = Constitutionfilestring.split("\n")                   # we want the line to be splitted 
s = input("Enter Search Term: ")                               # s represted seach terms


Start_line = 0                                            # we want the start of the line to be at 0
end_line = 1 
while s != "" :                                            
    for i in range(len(filestringlist)):
        if filestringlist[i].find(s) != -1: 
            for j in range (i, 0, -1): 
                if filestringlist[j] == "": 
                    Start_line = j 
                    break 
            for j in range (i, len(Constitutionfilestring), +1):
                if filestringlist[j] == "": 
                    end_line = j +1
                    break                                    # we need the break to break the sections that were given
            for j in range (Start_line,end_line):
                print("line", j, ":", filestringlist[j])
            print()
            i = end_line                           # i in the end will euqal the end of the line
    s = input("Enter Search Term: ")