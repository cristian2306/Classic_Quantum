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
    
def marbel_experiment(mat,click,state):
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
            state_click = mul_mat_bool(start,state)
            start = mul_mat_bool(start,mat) 
    else:
        for i in range(click):
            state_click = mat_op.mult_mat(start,state)
            start = mat_op.mult_mat(start,mat)
    return state_click


def exp_rendija_real(rendijas,blancos,prob):
    
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
    probabilidad = mul_mat_real(estado_2,V)
    return probabilidad

def exp_rendija_comple(mat,disparos):
    A = mat
    V = [complex_cart(0,0) for i in range(len(mat))]
    V[0]=complex_cart(1,0)
    V = mat_op.transpuesta(V)
    for i in range(disparos):
        C = mat_op.mult_mat(A,V)
        A = mat_op.mult_mat(A,mat)
        print(i,C)
    return C

        
    
    
    
