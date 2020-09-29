# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:11:25 2020

@author: Cristian
"""

import math
from complex_numbers import complex_number
from complex_numbers import complex_cart
from complex_numbers import complex_polar
import mat_op
from matplotlib import pyplot as plt
def Plot(Targ,Prob):
    names = []
    for i in range(Targ):
        names += [i]
    values = Prob
    
    plt.figure('Quantum')
    plt.bar(names,values)
    plt.ylabel('Probability')
    plt.xlabel('Target')
    plt.suptitle('Multiple slit experiment')
    plt.show()
    
def mul_mat_real(A,B):
    m_a = len(A)
    n_a = len(A[0])
    m_b= len(B)
    n_b= len(B[0])
    if n_a == m_b:
        ans = [[0 for i in range(len(B[0]))] for i in range (len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    ans[i][j] +=  A[i][k] * B[k][j]
        return ans
    else:
        return 'Error, el producto entre matrices no se puede'
    
def Quantum_system(mat,click,state):
    def mul_mat_bool(A,B):
        m_a = len(A)
        n_a = len(A[0])
        m_b= len(B)
        n_b= len(B[0])
        if n_a == m_b:
            ans = [[False for i in range(len(B[0]))] for i in range (len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(A[0])):
                        ans[i][j] =  ans[i][j] or (A[i][k] and B[k][j])
        return ans
    
    start = mat
    if type(mat[0][0])== bool:
        for i in range(click):
            state_click = mul_mat_bool(start,mat_op.transpuesta(state))
            start = mul_mat_bool(start,mat) 
        ans = state_click[:]
        for i in range(len(ans)):
            if ans[i][0]==True:
                ans[i] = 1
            else:
                ans[i]=0
        Plot(len(ans),ans)
        state_click
    elif type(mat[0][0]) == type(complex_cart(1,0)): 
        for i in range(click):
            state_click = mat_op.mult_mat(start,mat_op.transpuesta(state))
            start = mat_op.mult_mat(start,mat)
        state_click = [(state_click[i][0].mod())**2 for i in range(len(state_click))]
        Plot(len(state_click),state_click)
    else:

        for i in range(click):
            state_click = mul_mat_real(start,mat_op.transpuesta(state))
            start = mul_mat_real(start,mat)
        Plot(len(mat_op.transpuesta(state_click)),mat_op.transpuesta(state_click))
    return state_click


def exp_real_slit(rendijas,blancos):
    
    n = ((rendijas-1)*math.ceil(blancos/2))+1+rendijas+blancos
    estado = [[0 for i in range (n)] for j in range (n)]
    for i in range(rendijas):
        estado[i+1][0]=1/rendijas
        for j in range(i*(math.ceil(blancos/2))+rendijas+1,i*(math.ceil(blancos/2))+rendijas+blancos+1):
            estado[j][i+1] += 1/blancos 
            estado[j][j] = 1 
    estado_2 = mul_mat_real(estado,estado)
    V = [0 for i in range(n)]
    V[0]=1
    V = mat_op.transpuesta(V)
    prob = mul_mat_real(estado_2,V)
    B = mat_op.transpuesta(prob)
    Plot(n,B)
    
    return prob

def exp_complex_slit(mat):
    A = mat
    V = [complex_cart(0,0) for i in range(len(mat))]
    V[0]=complex_cart(1,0)
    V = mat_op.transpuesta(V)
    for i in range(2):
        C = mat_op.mult_mat(A,V)
        A = mat_op.mult_mat(A,mat)
    B = mat_op.transpuesta(C[:])
    for i in range(len(B)):
        B[i] = B[i].mod()
    Plot(len(B),B)
    
    return C

        
    
    
    
