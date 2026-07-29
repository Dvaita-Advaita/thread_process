import multiprocessing

# Two process cannot share data

result = []

def sq(arr):
    for num in arr:
        result.append(num ** 2)
    print("inside process",result)

arr = [1,2,3,4,5]

p1 = multiprocessing.Process(target=sq,args=(arr,))
p1.start()
p1.join()

print("outside,data not shared to global process",result)

# Data Sharing using Queue(First In First Output)

def sq(arr,q):
    for i in range(len(arr)):
        q.put(arr[i]**2)

q = multiprocessing.Queue()

p2 = multiprocessing.Process(target=sq,args=(arr,q))
p2.start()
p2.join()

while q.empty() is False:
    print("data sharing from inside to otside",q.get())

