from multiprocessing import Pool,TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == "__main__":

    pool = Pool(processes = 4) 

    print(pool.map(f,range(10)))

    for i in pool.imap_unordered(f,range(10)):
        print(i)
    

    res = pool.apply_async(f,(20,))
    print(res.get(timeout = 1 ))