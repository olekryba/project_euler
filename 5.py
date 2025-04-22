

svar=[]
delbart_med = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
b=1
c=0
rätt_b = False
while not rätt_b:
  
    rätt_b = True
    for delare in delbart_med:
        if b % delare == 0:
            None
        else:
            rätt_b = False
            break
    if rätt_b:
        print(b)
        break
    
            
    

    b=b+1


print(svar)
