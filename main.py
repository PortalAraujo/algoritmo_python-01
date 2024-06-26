print ("########################################")
print ("#        ALOGORITMO EM PYTHON          #")
print ("########################################")
print ("# Escolha a opçao desejada:            #")
print ("#                                      #")
print ("# 1. Fibonacci                         #")
print ("########################################")

try:
    choice = int (input())

    if choice == 1:
        print ("FIB")
except: ValueError as error: