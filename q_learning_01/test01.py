import torch

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