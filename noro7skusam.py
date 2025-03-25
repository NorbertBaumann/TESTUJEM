import statistics
# # print message: John Doe is 34 years old and he is a gardener
# name = "John Doe"
# age = 34
# occupation = 'gardener'
# msg= name +" is " str(age) + "" years old and he is a " + occupation # toto je standard
#msg = f'{name} is {age} years old ' #toto je najlepsie
#print (msg)
# print(name,"is",age,"years old and he is a",occupation) # toto som vymyslel ja


# calculate sum using for/while loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mysum = 0
for val in vals:
    mysum += val

print('the sum is', mysum)

# calculate minimum, maximum, number of els, sum, mean
# use functions
vals2 = [1, -2, 13, 24, 5, 9]
print(min(vals2))
print(max(vals2))
print(len(vals2))
print(sum(vals2))

print(sum(vals2)/len(vals2))
print(statistics.mean(vals2))
print(sum(vals2)/len(vals2))
print(statistics.mean(vals2))

filename = 'words.txt'

with open(filename, 'r') as fd:
    for line in fd:
        print(line.strip().upper())