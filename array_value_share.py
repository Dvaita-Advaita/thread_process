import multiprocessing



def sq(arr,result,v):
    v.value = 5.48
    for i in range(len(arr)):
        result[i] = arr[i] ** 2


arr = [1,2,3,4,5]

v = multiprocessing.Value('d',0.0)
result = multiprocessing.Array('i',5)
p1 = multiprocessing.Process(target=sq,args=(arr,result,v))
p1.start()
p1.join()

print(v.value)
print(result[:])







