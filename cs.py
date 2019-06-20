def myinput():
         sname=input("Enter the server name")
         dname=input("enter the database name")
         uname=input("Enter the username")
         passd=input("Enter the password")
         a=("Server name:%s \n DBNAME:%s \n Username:%s \n Password:%s \n"%(sname,dname,uname,passd))
         return a
print(myinput())


