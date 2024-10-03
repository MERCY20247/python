#1. The volume of a sphere with radius  r is (4/3)*pie*r**2.
#what is the volume of the sphere with radius 5.
#make sure the program enters the radius from the keyboard and provide the answer in 2 dps.
# SOLUTION
radius=int(input("Enter the radius of the sphere:"))
pie = 3.14
volume = (4/3)*pie*radius**2
print(f"The volume of the sphere with{radius} is: {volume:.2f}")

 #2.Create a program to calculate the area of a triangle (1/2*base*height).
#Base and height should be entered using the keyboard.
    # SOLUTION
base = int(input("Enter the base of the triangle:"))
height = int(input("Enter the height of the triangle:"))
area = 1/2*base*height
print(f"The area of the triangle with base{base} and height{height} is: {area:.2f}")    

#3. WITI has tasked you to automate a simple grading system.
    # As a Python student, write a program used to display the grades that
    #the students will be receiving based on the mark scored in a subject.
    #The grades are:
    #90% - 100% Grade is A 
    # 80% - 89% Grade is B
    # 70% - 70% Grade is c
    # 60% - 69% Grade is D
    # 50% - 59% Grade is E
    # < 50% fail
    # SOLUTION
def get_grade(mark):
 if 90 <= mark <= 100 :
    return 'A'
 elif 80 <= mark < 90:
        return 'B'
 elif 70 <= mark < 80:
        return 'C'
 elif 60 <= mark < 70:
       return 'D'
 elif 50 <= mark < 60:
     return 'E'
 else:
    return 'Fail'
    def main ():
       mark=int(input("Enter the student's mark(0-100):"))
       grade=get_grade(mark)
       print(f"The student's grade is:{grade}")
  

  #4.WITI Academy is proposing a Sacco to help students save their money.
 # Design a platform that will do the following.
  # Welcome to, WITIAcademy Sacco.
  #1. Deposit money
  #2. Withdraw money
  #3. Check balance
  # Ensure if the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
  # If the student selects 3, the account balance should be displayed.
  #SOLUTION
print("Welcome to, WITIAcademy Sacco")  
account_balance = 0
run = 1
while run == 1:
 print('1. Deposit money') 
 print('2. Withdraw money') 
 print('3. Check balance')
selection = int(input("Enter desired option 1,2 or 3")) 
student_option = int(input("Enter your selection(1,2, or 3)")) 
if student_option == 1:
 print('n\...processing a deposit transaction...')
deposit_amount = int(input('Enter amount to be deposited'))
if deposit_amount < 1000:
 print("The minimum deposit should be 1000")
elif student_option == 2:
 withdraw_amount = int(input("Enter withdraw amount"))
if withdraw_amount < 500:
 print("The minimum withdraw amoun is 500")
elif student_option == 3:
 account_balance = deposit_amount-withdraw_amount
 print(f"The account balance is {account_balance}")
else:
 print('You entered a wrong option! Please select 1,2, or 3\n')                        
                                                                      