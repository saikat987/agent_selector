
from collections import deque
import random
#four queues ,three for the available three types and one for the busy one 

q1,q2,q3,b=[],[],[],[]

#structure of the agents datatype
class agents:
    unique_id=0
    def __init__(self,name,is_available,post,avaialable_since=None):
        self.name=name
        self.unique_id=agents.unique_id
        self.is_available=bool(is_available)
        self.post=post
        if is_available:
            self.available_since=avaialable_since
        else :
            self.available_since=None
        agents.unique_id+=1
#function that describe the method        
def random1(p):
    if p=="spanish speaker" :
        if q1:
            #to calculate the length of the queue to generate a random no within a range
            l=len(q1)
            #generating a random no and sending him request to solve the issue
            q=random.randint(0,l-1)
            print(q1[q].name+" is registered with this issue waiting for him to resposne\n")
            b.append(q1.pop(q))
        else :
            #if there is no agents available in the available queue
            print("please wait since currently all our executive are busy\n")
        
    elif p=="sales" :
        if q2:
            
            l=len(q2)
            q=random.randint(0,l)
            print(q2[q].name+" is registered with this issue waiting for him to resposne\n")
            b.append(q2.pop(q))
        else :
            print("please wait since currently all our executive are busy\n")
        
    elif p=="support":
        if q3:
            
            l=len(q3)
            q=random.randint(0,l)
            print(q3[q].name+" is registered with this issue waiting for him to resposne\n")
            b.append(q3.pop(q))
        else:
            print("please wait since currently all our executive are busy\n")

            
def all_available(p):
    if p=="spanish speaker" :
        if q1:
            for i in q1:
                
                print(i.name+" is registered with this issue waiting for them to accept\n")
        else :
            print("please wait since currently all our executive are busy\n")
        
    elif p=="sales" :
        if q2:
            
            for i in q2:
                
                print(i.name+" is registered with this issue waiting for them to accept\n")
        else :
            print("please wait since currently all our executive are busy\n")
        
    elif p=="support":
        if q3:
            
            for i in q3:
                
                print(i.name+" is registered with this issue waiting for them to accept\n")
        else:
            print("please wait since currently all our executive are busy\n")
def least_busy(p):
    if p=="spanish speaker" :
        if q1:
            print(q1[0].name+"is registered with this issue")
            b.append(q1.pop())
        else :
            print("please wait since currently all our executive are busy")
        
    elif p=="sales" :
        if q2:
            
           print(q2[0].name+"is registered with this issue")
           b.append(q2.pop())
        else :
            print("please wait since currently all our executive are busy")
        
    elif p=="support":
        if q3:
            
           print(q3[0].name+"is registered with this issue")
           b.append(q3.pop())
        else:
            print("please wait since currently all our executive are busy")






#main function
t=int(input("enter the no of agents first the available one  and then the non available\n"))
l=[] 
print("enter the name ,is avaialable or not and if yes then enter in a sorted order wrt availavle since\n")

while(t):
    
    n=(input("name\n"))
    a=bool(input("is available 0 to no, 1 for yes\n"))
    p=input("enter the post either spanish speaker,sales,support\n")
    if a:
        a2=input("available since in minute\n")
        ag=agents(n,a,p,a2)
        if p=="spanish speaker":
            q1.append(ag)
        elif p=="sales":
            q2.append(ag)
        elif p=="support":
            q3.append(ag)
    else:
        a=agents(n,a,p,a2)
        b.append(a)
    t-=1

# main function to work with issues here you have to take input the type of the issue and it will continue until your issues are resolved
while True:
    
    
    p=input("enter the issue either spanish speaker related salse related or support related \n")
    t=input("type of search\n")
    if p=="spanish speaker":
        if t=="random":
            random1(p)
        elif t=="least_busy":
            least_busy(p)
        elif t=="all_available":
            all_available(p)
    elif p=="sales":
        if t=="random":
            random1(p)
        elif t=="least_busy":
            least_busy(p)
        elif t=="all_available":
            all_available(p)
    elif p=="support":
        if t=="random":
            random1(p)
        elif t=="least_busy":
            least_busy(p)
        elif t=="all_available":
            all_available(p)
    else:
        print("wrong choice please try again")
    print("do you have more issue? if yes press 1 else press 0")
    if not (int(input())):
        break
        
        
        
#NOTE
#we can have extra method that will work after the agents accept regect or resolve the problem
bool(0)