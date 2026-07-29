import multiprocessing


def sq(arr):
    for num in arr:
        print(num ** 2)

def cube(arr):
    for num in arr:
        print(num ** 3)

arr = [1,2,3,4,5]

p1 = multiprocessing.Process(target=sq,args=(arr,))
p2 = multiprocessing.Process(target=cube,args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()

print("Done")

