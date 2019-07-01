from multiprocessing import Process
from time import ctime
def f(name,num):
    print(name," start at: ",ctime())
    i = 0
    while i!= num:
        i+=1
    print(name," down at: ",ctime())

if __name__ == "__main__":

    print("All start at:",ctime())

    pool = []
    p_num = 3
    for i in range(p_num):
        pool.append(Process(target=f,args=[i,400000000]))
        pool[i].start()
        
    for p in pool:
        p.join()

    print("All down at:",ctime())