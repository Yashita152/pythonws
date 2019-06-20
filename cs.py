def myinput():
         sname=input("Enter the server name")
         dname=input("enter the database name")
         uname=input("Enter the username")
         passd=input("Enter the password")
         return sname,dname,uname,passd
def f(s,d,u,p):
         return s,d,u,p
def main():
         sname,dname,uname,passd=myinput()
         s,d,u,p=f(sname,dname,uname,passd)
         print("The string names are:",s,d,u,p)
main()
