'''
gör många produkter

23 x 34

'''

# abba
def is_palindrome(ord):
    i = 0
    x = -1
    y=0
    while y < len(ord)/2:
        if ord[i+y] ==  ord[x-y]:
            y=y+1
        else:
            return False

    return True
        

a=[]
b=[]
tal=0
count=0
while count <999:
    count=count+1
    tal=tal+1
    a.append(tal)
    b.append(tal)

hej=0
då=0
lista=[]
while då < 999:
    hej=0
    while hej < 999:
        tal=a[hej]*b[då]
        hej=hej+1
        if is_palindrome(str(tal)):
            lista.append(tal)
    då=då+1


print(max(lista))