# a python solution that reads the US Constitution, prompts for a search term, then displays the relevant sections.
# Read the Constitution from the internet 
import requests 
response = requests.get("https://www.usconstitution.net/const.txt")           # we want to import the link into a request to read
Constitutionstring = response.text

Constitutionstring_list = Constitutionstring.split("\n") 
search_term = input("Enter search term: ") 

start_line = 0 
end_line = 1 
while search_term != "": 
  for i in range (len(Constitutionstring_list)):
    if Constitutionstring_list[i].find(search_term) != -1: 
      for j in range(i, 0, -1):
         if Constitutionstring_list[j] == "":
           start_line = j
           break
      for j in range(i, len(Constitutionstring_list), +1):
         if Constitutionstring_list[j] == "":
            end_line = j + 1
            break
      for j in range(start_line, end_line):
        print()
        i = end_line
             


