# a python solution that reads the US Constitution, prompts for a search term, then displays the relevant sections.
# Read the Constitution from the internet 
import requests
def read_Constitution(): 
 response = requests.get("https://www.usconstitution.net/const.txt")
 return response.text
 
# read the Constitution 
Constitution_line = read_Constitution()
# Split the string by newline character into a list
Constitution_linelist = Constitution_line.split("\n")
# find the revelent section 
def find_sections(search_term, Constitution_line):
 found = False
 section_current = []

 for num_line, line in enumerate (Constitution_line):
  if search_term.lower() in line.lower():
   if not found:
    print(f"Found in the US Constitution:\n")
    found = True

    print(f"line {num_line+1}:\n{line}")
    start_line= num_line
    end_line = num_line

    # we want to find the start of the section 
    while start_line > 0 and Constitution_line[start_line-1].strip() != "":
     start_line -=1 

    # we want to find the end of the section 
    while end_line < len(Constitution_line) - 1 and Constitution_line[end_line+1].strip() != "":
     end_line +=1
    
    # we want to display the sections 
    for i in range (start_line, end_line +1 ):
     section_current.append(f"Line {i + 1}:\n{Constitution_line[i]}")

    if found: 
     print("\n".join(section_current))

if __name__== "--Main--": 
 while True:
  search_term = input("Enter search term (blank to exit): ").strip()
  if not search_term:
      break

  find_sections(search_term, Constitution_linelist) 