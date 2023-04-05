num=5
print(num)
num=num+2
print(num)
num=num//3*6
print(num)
print(7+15%4)
num=24//3//4
print(num)
print('\n')

##total = 10
##greet = 'Hello'
##both = total + greet
##print(both)
print('\n')

total= '10'
greet='Hello'
both=total+greet
print(both)
print('\n')

print("A", end = "")
print("B", end = "")
print("C", end = "")
print("D", end = "")
print('\n')

a='10'
b='99'
c=a+b
print(c)
a=10
b=99
c=a + b
print(c)
print('\n')

name=input('please enter your name: \n')
print('Hello', name)
age=input('Your age is:')
print('your age is', age,'\n')
print('test\\test2\\answers.txt \n')

the_text= input('enter some text.')
print('this is what you entered:')
print(the_text)
print('this is what you entered:',the_text)
print('this is what you entered:',end='')
print(the_text)
print('\\n')

##self check question
num_1=int(input())
num_2=int(input())
total=num_1 + num_2
print(total)
print('\n')

cost=int(input('enter cost of item: $ '))
paid=int(input('enter cash paid :$ '))
change= paid - cost
print('change is :',change)
print('\n')

num_1=float(input())
num_2=float(input())
num_3=float(input())
average=(num_1 + num_2 + num_3)/3
print(round(average,2))
a=3
o=0
print('you have :  ',a,'apples and ',o,'oranges')
buy_a=4
buy_o=6
print('you buy :   ',buy_a,'apples and',buy_o,'oranges')
a=a+buy_a
o=o+buy_o
print('you now have:',a,'apples and',o,'oranges')
print('\n')

centigrade=float(input('enter centigrade : '))
fahrenheit=centigrade * 1.8
print(centigrade,'centigrades = ',fahrenheit,'farhrenheit')
print('\n')

num_input=input('Enter a number :')
try:
    num_val=int(num_input)
except:
    num_val= -1
if num_val > 0 :
    print('A number was entered')
else:
    print('not a number')
print('\n')

n=input("please enter an integer :")
try:
    n=int(n)
    print('number entered')
except ValueError:
    print("not valid")
print('\n')

while(True):
    number=input('enter number :')
    try:
        number=45/int(number)
        print('number entered')
    except ZeroDivisionError:
        print('cannot divide by zero')


n=5
while(n>0):
    n=n-1
    number=input('enter your number :')

    try:
        number=45/int(number)
        print('number entered correctlt. ' + str(number) + "\n")
    except ZeroDivisionError:
        print('Cannot Divide by zero' + "\n")
