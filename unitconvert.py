# 1. Presentation Question (To be done in advance and then presented/discussed in the interview for 10 minutes)
# Please prepare a short presentation to the following question: What do you need to consider when upgrading a Database in an enterprise environment?
 
 
 
# 2. Coding Exercise (To be done in advance and then discussed in the interview for 15 minutes)
# Create a program that translates measurement units!
               
# The program should be able to take a string (as parameters on the command line), in the form of:          
# X unit1 in unit2   
 
# The program should produce a single string as output (command line, stdout) of the form:         
# Y unit2  
# Examples:            
# Input:                     Output:
# 5 m in cm              500 cm
# 50 cm in m            0.5 m
               
# You program needs to be deal with the following units:         
# m [metres]          
# cm [centimetres]
               
# Your program can just deal with the abbreviations (it doesn't need to be able to deal with the whole word)         
               
# Your program should be written to the standard that you'd expect in a commercial programming environment and should be buildable.   
          
# You should think about these questions to be discussed in interview: 
               
# - How easy would it be to add a new unit type?        
# - How can we test the program operates correctly?
# - How could this program be changed to operate as a web service?   end point like an API, allow people to send calculations and allow backend to respond, can filter through options

# - How could this program be changed to operate as a web site?         allow user input fields to take in values, drop down menus/or input for each unit type
               
# The program source code should be provided in a buildable form with build instructions that we can follow!     
   
# The program should be buildable on a UNIX-like environment, preferably OS X, but Linux or MSYS2 (Windows) are also acceptable.      




num1 = input('enter the value: ')
unit1 = input('Which unit do you want to convert it from: ')
unit2 = input('which unit do you want it converted to: ')

if unit1 == "cm" and unit2 == 'm':
    ans = float(num1) / 100
    print(ans,"m")
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1) * 100
    print(ans,'cm')

# unlimited additions can be added here, allows ease of adding a new unit type, the CLI flow allows many conversions instead of a "case" system which is more clunky for users

# need to test for correct inputs, isinteger(what happens if non number is put as value, what happens if non valid string value is placed for units), must also check for capitalisation of words
# end point like an API, allow people to send calculations and allow backend to respond, can filter through options, # if case system, api call can be made to case name based on switch statement from front end
#allow user input fields to take in values, drop down menus/or input for each unit type

# build instructions, pip pip install pipenv, python unitconvert.py
# def conversion():
#     user_input = input('Please input the desired conversion (X cm/m in cm/m): ')
#     try:
#         user_input = user_input.split()
#         from_unit = user_input[1]
#         to_unit = user_input[3]
#         value = int(user_input[0])

#         if (from_unit == 'cm' and to_unit == 'm'):
#             return print(str(value/100) + 'm')
#         elif (from_unit == 'm' and to_unit == 'cm'):
#             return print(str(value * 100) + 'cm')

#     except:
#         print('Please request a valid conversion')
#         conversion()

# conversion()