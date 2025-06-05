'''print(text+"*"*1)
print(text*2,"*"*1)
print(text*3,"*"*1)'''
'''print(text*(round-(x+1))+"*"*((x+1)+(x+2)))'''
'''    x*=2
    print(text*(round-(x+1))+"*"*((x+1)+(x+2)))'''

round = int(input())
space = " "

for x in range(round):
    for y in range(x+1):
        x+=1
    print(space*(round-(y+1))+(x*"*"))






