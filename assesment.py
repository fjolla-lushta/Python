#Deklarimi i variablave
age=25 #int
height=1.75 #float
name="Fjolla" #string
is_student=True #bool

print(age,height,name,is_student)


#Me marr input nga perdoruesi
name=input("Shkruaj emrin:")
age=int(input("Shkruaj moshen:"))
print(f"Pershendetje {name}, ti je {age} vjecar")


#Funksion per shumen e dy numrave
def sum(a,b):
    return a+b
print(sum(5,3))


#Cift 
def eshte_cift(num):
    return num % 2 ==0
print(eshte_cift(5))

#Tek
def eshte_tek(num):
    return num %2 !=0
print(eshte_tek(4))


#Krijo file eshte shkruj diqka mrena
def write_log(message):
    with open(r"C:\Main\python\app.log","a") as file:
        file.write(message + "\n")
write_log("Fjalia e pare")


#Me lexu file
path = r"C:\Main\Python\app.log"
with open(path, "r", encoding="utf-8") as f:
    print(f.read())


#Numero fjalet
with open(path , "r" , encoding="utf-8") as f:
    text=f.read()
    words=text.split()
    print(len(words))


#Numero rreshtat
with open(path , "r" , encoding="utf-8") as f:
    lines=f.readlines()
    print(len(lines))


#Sa here paraqitet nje fjale
with open(path,"r",encoding="utf-8") as f:
    text=f.read()
    print(text.count("Hello"))


#Palindrome
#Jon ato fjalte qe kur i lexon edhe prej fundit osht e njejta fjale
def palindrome(s):
    return s == s[::-1]
print(palindrome("radar"))


#Me kthy nje string mrapsht
txt="python"
print(txt[::-1])

#Numero zanoret
def zanoret(s):
    count=0
    for c in s.lower():
        if c in "aeoiu":
            count+=1
        return count
print(zanoret("Hello World"))


#Krijo nje klas Person
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #Krijimi i objekteve dhe pastaj printimi i tyre
        person1=Person("Fjolla",25)
        person2=Person("Festim",30)
        print(person1.name,person1.age)
        print(person2.name,person2.age)


#Krijo nje objekt edhe printo
p=Person("Festim",25)
print(p.name,p.age)


#Metode per pershkrim
class Personi:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def pershkrim(self):
        print(f"Emri: {self.name},Mosha {self.age}")

p=Personi("Fjolla",23)
p.pershkrim()


#Factory function
def create_person(name,age):
    return Person(name,age)
p1=create_person("Arta",28)
print(p1.name)

#Liste me numra
numrat=[11,12,13,14]

#Max,min,mesatare
print(max(numrat))
print(min(numrat))
print(sum(numrat))
print(sum(numrat)/len(numrat))


#Filtro numrat cift
nums=[1,2,3,4,5,6]
even=list(filter(lambda x: x%2 ==0,nums))
print(even)


#Rendit listen
nums=[5,6,2,9,1]
#Prej ma tvogles deri te ma e madhja
print(sorted(nums))
#Prej ma tmadhes deri te ma e vogla
print(sorted(nums,reverse=True))


#Krijo nje for loop
for x in [1,2,3]:
    print(x)


#While loop(menu)
while True:
    print("1. Hi")
    print("2. Exit")
    choice = input ("Zgjedh:")
    if choice == "2":
        break


#Dictionary
person={"name":"Fjolla","age":24}
print(person["name"])


#Program me menu
while True:
    print("1. Hi")
    print("2. Exit")
    choice=input("Zgjedh:")
    if choice == "2" :
        break


#try/except
try:
    x=int(input("Numer:"))
#Vlera qe e shtypim ne terminal nese nuk osht numer shfaqet error
except:
    print("Error")


#Validim inputi
while True:
    password=input("Shkruaj passwordin:")
    if len(password)<8:
        print("Shume i shkurte!")


#Kontrollo nese lista ka vetem numra
items=['1','2','abc','4']
def vetem_numra(lista):
    return all(x.isdigit() for x in lista)
print(vetem_numra(items))


#Gjej numrin qe paraqitet me ne shumti ne nje liste
def gjej_me_shumti(nums):
    max_count=0
    result=None
    for n in nums:
        count=nums.count(n)
        if count > max_count:
            max_count=count
            result=n
    return result

nums=[1,2,3,4,3,3]
print(gjej_me_shumti(nums))


#Bashko dy lista pa duplikant
a=[1,2,3]
b=[3,4,5]
result=list(set(a) | set(b))
print(result)

#Filtro stringat qe kane gjatesi >4
words=["hi","hello","code",'AI']
long_words=list(filter(lambda x: len(x) > 4,words))
print(long_words)


#Numero karakteret ne nje string
text="Hello"
freq={}
for c in text:
    freq[c]=freq.get(c,0)+1
print(freq)


#Gjej numrat unik pa perseritje
nums=[1,2,2,2,3,4,4]
unique=[x for x in nums if nums.count(x) ==1]
print(unique)


#Validimi input(range)
while True:
    num=int(input("Shkruaj nje numer ne mes 1 deri 100"))
    if 1<=num <=100:
        print("Numri eshte valid")
        break
    print("Gabim")


#Kalkulator i thjeshte
def kalkulator(a,b,operation):
    if operation == "add":
        return a+b
    elif operation == "Substract":
        return a-b
    elif operation == "Multiply":
        return a*b
    elif operation == "Divide":
        return a/b
    

#lexo fikle edhe largo
with open(path,"r",encode="utf-8")as f:
    for line in f:
        print(line.strip())


#Gjej fjalen me te gjate
text="python si very powefu language"
words=text.split()
longest=max(words , key=len)
print(longest)

#Rendit dictionary sipas vlerave
data={"a":3,"b":1,"c":2}
sorted_data=sorted(data.items(),key=lambda x: x[1])
print(sorted_data)


#Kontrollo nese lista eshte sorted
nums=[1,2,3,4,5]
print(nums == sorted(nums))


#Gjej shumen e numrave cift
nums=[1,2,3,4,5,6]
result=sum(x for x in nums if x%2 ==0)
print(result)


#Kontrollo pass
password=input("Password:")
if len(password) >= 6 and any (c.isdigit() for c in password):
    print("Valid")
else:
    print("Invalid")


#Flatten list
matrix=[[1,2],[3,4],[5,6]]
flat=[x for row in matrix for x in row]
print(flat)


#Gjej intersection te dy listave
a=[1,2,3]
b=[2,3,4]
print(list(set(a) & set(b)))


#Krijo nje klase Student me mesatare
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    def mesatare(self):
        return sum(self.grades)/len(self.grades)
s=Student("Visar",[8,9,10])
print(s.mesatare())