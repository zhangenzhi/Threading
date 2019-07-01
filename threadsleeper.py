import threading
from time import ctime,sleep
#thread is using for synchronous,but won't spead up computing.
def loop(nloop,nsec):
    print("start loop",nloop,"at:",ctime())
    # sleep(nsec)
    i=0
    while i!=nsec:
        i +=1
    print("down loop",nloop,"at:",ctime())

loops = [400000000,400000000]
def main():
    print("Start at:",ctime())

    threads = []
    nloops = range(len(loops))

    for i in nloops:
        thread = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(thread)
    
    for thd in threads: # start thread but not run
        thd.start()

    for thd in threads: # wait for all thread finish
        thd.join()
    
    print("All down at:",ctime())


if __name__ == "__main__":
    main()