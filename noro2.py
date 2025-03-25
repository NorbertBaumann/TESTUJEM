import random #volanie neakej jednotky

r = random.randint(-5, 5) # priradenie

print(r)

if r > 0:
    print('The r variable is positive')
elif r < 0:
    print('The r variable is negative') # vetvenie podmienky
elif r == 0: # porovnavanie
    print('The r variable is zero')
else: #ak nieje splnena predchadzajuca
    print('INAK nic')