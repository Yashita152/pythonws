def myinput():
         sname=input("Enter the server name")
         dname=input("enter the database name")
         uname=input("Enter the username")
         passd=input("Enter the password")
         return sname,dname,uname,passd
def cs():
         sname,dname,uname,passd=myinput()
         a={"Sname":sname,"dname":dname,"Uname":uname,"Password":passd}
         l=[]
         l.extend(a.items())
         print(l)
cs()
         
