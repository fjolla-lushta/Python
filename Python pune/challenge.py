#Check if a user is not empty and the age is greater than or equal to 18

user="Fjolla"
age=23

if user and age >= 18:
    print("Kemi user dhe eshte me i madh se 18")


#Check if the password is at least 8 characters long and does not contain spaces

password="my password"

if len(password) >= 8 and " " not in password:
    print("Gjithqka ne rregull")
else:
    print("Passwordi duhet te jete 8 characters dhe nuk duhet te permbaje hapesira")


#Check if a users email is not empty,conatains @ and ends with .com

user_email="fjolla.lushta27@gmail"

if user_email and "@" in user_email and user_email.endswith(".com"):
    print("Ne rregull")
else :
    print("Permbushi kerkesat")


#Check if a username is a string ,is not None and is longer than 5 char

username="Fj"
if isinstance(username,str) and username is not None and len(username)>5:
    print("Mire osht")
else:
    print("Kqyr mire")


#Check if the user is either an admin or a moderator an either they're not banned or they've verified their email
is_admin=True
is_moderator=False
is_banned=False
is_email_verified=True
if(is_admin or is_moderator) and (not is_banned or is_email_verified):
    print("Kemi akses")


#Gjenero nje numer random edhe kqyr a osht cift apo tek
import random
num=random.randint(1, 100)
print("Number:",num)
if num %2 ==0:
    print("Even")
else:
    print("Odd")

#Validate the quality and correctness of email values
email="fjolla.lushta272gmail.com"
if email == "" :
    print("Email eshte bosh")
elif not("@" in email and "." in email):
    print("Mungon @ os .")
elif email.count("@") !=1:
    print("Email duhet me pas veq nje @")
elif not(email.endswith(".com") or email.endswith(".net")):
    print ("Email duhet te perunfdoj me .com ose .net")
elif len(email) > 254 :
      print("Email duhet me pas ma pak se 254 char")
elif not(email[0].isalnum() or email[-1].isalnum()):
    print("Email duhet me nis edhe me mbaru me shkronja dhe numra")
else:
    print("Email ne rregull")


#password validation
password = "my pass"

if password == "":
    print("Password mos me kon i zbrazet")
elif len(password) < 8:
    print("Password duhet me pas së paku 8 karaktere")
elif not any(c.isupper() for c in password):
    print("Duhet me pas të paktën një shkronjë të madhe")
elif not any(c.islower() for c in password):
    print("Duhet me pas të paktën një shkronjë të vogël")
elif password.strip() !=password:
    print("Pass sduhet me pas hapesira")
elif password != email :
    print("Pass duhet me kon i ndryshem me email")
elif not(password[0].isalnum() or password[-1].isalnum()):
    print("Pass duhet me fillu edhe me mbaru me shkronja dhe numra")
else:
    print("Password OK")


#7 shumezimi
for i in range(1,11):
    print(f"7 * {i} = {7*i}")


#* pattern
for i in range (1,7):
    print("*" * i)


#find duplicate names
file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

for file in set(file_list):
    if file_list.count(file) > 1:
        print(f"Duplicate file found: {file}")



#3 attempts me thon yes mandej nalet
attempts=0
while attempts < 3:
    answer=input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Thank you")
        break
    attempts += 1
print("3 strikes.You-re out")


#Dictionary Challenge
user={"id":1,"name":"John","age":30}
#1.Create new dict
users={"id":1,"name":"John","age":30,"city":"New York"}
#2.Keep only pairs with string values
#3.Convert values to uppercase
#4.Elegant & short solution
user_str={
    k.upper() : v.lower()
    for k,v in users.items()
    if isinstance(v,str)
}
print(user_str)


#calc the total of values
def total(*args):
    print(sum(args))


#Create the user profile
def create_user(**kwargs):
    print(type(kwargs))
    print(kwargs)
create_user(First_name="john",
            last_name="Lushta",
            age=33,
            country="Egypt")


#return examples
def clean_name(name):
    if not name:
        return None
    else:
        cleaned=name.strip().lower()
        return cleaned
    
cln_name=clean_name('M')
print(cln_name)