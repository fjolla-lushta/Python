#Shkruaj një program që printon: "Hello, World!"
programi="Hello,World!"
print(programi)

#Merr një input nga user dhe printo atë.
inputi=input("Merr nje input qfare dush:")
print(inputi)

#Merr një numër dhe printo nëse është pozitiv apo negativ.
def qfar_numri(x):
    if x > 0 :
        print("Numer pozitiv")
    elif x == 0:
        print("Numri osht zero")
    else:
        print("Numer negativ")
qfar_numri(-4)

#Shkruaj program që kontrollon nëse një numër është çift apo tek.
def cift_tek(num):
    if num % 2 ==0:
        print("Numri eshte cift")
    else:
        print("Numri eshte tek")
cift_tek(5)

def tek_cift(numri):
    if numri %2 !=0:
        print("Numri eshte tek")
    else:
        print("Numri eshte cift")
tek_cift(4)

#Merr emrin dhe moshën dhe printo:
emri=input("Shkruje emrin:")
mosha=int(input("Shkruje moshen"))
print(f"Emri im eshte {emri} dhe jam {mosha} vjece")


#Merr një notë (0–100) dhe printo:
#90–100 → A
#80–89 → B
#70–79 → C
#<70 → F

def nota_fk(nota):
    if nota == 100:
        print("A+")
    elif nota >= 90:
        print("A")
    elif nota >=80:
        print("B")
    elif nota >=70:
        print("C")
    else:
        print("F")
nota_fk(82)


#Kontrollo nëse një numër është midis 10 dhe 50.
def midis(rangu):
    if rangu in range(10,50):
        print("True")
    else:
        print("False")
midis(40)


#Merr 3 numra dhe gjej më të madhin.
lista=[5,2,6,3]
print(max(lista))

#Kontrollo nëse një vit është vit i brishtë (leap year).
viti=int(input("Shtyp nje vit:"))
if (viti %4==0 and viti %100 !=0) or (viti % 400==0):
    print("Vit i brishte")
else:
    print("Nuk osh vit i brishte")

print(viti)

#Printo numrat nga 1 deri në 10 me for
for x in range(1,11):
    print(x)

#Printo vetëm numrat çift nga 1 deri në 20
newList=[num for num in range(1,20) if num % 2 ==0]
print(newList)

oldList=[num for num in range(1,20) if num % 2 !=0]
print(oldList)

#Gjej shumën e numrave nga 1 deri në 100
total=0
for x in range(1,100):
    total+=x
print(total)

#Përdor while për të printuar 10 deri në 1 (reverse).
i=10
while i >=1:
    print(i)
    i-=1

#Printo tabelën e shumëzimit për një numër (input nga user).
for i in range(1,11):
    print(f'8 * {i} ={8*i}')


#Krijo një listë me 5 numra dhe printo elementin e tretë
printo=[2,3,4,5,6]
print(printo[2])


#Shto një element në listë dhe pastaj fshije atë
printo.append(7)
print(printo)

printo.pop()
print(printo)

#Krijo një funksion që kontrollon nëse një string është palindrome (p.sh. "madam")
def palindroma(s):
    s==s[::-1]
palindroma("madam")

#Gjej maksimumin në një listë pa përdor max()
max_num = printo[0]

for i in printo:
    if i > max_num:
        max_num = i

print(max_num)

#Numëro sa herë shfaqet një element në listë
lst = [1, 2, 2, 3, 2, 4]
count = 0

for i in lst:
    if i == 2:
        count += 1

print(count)

#Krijo një funksion që merr 2 numra dhe kthen shumën e tyre
def merr_numra(a,b):
    return a+b
print(merr_numra(4,7))


#Krijo një program që:
#Merr një listë numrash
#I ndan në çift dhe tek
#I printon veçmas
even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)


#zanoret
def zanoret(s):
    for c in s.lower():
        if c in "aeriou":
            count+=1
        return 1
