medical_cause=input("Did you have an medicalcause? yes or no:")

attendence=int(input("enter the attendence of the student:"))

if medical_cause=="yes":
    print("you are allowed")
else:
    if attendence>=75:
      print("allowed")
    else:
      print("not allowed")