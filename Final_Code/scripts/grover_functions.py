from qiskit import QuantumCircuit, assemble, Aer, QuantumRegister, ClassicalRegister, AncillaRegister, transpile
from qiskit.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
import math
from math import log, ceil, floor
import plotly.express as px
import numpy as np
import timeit
import time

def create_oracle(v_reg, nb_check):
    qc = QuantumCircuit(v_reg + 1)

    a = len(bin(nb_check)[2:]) #This gives the length of binary value to encode
    pos = 0
    for j in list(bin(nb_check)[2:])[::-1]+(v_reg-a)*['0']: #loops through the reverse ordered list composed of the binary encoding of the value
        if not int(j):
            qc.x(pos)

        pos += 1

    qc.mct(list(range(v_reg)),v_reg)

    pos = 0
    for j in list(bin(nb_check)[2:])[::-1]+(v_reg-a)*['0']: #loops through the reverse ordered list composed of the binary encoding of the value
        if not int(j):
            qc.x(pos)

        pos += 1

    return qc

def encode_qc(i_reg,v_reg,val_array):

    qc = QuantumCircuit(i_reg + v_reg)

    for step in range(len(val_array)):

        x_place = 0 #This variable is used to find where to put the NOT in the CNOT encoding
        a = len(bin(val_array[step])[2:]) #This gives the length of binary value to encode

        for j in list(bin(val_array[step])[2:])[::-1]+(v_reg-a)*['0']: #loops through the reverse ordered list composed of the binary encoding of the value

            ### CONTROL X encoding ###
            if int(j):

                ### X encoding ###
                pos = 0
                b = len(bin(step)[2:])
                for i in list(bin(step)[2:])[::-1]+(i_reg-b)*['0']:

                    if not int(i) and int(j):
                        qc.x(pos)
                    pos += 1

                qc.mcx(list(range(i_reg)), i_reg + x_place)


                ### X encoding ###
                pos = 0
                b = len(bin(step)[2:])
                for i in list(bin(step)[2:])[::-1]+(i_reg-b)*['0']:

                    if not int(i):
                        qc.x(pos)
                    pos += 1

#                 qc.barrier() #uncomment this is you want a more readable circuit, but then cannot be used as gate


            x_place += 1

    return qc

def U_c():
    qc = QuantumCircuit(4)

    qc.x(1)
    qc.mcx([0,1],2, mode='noancilla')
    qc.x([0,1])
    qc.mcx([0,1],3, mode='noancilla')
    qc.x(0)

    return qc

def n_comp_p1(n):
    qc = QuantumCircuit(5*n)

    u_c = U_c().to_gate()
    u_c.label = "U_c"

    for i in range(n):
        qc.append(u_c, range(i*5,i*5 + 4))

    for i in range(n-1):
        qc.x(i*5 + 2)
        qc.x(i*5 + 3)
        qc.mcx([i*5 + 2, i*5 + 3], i*5 + 4, mode='noancilla')
        qc.x(i*5 + 2)
        qc.x(i*5 + 3)

    for i in reversed(range(n-1)):
        qc.mcx([i*5 + 4,i*5 + 7], i*5 + 2, mode='noancilla')
        qc.mcx([i*5 + 4,i*5 + 8], i*5 + 3, mode='noancilla')

    return qc

def n_comparator(n):
    qc = QuantumCircuit(5*n)

    c1 = n_comp_p1(n).to_gate()
    c1.label = "Comp_p1"

    qc.append(c1, range(5*n))

    qc.cx(3,5*n-1)

    qc.append(c1.reverse_ops(), range(5*n))

    return qc

def set_thresh(qc, nb_i_bits, nb_v_bits, val):
    pos = 0
    a = len(bin(val)[2:])
    # This time no [::-1] (no reverse order), as the order of encoding is opposite to the system; instead we first add the 0s and then the binary nb
    for j in (nb_v_bits-a)*['0']+list(bin(val)[2:]): #loops through the reverse ordered list composed of the binary encoding of the value
        if int(j):
            qc.x(nb_i_bits+ pos*5)

        pos += 1
