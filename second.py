import string
import random

if __name__=="_main_":
    s1=string.assci_lowercase
    #a.appprint(s1)
    s2=string.assci_uppercase
    #print(s2)
    s3=string.assci_digits
    #print(s3)
    s4=string.assci_puctuuation
    #print(s4)
    plen=int(input("enter passward length/n"))#tool hole gebrish 
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    #print(s)
    print("".join(s[0:plen]))
