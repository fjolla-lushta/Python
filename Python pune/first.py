#Komentet shkruhen keshtu

print("Your Learning path: \n\t - Python Basics \n\t -Data Engineering \n\t -Ai")

#variable a name you create to store a value

name = ".com" 

print("fjolla.lushta27@gmail" + name)

tel = "+49 (176) 123-4567"

print(tel.replace(" ", "").replace("+" , "00"))

name="Fjolla"
age=23

print(f"My name is {name} and I am {age} years old.")

#.strip() perdoret per mi hek hapesirat e panevojshme nga fillimi dhe fundi i nje stringu

#.find() perdoret per me gjete diqka edhe e kthen indeksin e saj

#.isalpha() perdoret per me kontrollu nese nje string permban vetem shkronja

x=5 #real
y=3 #imagjinar
print(complex(x,y)) #output: 5+3j

#math.floor() nese osht 1.3 e bon 1,nese osht 2.7 e bon 2
#math.ceil() nese osht 1.3 e bon 2 dmth gjithe vleren ma shume
#math.trunc() nese e kena 1.5 e bon 1 , 2.3 e bon 2 dmth e merr numrin e pare para pikes

#per register form
#all([],[]) ktu krejt fields duhet mu plotsu qe me kon true
#any([],[]) njo me kon true dmth ni field mu plotsu osht boll

#match me case si perdoren
match country:
    case "germany":
        print("Germany")
    case "italy":
        print("Italy")
    case _:
        print("Other Country")