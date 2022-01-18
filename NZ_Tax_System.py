#NZ Tax Calculator.
#G.Vaughan 15/1/2022
#Calculates effective tax paid

#NZ uses a progressive tax system.
#1st 14k = 10.5%;
#14k-48k = 17.5%;
#48-70k = 30%;
#70k - 180k 33%
#180k+ = 39%

#hard values for each bracket:
#1:  14000*.105 = 1470
#2:  (48000-14000)*.175+1470 = 7420
#3:  (70000-48000) * .3 + 7420 = 14020
#4:  (18000-70000)*.33+14020 = 50320
#5:  (salary-180k)*.39+50320 = ?

print("NZ Income Tax Calculator")
print("Please enter your salary:")

salary = int(input())
salary_error = 0

#start at the top and work down

if salary > 180000:
    tax = (salary - 180000) * .39 + 50320
elif salary <=180000 and salary > 70000:
    tax = (salary - 70000)* .33 + 14020
elif salary <=70000 and salary > 48000:
    tax = (salary - 48000)*.3 + 7420
elif salary <=48000 and salary > 14000:
    tax = (salary - 14000) *.175+ 1470
elif salary <=14000 and salary > 0:
    tax = salary * .105
elif salary <= 0:
    tax = 0
    print("You dont pay tax")
    salary_error = 1

if salary_error == 0:
    print ("net pay:  $"+str(salary - tax)+"0")
    print ("tax paid:  $"+str(tax)+"0")
    print ("effective tax rate:  %"+ str(round(tax/salary*100,2)))

#end nothing else to do.
    



