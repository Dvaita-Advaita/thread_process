import time
import threading

def sq(arr):
    for num in arr:
        time.sleep(0.2)
        print(num ** 2)

def cube(arr):
    for num in arr:
        time.sleep(0.2)
        print(num ** 3)

# Without threading
t1 = time.time()
arr = [1,2,3,4,5]
sq(arr)
cube(arr)

print("time taken without threading",time.time()-t1)

# With threading
t2 = time.time()
t_s = threading.Thread(target=sq,args=(arr,))
t_c = threading.Thread(target=cube,args=(arr,))

t_s.start()
t_c.start()

t_s.join()
t_c.join()

print("time taken with threading",time.time()-t2)