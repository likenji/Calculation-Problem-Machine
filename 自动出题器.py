# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:07:52 2017

@author: User
"""

import random
from fractions import Fraction
import time
answer1=[]
def oprt(k):
    if(k==2):
        return " + "
    else:
        return " - "

def gener(number=2):
    a1=random.randint(1,20)
    a2=random.randint(1,20)
    problem='{0}/{1}'.format(a1,a2)
    answer=Fraction(problem)
    for i in range(number-1):
        oprt2=random.randint(1,2)
        c1=random.randint(1,20)
        c2=random.randint(1,20)
        answer=answer + Fraction('{0}/{1}'.format(c1,c2)) if oprt2==2 else answer - Fraction('{0}/{1}'.format(c1,c2))
        problem+="{2}{0}/{1}".format(c1,c2,oprt(oprt2))
    return problem,answer

def main():
    time1=time.time()
    a="Y"
    while(a=="Y"or a=="y"):
        for i in range(10):
            t=gener(2)
            while(t[1]<0):
                t=gener(2);
            print("第{}题{}".format(i+1,t[0]))
            answer1.append(t)
            if i%5==4:
                print("\n")
        for i in range(10,15):
            t=gener(3)
            while(t[1]<0):
                t=gener(3);
            print("第{}题{}".format(i+1,t[0]))
            answer1.append(t)
            if i%5==4:
                print("\n")              
        checktheanswer=input("是否查看答案，输入Y表示是，输入N表示否")
        if(checktheanswer=="Y" or checktheanswer=='y'):
            for i in range(15):
                print("第{}题答案:{} = {}".format(i+1,answer1[i][0],answer1[i][1]))
                if i%5==4:
                    print("\n")        
        time2=time.time()
        print("本轮用时：{}s".format(time2-time1))
        a=input("你还要再来点题么？输入Y表示是，输入N表示否")
        
if __name__=="__main__":
    main()
