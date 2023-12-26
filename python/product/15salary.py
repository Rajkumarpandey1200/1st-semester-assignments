# To determine the net salary of an employee when it is known that
# the employee is eligible to dearness allowance (DA) of 97% of the
# basic pay, House Rent Allowance (HRA) of 57% of the basic pay
# and medical allowance of Rs.150 . It is further known that 12% of
# the basic pay is deducted from the gross salary for the Employees’
# Provident fund (EPF) and Rs. 200 is deducted from the gross pay
# as the professional tax.


salary=float(input("Enter salary :"))
DA= salary*97/100;
HRA=salary*57/100;
MA=150;
EPF=salary*12/100;
PT=200;
GT= salary+DA+HRA+MA-EPF-PT;
print("Dareness allowence 97% is              \t:"'+',DA,u'\u20b9')
print("House Rent Allowence 57% is            \t:"'+',HRA,u'\u20b9')
print("Medical Allowence  is                  \t:"'+',MA,u'\u20b9')
print("Employees provident fund 12% deducted  \t:"'-',EPF,u'\u20b9')
print("Professional tax                       \t:"'-',PT,u'\u20b9')
print("Net salary----------------------------\t:",GT,u'\u20b9')