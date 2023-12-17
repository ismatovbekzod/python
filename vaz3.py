# import os
# import math
# os.system("cls")
# def  tub(son):
#     for i in range(2,int(math.sqrt(son))+1):
#         print("a")
#         if son % i == 0:
#             print(False)
#             break            
#         else:
#             print(True)
            
            
# tub(int(input("Son kiriting : ")))
import os
import math

# Clear the terminal screen
os.system("cls")

def tub(son):
    if son < 2:
        return False    
    for i in range(2, int(math.sqrt(son)) + 1):
        if son % i == 0:
            return False
    
    return True

n = int(input("Son kiriting : "))
print(tub(n))
