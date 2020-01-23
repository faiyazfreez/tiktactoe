# class TicTacToe:
#     a = [" " for i in range(9)]

#     def display(self):
#         print("-"*13)
#         print("|",self.a[0],"|",self.a[1],"|",self.a[2],"|")
#         print("-"*13)
#         print("|",self.a[3],"|",self.a[4],"|",self.a[5],"|")
#         print("-"*13)
#         print("|",self.a[6],"|",self.a[7],"|",self.a[8],"|")
#         print("-"*13)
# class players(TicTacToe):
#     def __init__(self):
#         self.player1 = input("Enter Player1 Name : ")
#         self.player1_option = input("You X [or] O : ")
#         self.player2 = input("Enter Player2 Name : ")
#         self.player2_option = input("You X [or] O : ")
#         self.display()

#     def game_start(self):
#         while True:
#             player1_position = int(input("{} Enter Your Position : ".format(self.player1)))
#             # self.check_player(player1_position)
#             if self.a[player1_position-1] == " ":
#                 self.a[player1_position-1] = self.player1_option
#                 self.display()
#             else:
#                 print("Already Entered!\nTry another position")
#             player2_position = int(input("{} Enter Your Position : ".format(self.player2)))
#             if self.a[player2_position-1] == " ":
#                 self.a[player2_position-1] = self.player2_option
#                 self.display()
#             else:
#                 print("Already Entered!\nTry another position")
#             self.check = [
#                 (self.a[0], self.a[1], self.a[2]), (self.a[3],self. a[4], self.a[5]), (self.a[6], self.a[7], self.a[8]),
#                 (self.a[0], self.a[3], self.a[6]), (self.a[1],self. a[4], self.a[7]), (self.a[2], self.a[5], self.a[8]),
#                 (self.a[0], self.a[4], self.a[8]), (self.a[2],self. a[4], self.a[6])
#                 ]
#             for chk in self.check:
#                 if chk[0] == self.player1_option and chk[1] == self.player1_option and chk[2] == self.player1_option:
#                     return "The Winner is {}".format(self.player1)
#                 if chk[0] == self.player2_option and chk[1] == self.player2_option and chk[2] == self.player2_option:
#                     return "The Winner is {}".format(self.player2)
# game = players()
# print(game.game_start())


# l=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
# for i in l:
#     print(i[0],i[1],i[2])
#idula mela irukura process enathu

# l=[1,2,3,4]
# print(list(filter(l%2==0,l)))
# help(filter)

#reduce is in functools module
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100,80] 
# sums = (reduce((lambda x,y:x+y), li))
# print (sums) 

#filter(must list,tuple,set is to define)
# x=list(filter(lambda z:z%2!=0,li))
# print(x)

#map(must list,tuple,set is to define)
# x=list(map(lambda z:z*2,li))
# print(x)

# l=[1,2,3,4]
# for i,j in (enumerate(l)):
#     yield i,j

# yield should use inside of functions(if we use yield,must for loop use pananum)
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#         if num==3:
#             break
#     return num
# x=infinite_sequence()
# print(next(x))
# print(next(x))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(num)
# print(next(x))
# print(next(x))


# the function that will multiply each element by 5(yield example)
# def multiplyByFive(*kwargs): #Extra Notes in Yield function:
#    for i in kwargs:          #every generator is a iterator but not every iterator is generator
#        yield(i * 5)            #but iterator(in iter just use iter&next func) is more memory efficient using (.__sizeof__)
# print(multiplyByFive(4, 5, 6, 8))
# print(next(multiplyByFive(4, 5, 6, 8)))
# print(next(multiplyByFive(4, 5, 6, 8)))
# showing the values
# for i in multiplyByFive(4, 5, 6, 8):
#    print(i,end=' ')

# print(help('string'.isupper()))


# print(help(sum)) 


# from operator import itemgetter
# help(itemgetter)

# {'k':'joke','l':'last'}

# dicts = {"a":1,"b":2,"c":3}
# d ={k :("even" if v%2 == 0 else "odd") for (k,v) in dicts.items()}
# print(d)


# You can access the inner class in the outer class using the self keyword. 
# So, you can quickly create an instance of the inner class and perform operations in the outer class as you see fit.
# class Outer:
#     """Outer Class"""
#     def __init__(self):
#         ## instantiating the 'Inner' class
#         Outer.inner = self.Inner() #This shows the object created foer yhe Inner class.The object is class Name.something or Self.something
#     def reveal(self):
#         ## calling the 'Inner' class function display
#         Outer.inner.inner_display("Calling Inner class function from Outer class",'super')
#         self.Inner.outter_display()   #Here i am not mentioning the self so calling the function using class name
#     class Inner:
#         """Inner Class"""
#         def inner_display(self, msg,new_msg):  #Here i mentioned the self 
#             print(msg,new_msg,sep='\n')
#         def outter_display():  #Here i am not mentioned the class
#             print('hello')  
# outer=Outer()
# outer.reveal()


# class Outer:
#     """Outer Class"""
#     def __init__(self):
#         ## Instantiating the 'Inner' class
#         self.inner = self.Inner()
#         ## Instantiating the '_Inner' class
#         self._inner = self._Inner()
#     def show_classes(self):
#         print("This is Outer class")
#         print(self.inner)
#         print(self._inner)
#     class Inner:
#         """First Inner Class"""
#         def inner_display(self, msg):
#             print("This is Inner class")
#             print(msg)
#     class _Inner:
#         """Second Inner Class"""
#         def inner_display(self, msg):
#             print("This is _Inner class")
#             print(msg)
# # outer=Outer()                 #These 169 & 170 line is defined by me
# # outer.show_classes()          #Note in object assigning for class , with self can't be assign
# ## instantiating the classes
# ## 'Outer' class          
# outer = Outer()
# ## 'Inner' class
# inner = outer.Inner()   ## inner = outer.inner or inner = Outer().Inner()
# ## '_Inner' class
# _inner = outer._Inner() ## _inner = outer._outer or _inner = Outer()._Inner()
# ## calling the methods
# # outer.show_classes()
# # print()
# ## 'Inner' class
# inner.inner_display("Just Print It!")
# print()
# ## '_Inner' class
# _inner.inner_display("Just Show It!")


# class sum():
#     def add(self,a,b):
#         return a+b
# class divi():
#     def addu(self):
#         return self.add(5,6)
# x=divi()
# pr

# numbers=[7,2,3,4,5,6,8,9]
# odd_squares = [(number * number) for number in numbers if number % 2 == 1]
# # print(odd_squares)


# modified_numbers = [number * number if number % 2 == 1 else number * 2 for number in numbers]
# print(modified_numbers)

# m_num=[]
# for i in numbers:
#     if i%2==1:
#         m_num.append(i*i)
# print(m_num)

# m=[0 if number%2==0  if number%3==0 else number for number in numbers]
# print(m)

# matrix=[[1,2,3],[4,5,6]]
# flattened_list = [number for each_list in matrix for number in each_list]
# print(flattened_list)

# [0 if number % 2 == 0 else 1 if number % 3 == 0
#                    else number for number in numbers]

# import requests
# url='https://eu7.proxysite.com/process.php?d=bkq8faM4MU%2FJzypuogyorSO%2F&b=1'
# form_data={"server-option":"eu7",
#             "d":"www.tamilrockers.com",
#             "allowCookies":"on"
#             }
# r=requests.post(url,data=form_data).content
# print(r)

# for i in 'Anitha':
#     for j in 'vinitha':
#         print(i,j)


# i=10
# while not  i<1:
#     print(i)
#     i-=1

# for i in range(1,10):
#     print(i*"*",end='')

# a=5
# b=1
# print('begin')
# while b<=a:
#     # print('b=',b,'a=',a)
#     c=1
#     # d=a-b
#     while c<=b*2-1:
#         # print('c=',c,'b=',b)
#         print('*',end='')
#         c=c+1
#         # print('c=',c)
#     print()
#     b=b+1
#     print('end')

# def fibonacci(n):
#     a,b=0,1
#     while a<n:
#         print(a)
#         a,b=b,a+b     #this line is important in fibonacci
# fibonacci(20)

# x=int(input("\"a\":"))  #it will shows the output like "a":
# y=int(input('\'b\':'))  #it will shows the output like 'b':

# i=1
# while i<=5:
#     # print(i)
#     print("*",end='')   #Etanah time loop suthuto , atanah time star print aagum
#     i=i+1

# x=0
# for i in range(2,5):
#     x+=1
# print(x)


# Python program to print all  
# prime number in an interval 
  
# start = 1
# end = 100
# for val in range(start, end + 1): 
      
#    # If num is divisible by any number   
#    # between 2 and val, it is not prime  
#    if val > 1: 
#        for n in range(2, val): 
#            if (val % n) == 0: 
#                break
#        else: 
#            print(val) 



# x=[i * i for i in range(5)   if i % 2 == 0]
# print(x)

# import os
# os.chdir(r'C:\Users\FAIYAZ FREEZ\Desktop')
# print(os.getcwd())
# f=open('New Text Document.txt')
# print(type(f.readline()))
# # f.close()
# print(f.tell())
# f.seek(5)
# print(f.read())
# (f.close())
# print(closed())











