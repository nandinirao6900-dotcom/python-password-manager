import random
import json
import os 
import string
FILE_NAME = "passwords.json"  
def load_passwords():
    if  os.path.exists(FILE_NAME):
        try:
         
          with open(FILE_NAME, "r") as f :
            return json.load(f)
        except:
           return{} 
           
    else:
        return {}
    

def save_passwords(data):
    with open(FILE_NAME, "w") as f :
       json.dump(data , f , indent = 4)


def add_password():
   website = input("enter the website name = ")
   password = input("enter the password = ")
   data = load_passwords()
   data[website] = password
   save_passwords(data)
   print("password added successfully !")


def view_passwords():
    data = load_passwords()
    if not data:
       print("no passwords found!!")
    else:
       print("the passwords are:")
       for website , password in data.items():
          print(website, ":" , password)


def search_password():
   website = input("enter the website name = ")
   data = load_passwords()
   if website in data  :
      print("password = ", data[website])   
   else:
      print("website not found !")


def update_password():
   website = input("enter website = ")
   data = load_passwords()
   if website in data:
      new_password = input("enter new password = ")
      data[website] = new_password
      save_passwords(data)
      print("password updated successfully!!")
   else:
      print("website not found !!")


def delete_password():
   website = input("enter the website= ")
   data = load_passwords()
   if website in data:
      del data[website]
      save_passwords(data)
      print("password deleted successfully!")
   else:
      print("website not found!")


def generate_password():
  try:
      length =int(input("enter password length = "))
      characters = (string.ascii_letters+ string.digits+string.punctuation)
      password = "".join(random.choice(characters)                   
                 for _ in range(length))
      print("the generated password is ", password)
  except ValueError:
      print("please enter a valid number !")

while True:
     print("---PASSWORD MANAGER---")
     print("1.Add password")
     print("2.View password")
     print("3.Search password")
     print("4.Update password")
     print("5.Delete password")
     print("6.Generate password")
     print("7.Exit")
     choice = (input("Enter choice(1,2,3,4,5,6,7) ="))      
   
     if choice == "1":
        add_password()

     elif choice == "2":
        view_passwords()

     elif choice == "3":
        search_password()

     elif choice == "4":
        update_password()

     elif choice == "5":
        delete_password()

     elif choice == "6":
        generate_password()

     elif choice == "7":
        print("Goodbye!")
        break

     else:
        print("Invalid choice!")
        

 
