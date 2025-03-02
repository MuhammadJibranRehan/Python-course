name : str = "Muhammad Jibran Rehan"

print(type(name))
print(name)

print("name")

name : str = "Muhammad Jibran Rehan"

print(name)


message : str = '"Python" Students \n father Name'
print(message)



name : str = "Muhammad Jibran Rehan"
father_name : str = "Rehan Farooq Ul Haq"
education : str = "IX"
age : int = "15"
age1 : int = str(15)

card : str = "Python Student Card\n Student Name: "+ name + "\n Age:" + age + "\n Father Name: " + father_name + "\n Education: " + education
print(card)


print(7 + 8 + 2)



print(7 + \
      8 + \
      2)




name : str = "Muhammad Jibran Rehan"
father_name : str = "Rehan Farooq Ul Haq"
education : str = "IX"
age : int = 15

card : str = f"""
Python Student Card
Student Name: {name}
Father Name: {father_name}
Education: {education}
Age: {age}
"""

print(card)

try:
    ali = int(input("Enter your username"))
    saad = int(input("Enter your password: "))
    
    if ali == saad:
        print("ok ")
    else:
        print("ok! opening your page")
except ValueError:
    print("Enter a valid age")     



import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *shapater!*
""")
