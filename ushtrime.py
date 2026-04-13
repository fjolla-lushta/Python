#Deklarimi i funksionit edhe mi kry mathematic operaations

def arithmetic(x,y):
    try:
        sum=x+y
        sub=x-y
        prod=x*y
        div=x/y
        return sum,sub,prod,div
    except ZeroDivisionError:
        print("Nuk bon me pas zero")
    return

print(arithmetic(4,0))
print(arithmetic(4,2))


#Zanoret
def zanoret(s):
    count=0
    for c in s.lower():
        if c in "aeiou":
            count+=1
    return count
print(zanoret("HELLO WORLD"))


#Numer i perpjestushem me 7 ne range 1-50
newList=[num for num in range(1,51) if num %7==0]
print(newList)

#E hap ni file ja lexon permbajtjen edhe i numron rreshtat
try:
    with open("text.txt","r") as f:
        content=f.read()
        count=len(content.splitlines())
except FileNotFoundError:
    print("File not found")


class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def __str__(self):
        return f"Student {self.name} is {self.age} years old and is currently in {self.grade} grade"
    def change_grade(self,grade):
        self.grade=grade

student1 = Student("Fjolla",23,4)
print(student1.__str__())
student1.change_grade(5)
print(student1.__str__())



class Fakulteti:
    def __init__(self,name,surname,age,city,grade):
        self.name=name
        self.surname=surname
        self.age=age
        self.city=city
        self.grade=grade
    def __str__(self):
        return f"Student {self.name} {self.surname} is {self.age} years old ,lives in {self.city} and is in {self.grade} grade"
    def change_grade(self,grade):
        self.grade=grade
studenti=Fakulteti("Fjolla","Lushta",23,"Mitrovice",5)
print(studenti.__str__())
studenti.change_grade(4)
print(studenti.__str__())

#Deklarimi i variablave
numer_int=5
numer_float=4.5
vlere_string="Hello"
vlere_bool=True
print(numer_int,numer_float,vlere_string,vlere_bool)


#Cif edhe tek
def cift(num):
    return num %2 ==0
print(cift(3))

def tek(num):
    if num % 2!=0:
        return "Numer tek"
    else :
        return "Numer cift"
print(tek(4))


#input me marr
emri=input("Shkruje emrin:")
print("Pershendetje " ,emri)


num1=int(input("Shkruje numrin e pare:"))
num2=int(input("Shkruje numrin e dyte:"))
print(num1+num2)


#palindroma
def palindroma(s):
    s==s[::-1]
print(palindroma("Fjolla"))
print(palindroma("radar"))

#Me kthy fjalen mrapsht
txt=input("Shkruj qka dush:")
print(txt[::-1])


#Ni liste te qfaredoshme 
lista=[2,5,3,7,8]
print(max(lista))
print(min(lista))
print(sum(lista))
print(sum(lista)/len(lista))

#Filtro numrat tek nga lista
tek_numrat=list(filter(lambda x: x%2!=0,lista))
print(tek_numrat)

cift_numrat=list(filter(lambda x:x%2==0,lista))
print(cift_numrat)

print(sorted(lista))
print(sorted(lista,reverse=True))

for x in range(2,20):
    print(x)



class Studenti:
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country
    def __str__(self):
        return f"Emri im eshte {self.name} jam {self.age} vjece dhe jetoj ne {self.country}"
    def rrit_moshen(self,age):
        self.age=age
studenti1=Studenti("Fjolla",23,"Kosove")