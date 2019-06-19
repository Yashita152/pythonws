def myinput():
          a=int(input("Enter no.1 "))
          b=int(input("Enter no.2"))
          print(a)
          print(b)
          return a,b
def compute(n1,n2):
         sum=n1+n2
         return sum
def main():
         a,b=myinput()
         sum=compute(a,b)
         print("The sum of two nos is",sum)
main()

