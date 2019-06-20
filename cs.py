def myinput():
         sname=input("Enter the server name")
         dname=input("enter the database name")
         uname=input("Enter the username")
         passd=input("Enter the password")
         return sname,dname,uname,passd

def main():
         sname,dname,uname,passd=myinput()
         print("Server name:",sname,"\n DBNAME",dname,"\n Username:",uname,"\npwd:",passd)
main()
