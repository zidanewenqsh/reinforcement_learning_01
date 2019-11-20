import torch
import random
q = torch.zeros(6,6)
r = -torch.ones_like(q)

# print(q)
# print(r)
# r[0,4],r[1,3],r[2,3],r[3,1:3],r[3,4],r[4,0],r[4,3],r[5,1],r[5,4]=0
r[[0,1,2,3,3,3,4,4,5,5],[4,3,3,1,2,3,0,3,1,4]]=0
r[[1,4,5],5]=100
print(r)
# a, b=1
# print(a)

indices = list(range(r.size(0)))
indices_ = list(range(r.size(0)))
y_index = random.sample(indices,1)[0]
x_index = random.sample(indices,1)[0]
print("a",y_index,x_index)
# indices.pop(y_index)
# print(indices)
# print(r[indices])
j = 0
for i in range(10):
    y_index = random.sample(indices, 1)[0]
    x_index = random.sample(indices, 1)[0]
    j=0
    while True:
        mask = r[y_index] != -1
        mask1 = mask.nonzero()
        x_index_1 = torch.randint(0,mask1.size(0),size=(1,))[0]
        x_index = mask1[x_index_1][0].item()
        print("indices",x_index,y_index)
        y_index = x_index

        if r[y_index,x_index] == 100:
            print(j, r[y_index, x_index])
            break

        j+=1