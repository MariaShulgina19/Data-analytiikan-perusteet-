# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print()
           
N=100
a=1
b=1
luku=a+b
print (a)
print (b)

while luku < N:
   
  print(luku)
  a=b
  b=luku
 
  luku=a+b
 
#%%
#Ltasaera laina
print()
k=200000 #laina määrä
p=3#vuosikorkoproseni
N=120#maksuerat
A=1+(p/12/100) #kuukausikorko
print ('kuukausikorko-', A)
m=(A**N*(A-1))/(A**N-1)*k #kuukauden lyhennys
print ('kuukausi era', m)
korko=(k*A)-k
print ('ensim. kuukausi', korko)
_jäljellä= k+korko-m
print (_jäljellä)
kk=1
print(kk)

korkoYht=korko

print ('kk  ' '  korko' '   jäljellä')

while kk <= N:
    #print (kk ,'   ' , korko, ' ' , _jäljellä)
    print('{:3d}  {:4.3f}   {:7.3f}'.format(kk,korko,_jäljellä))
    #print('{:3d},{:4d.3f}'.format(kk,korko))
    #print('{:3.3f}'.format(korko))
    kk +=1
    k=_jäljellä
    korko=(k*A)-k
    _jäljellä= k+korko-m
    korkoYht +=korko
print()    
print ('korko Yht: {:7.1f}'.format(korkoYht))  
  