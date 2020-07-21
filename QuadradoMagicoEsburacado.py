# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:40:27 2020

@author: asgun
"""
import numpy as np
import itertools
import math

results =[]
count = 0

def solViavel(arr):
    boolViavel = False
    
    if arr[:,0].sum() <= 42:
        if arr[:,1].sum() <= 42:
            if arr[:,2].sum() <= 42:
                if arr[:,3].sum() <= 42:
                    if arr[:,4].sum() <= 42:
                        if np.trace(arr) <= 42:
                            if np.trace(np.flipud(arr)) <= 42:
                                boolViavel = True
    return(boolViavel)

def check(arr):
    boolViavel = False
    
    if arr[:,0].sum() == 42:
        if arr[:,1].sum() == 42:
            if arr[:,2].sum() == 42:
                if arr[:,3].sum() == 42:
                    if arr[:,4].sum() == 42:
                        if np.trace(arr) == 42:
                            if np.trace(np.flipud(arr)) == 42:
                                boolViavel = True
    return(boolViavel)

def preenche(arrRef, tileVal, idxCont):
    #Recebe o valor do tile e o idx do conteiner
    for i in range(len(tileVal)):            
        lin = math.floor(idxCont[i] /5)
        col = idxCont[i] - lin*5
        arrRef[lin,col] = tileVal[i]

def passo8(arr, sTiles):
    global conteiner
    global tiles    
    global count
    comb = list(itertools.combinations(list(sTiles),3))
    
    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[4,0]  == 42:
            #Copia matrizes
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [22,23,24])
            
                if check(arr2):
                    count+=1                
                    #print(arr2)
                    results.append(arr2)
                
def passo7(arr, sTiles):
    global conteiner
    global tiles    

    comb = list(itertools.combinations(list(sTiles),2))
    
    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[3,0] +arr[3,1] == 42:
            #Copia matrizes
            set2= sTiles.copy() - set(c)
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [17,18])
            
                passo8(arr2,set2)
                
                
def passo6(arr, sTiles):
    global conteiner
    global tiles    

    comb = list(itertools.combinations(list(sTiles),2))
    
    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[2,0] +arr[2,1] == 42:
            #Copia matrizes
            set2= sTiles.copy() - set(c)
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [13,14])
            
                passo7(arr2,set2)
                
def passo5(arr, sTiles):
    global conteiner
    global tiles    

    comb = list(itertools.combinations(list(sTiles),2))
    
    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[1,1] +arr[1,3] == 42:
            #Copia matrizes
            set2= sTiles.copy() - set(c)
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [7,9])
            
                passo6(arr2,set2)

def passo4(arr, sTiles):
    global conteiner
    global tiles    

    comb = list(itertools.combinations(list(sTiles),2))
    
    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[0,1] +arr[3,1] == 42:
            #Copia matrizes
            set2= sTiles.copy() - set(c)
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [6,11])
            
                passo5(arr2,set2)
                
def passo3(arr, sTiles):
    global conteiner
    global tiles    

    comb = list(itertools.combinations(list(sTiles),2))
    
    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[0,4] +arr[4,0] == 42:
            #Copia matrizes
            set2= sTiles.copy() - set(c)
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [8,16])
            
                passo4(arr2,set2)
    
def passo2(arr, sTiles):
    
    global conteiner
    global tiles
    
    comb = list(itertools.combinations(list(sTiles),3))
    

    for c in comb:
        #Só vai para frente se preencher condicao 
        if sum(c) +arr[0,0] == 42:
            #Copia matrizes
            set2= sTiles.copy() - set(c)
                    
            permut1 = list(itertools.permutations(c))        
            
            for p in permut1:
                
                arr2 = np.copy(arr)    
                preenche(arr2,  p, [10,15,20])
            
                passo3(arr2,set2)
        




def square2():
   global conteiner 
   global count
   
   
   setNumbers = set(range(1,21))

   #Passo 0:
   comb = itertools.combinations(setNumbers,4)
   
   for c in comb:
       if sum(c)==42:
           permut1 = list(itertools.permutations(c))        
           set1= setNumbers - set(c)
        
           for p in permut1:
               #Passo 1
               arr1 = np.zeros([5,5])
               
               preenche(arr1,c,[0, 1, 2, 4])
               passo2(arr1, set1)
   print("Número de resultados:", count)

if __name__ == "__main__":
    square2()