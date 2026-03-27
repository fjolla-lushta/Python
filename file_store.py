#Store applications log messages in a file
def write_log(message):
    with open (r"C:\Main\python\aoo.log","a") as file:
        file.write(message + "\n")

write_log("App Started")
write_log("User logged in")


#clean an email and slit it into username and domain
def clean_and_split_email(email):
    cl_email=email.strip().lower()
    username,domain=cl_email.split("@")
    return{"username":username,
           "domain":domain}

clean_and_split_email("sara@gmail.com")

#Project
def process_user_email(email):
    write_log("App started")
#1.Receive an email from the user
email=input("Please enter your email:")
#2.Validate the eamil
is_valid_email(email)
#3.If it is invalid,Log an error in a file
if not is_valid_email(email):
    write_log(f"Invalid email received: {email}")
else:
    clean_email=clean_and_split_email(email)
    write_log(f"Processed Email:{clean_email}")
write_log("App Stopped")
#4.If it is valid,clean and structure the email
#5.Log each step of the program
email=input("Please enter your email:")


#Llojet e function
#Action functions (Print,connect,send,call)
#Validation functions (output true edhe false)
#Transformation functions (input dhe output jane te ndryshem)
#Orchestration function(thir funskione te tjera dhe organizon logjiken e programit)