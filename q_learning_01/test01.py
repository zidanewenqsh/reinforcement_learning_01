import torch
import random

torch.set_printoptions(precision=0, sci_mode=False)
q = torch.zeros(5, 6)
r = -torch.ones(6, 6)

# print(q)
# print(r)
# r[0,4],r[1,3],r[2,3],r[3,1:3],r[3,4],r[4,0],r[4,3],r[5,1],r[5,4]=0
r[[0, 1, 2, 3, 3, 3, 4, 4, 5, 5], [4, 3, 3, 1, 2, 4, 0, 3, 1, 4]] = 0
r[[1, 4, 5], 5] = 100
q[[1, 4], 5] = 100
print(r)
gama = 0.8
j = 0
for i in range(10):
    # y_index = random.sample(indices, 1)[0]
    # x_index = random.sample(indices, 1)[0]
    y_index = 0
    x_index = 0
    j = 0
    while True:
        mask = r[y_index] != -1
        mask1 = mask.nonzero()
        x_index_1 = torch.randint(0, mask1.size(0), size=(1,))[0]
        x_index = mask1[x_index_1][0].item()
        print("indices", y_index, x_index)

        if r[y_index, x_index] == 100:
            print(j, r[y_index, x_index], y_index, x_index)
            print(q)
            break
        else:
            q[y_index, x_index] = torch.max(q[x_index]) * gama
            y_index = x_index

        j += 1
