import numpy as np
from scipy.stats import bernoulli as bn


# call = np.array([[1,2,3],[4,5,6],[7,8,9]]).reshape((1, 3, 3))
# print(call)
# print(call[:, :, :-1])
# matrix=np.apply_along_axis(sum, axis=-1, arr=call[:, :, :-1])
# print(matrix)





pools_nb=8 # maxium to be pools_size*2
# Yes, but only because we want every sample being part of 2 pools (design constraint)
pools_size=4
size=(pools_size*pools_size)
shape: tuple = (pools_size, pools_size)
dim=2

design: np.ndarray = np.zeros((pools_nb, size), dtype=int)
print(design)

for i in range(int(pools_nb/dim)): #0 1 2 3
    j = i * pools_size
    design[i, j:j+pools_size] = [1]*pools_size
print(design.shape)

for i in range(int(pools_nb/dim), pools_nb): #4 5 6 7
    j = i - pools_size              #0 1 2 3
    design[i,
        [j+k*pools_size for k in range(pools_size)]] = 1
print(design)
scores=[[ 3, 9, 15,3, 9, 15,3, 9, 15,3, 9, 15,3, 9, 15,3]]
pooled_gt = np.dot(design,np.transpose(scores)).reshape((1, 8, 1))
print(pooled_gt.shape)
pooled_gt = np.broadcast_to(pooled_gt, (1, 8, 3))
print(pooled_gt.shape)

# cache = (design[i, :].reshape(shape) == False)
# print(cache)


# x = np.ones((1, pools_nb, 1))
# y = np.asarray([-1, -1, 0])
# b = np.broadcast(x, y) #(x*y)
# p = np.empty(b.shape)
# print(x*y)
# p.flat = [u * v for (u, v) in b]
# for i in p.flat:
#     print(i)

# flag: bool = bn.rvs(p=0.01, size=1)
# print(flag)