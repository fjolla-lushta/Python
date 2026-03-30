person=["Fjolla",23,'Programere','Kosove']
name,age,profession,country=person
print(age)

lista=[1,4,8,10,23]
print(max(lista))
print(min(lista))
print(sum(lista))
print(len(lista))


comb_1=[1,2,3]
comb_2=['a','b','c']
comb_3=list(zip(comb_1,comb_2))
print(comb_3)
#Kjo menyre spo funksionojka
comb_4=list(zip(comb_1 + comb_2))
print(comb_4)

letters=['A','B','C']
print(list(map(str.lower,letters)))

numbers=['1','2','3']
print(list(map(int,numbers)))

letters_2=['a','b','c']
print(list(map(str.upper,letters_2)))

spaces=['    Fjolla','Visar   ', '   Jon  ']
print(list(map(str.strip,spaces)))

#Kthen listen me elementet qe ka veq shkronja
items=['123','Fjolla','23','Visar']
for i in filter(str.isalpha,items):
    print(i)


items=['345','Fjolla2','Festim','456']
for j in filter(str.isalpha,items):
    print(j)


lista=[5,2,4,6,1]
print(sorted(lista))
#pe kthejka ni vlere te caktuar ne nje liste
print(abs(-3))


prices=[20,180,240,30,60]
print(list(filter(lambda p : p>40,prices)))
print(list(filter(lambda p : p <100,prices)))

shkolla=[['Fjolla','Lushta',85],
         ['Visar','Imeri',70],
         ['Jon','Doe',80]]
print(list(filter(lambda row : row[1] == 'Lushta',shkolla)))
print(list(filter(lambda row : row[2] <=70,shkolla)))
print(list(filter(lambda row: row[0].startswith('J'),shkolla)))


Bashkesia_1=[1,2,3,4]
Bashkesia_2=[3,4,5,6]
#Krejt elementet i merr pa duplikim
Union=set(Bashkesia_1) | set(Bashkesia_2)
#Te perbashktat
Intersection=set(Bashkesia_1) & set(Bashkesia_2)
#I merr qato qe i ka te ndryshme
Symetric_Differnce=set(Bashkesia_1) ^ set(Bashkesia_2)
Difference=set(Bashkesia_1) - set(Bashkesia_2)
Difference_2=set(Bashkesia_2)- set(Bashkesia_1)
print(Union)
print(Intersection)
print(Symetric_Differnce)
print(Difference)
print(Difference_2)
#Set Relationships
print(set(Bashkesia_2).issuperset(set(Bashkesia_1))) 
print(set(Bashkesia_2).issuperset({3,4}))    
print(set(Bashkesia_1).issubset(set(Bashkesia_2)))   
print(set(Bashkesia_1).isdisjoint(set(Bashkesia_2)))


user={'name':'Fjolla','age':23,'country':'Kosove'}
print(user['name'])
print(user.get('age'))
#I shtyp vetem keys => name,age,cuntry
print(list(user.keys()))
#i shtyp vetem values => Fjolla,23,Kosove
print(list(user.values()))
#i shtup krejt listen me kyes edhe values
print(list(user.items()))
#munesh me specifiku sakte qka don me shtyp
print(list(user.items())[0][0])
#qishtu e bon update
user.update({'email':'fjolla.lushta27@gmail.com'})
print(user)
#qishtu e specifikon qka don me fshi
user.pop('age')
print(user)



emri='Fjolla'
mosha=23

if emri and mosha >=18:
    print("Munesh mu regjistru")

password='23456789'
if password and len(password) >=8 and "@" not in password and " " not in password:
    print("Ky password bon")
else:
    print("Ky password nuk bon")

email='fjolla.lushta27gmail.com'
if email and "@" in email and email.endswith(".com"):
    print("Ky email eshte ne rregull")
else:
    print("Kqyri kerkesat mire")


username='Fjolla'
if isinstance(username,str) and username is not None and len(username)>7:
    print("Ky username eshte i vlefshem")
else:
    print("Ky username nuk eshte i vlefshem")


import random
num=random.randint(1,500)
print(num)
if num %2==0:
    print("Cift")
else:
    print("Tek")

emaili='fjolla.lushta27@gmail.com'
if email == "":
    print("Email bosh")
elif not("@" in emaili and "." in emaili):
    print("Mungon @ edhe .")
elif emaili.endswith(".com"):
    print("Nuk perfundon me .com")
elif emaili.count("@") !=1:
    print("Duhet veq nje @ me pas")
elif len(emaili) < 254:
    print("Email i gjatë shumë")
elif not(emaili[0].isalnum() or emaili[-1].isalnum()):
    print("Duhet mja nis e me perfundu me numera dhe shkronja")
else:
    print('Mire osht')

passi='453322'
if passi=='':
    print("Sbon me kon i thate")
elif len(passi) <8:
    print("Ma i madh se 8 char")
elif passi.strip() !=passi:
    print("Sbon hapesire")
elif passi != emaili:
    print("Ndryshe me kon")
elif not(emaili[0].isalnum() or emaili[-1].isalnum()):
    print("Mja nis e me perfundu me shkronja e me numra")
elif not any(char.isupper() for char in passi):
    print("Nje shkronj te madhe duhet me kpermbajte")
elif not any(char.islower() for char in passi):
    print("Nje shkronje te vogel duhet me permbajte")
else:
    print("Mire osht")



for i in range(1,11):
    print(f'8 * {i} ={8*i}')



file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
for file in set(file_list):
    if file_list.count(file)>1:
        print(f'Ka duplikime {file}')


attemps=0
while attemps <3:
    shkruj=input("Shkruj a yes/no:")
    if shkruj =="yes":
        print("Bravo")
        break
    attemps +=1
print("U kry")


def clean_name(name):
    if not name:
        return None
    else:
        clean_name=name.strip().lower()
        return clean_name
    print(clean_name("Fjolla     "))

def write_log(message):
    with open (r"C:\Main\python\app.log","a") as file:
        file.write(message + "\n")

write_log("Fjalia e pare")

def seperate_email(email):
    cl_email=email.strip().lower()
    username,domain=cl_email.split("@")
    return{"username:":username,
           "domain:": domain}
print(seperate_email("fjolla.lushta27@gmail.com"))