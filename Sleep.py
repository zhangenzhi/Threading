from time import ctime,sleep

def loop0():
    print("Loop 0 start at",ctime())
    sleep(4)
    print("Loop 0 down at",ctime())

def loop1():
    print("Loop 1 start at",ctime())
    sleep(2)
    print("Loop 1 down at",ctime())

def main():
    print("start at",ctime())
    loop0()
    loop1()
    print("All down at",ctime())

if __name__ == "__main__":
    main()