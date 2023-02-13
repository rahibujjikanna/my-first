
print("**** hello sir ( I AM AI ATM ).tq for came ****")

user_name='rahi'
password='123rahi'

a_name=(input("enter your user name:"))
b_password=str(input("enter your pin number:"))

if a_name==user_name and b_password==password:
   print('''
    1) PLZ TALK TO AI  
   
    ''')
else:
    print("plz enter currect pin sir if you do not enter currect pin options are in hide so enter currect pin")
amount=10000
option=int(input("enter your option:"))
if option==1:
    print(''' HELLO SIR 
    1) i am AI plz (if YOU DON'KNOW HOW TO DEPOSITE AND HOW TO WITHDRAW PLZ CLICK 1 option I WILL TELL YOU) 
    2) deposite
    3)withdraw
    4)statement
    5)forgot your pin
    6) exit
    ''')

    
enter=int(input(": "))
if enter==1:
    print('''
    @ deposite process
    @) swipe your card  next 
    1) plz click on deposite option sir
    2) enter your atm personal pin number sir
    3) then how much money deposte.enter money
    4) then successfull complete your deposite 

    @ withdraw process
    @ awipe your card
    1) plz click withdraw option sir
    2) enter your atm personal pin number sir
    3) then how much amount withdraw plz enter
    4) then successfull complate your withdraw
    
    

    ''')
elif enter==2:

    deposite=int(input("enter the money:"))
    amount=+deposite
    print("total amount",amount)
    print("<>"*40)
    
elif enter==3:

    withdraw=int(input("enter the money:"))
    amount=-withdraw
    print("total amount",amount)
    print("<>"*40)

elif enter==4:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("user_name:",user_name)
    print("total amount:",amount)

elif enter==5:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    print("password:",password)

    print("sir see your pin number")

elif enter==6:
    exit()

else:
    print("sorry sir plz enter current pin")
    


    





    



