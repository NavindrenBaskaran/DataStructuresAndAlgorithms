import time 

def benchmark():
    array = [11122] * 100000000000
    time0 = time.time()
    len(array)
    time1 = time.time()

    print time0
    print time1

benchmark()
