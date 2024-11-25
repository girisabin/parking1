import dbhelper3

print("Enter 1 for create table \n enter 2 for insert \n enter 3 show all records  \n enter 4 for exit" )

option = int(input("Enter the option:"))

if option==1:
    dbhelper3.create_query()

if option==2:
   dbhelper3.insert_query()

if option==3:
   dbhelper3.show_all()  

if option==4:
   dbhelper3.exit_parkinglot()
