#!/usr/bin/env python
# coding: utf-8



def primos_gemelos(rango):
    resul=[]
    pg=False
    for i in range(3,rango,2):
        p=True
        for x in range(3,int(i**0.5)+1,2):
            if i%x==0:
                p=False
                break
        if p:
            if pg:
                resul.append((i-2,i))
            pg=True
        else:
            pg=False
    return resul
            
print(primos_gemelos(1000))






