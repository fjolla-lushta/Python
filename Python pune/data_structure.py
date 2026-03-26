#list[]
#tuple()
#set{}
#dict{}

person=["Fjolla",23,"Programmer","Kosovo"]

name,age,profession,country=person

print(name)

#Functions
max()
min()
sum()
len()
all()
any()

#Methods
count()
index()

#Operators
#in
#is
#== ose < >


#Remove
#.clear() => Remove all items
#.remove(value) => Remove by values (First Match)
#.pop(index) => Remoove the last item

#Shallow copy
#copy2=original.copy()

#Deep copy perdore per nested lists
#copy2=copy.deepcopy(original)


#Kombinim i dy listave
letters=['a','b','c']
numbers=[1,2,3,4]
comb=list(zip(letters,numbers))
print(comb)


#Kombinimi i listave behet keshtu
#Simple combine A + B
#Nested list but keep them seperated [AB,CD]
#.extend()
#zip(AB,CD) => [(A,C),(B,D)]


#Map
letters=['a','b','c']
print(list(map(str.upper,letters)))

numbers=['1','2','3']
print(list(map(int,numbers)))

names=['   Maria','John   ',' Kumar  ']
for n in map(str.strip(),names):
    print(n)


#Filter
letters =['a','','b',None,'c',False ]
print(list(filter(bool,letters)))
#ose
print(list(filter(None,letters)))

items=['sql','123','python','42']
print(list(filter(str.isalpha,items)))
#ose
for i in filter(str.isalpha,items):
    print(i)


#Built in functions
len()
sorted()
abs()

#Quick and costume logic
#lambada

#Lambada shembull
prices=['$12.5','$9.99','$110.00']
print(list(map(lambda p: float(p.replace('$','')),prices)))

prices=[120,30,300,80]
print(list(map(lambda p: p>=100,prices)))

students=[['Maria',85],
          ['Kumar',90],
          ['Max',60]]
#E shtyp kush i ka pikte ma shume se 70
print(list(filter(lambda row : row[1]>= 70,students)))
#E shtyp kujt ja nis emri me shkronjen M
print(list(filter(lambda row: row[0].startswith('M'),students)))
