import sys
sys.setrecursionlimit(10**7)
string = input()

def AKA(x):
    if len(x) == 1:
        return True
    
    if x != x[::-1]:
        return False
      
    return AKA(x[:len(x)//2]) and AKA(x[-(len(x)//2):])
    

if AKA(string):
    print("AKARAKA")
else:
    print("IPSELENTI")