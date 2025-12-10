import numpy as np  
'''
arr=np.array(['a','2','3'], dtype='a')
print(arr)
print(arr.dtype)

arr=np.array(["apple","banana","cherry"])
print(arr.dtype)
'''
arr=np.array([1.1,2.2,3.3])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)
arr=np.array([1,0,3])
newarr=arr.astype('f')
print(newarr)
print(newarr.dtype)