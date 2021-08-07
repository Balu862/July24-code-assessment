import multiprocessing,logging
logging.basicConfig(filename='Oddeven.log',level=logging.DEBUG)
try:
    def odd(getlist):
        for i in getlist:
            if i%2!=0:
                print("odd ",i)
                logging.info ("odd number is added")
    def even(getlist):
        for i in getlist:
            if i%2==0:
                print("even ",i)
                logging.info ("Even number is added")
    if __name__ == "__main__":
        mylist=list(map(int,input("Please enter the numbers in Straight line with space ").split()))
        p1=multiprocessing.Process(target=even,args=(mylist,))
        p2=multiprocessing.Process(target=odd,args=(mylist,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("..........")
except ValueError:
    logging.error("please check whether the input has to written in int or string")
    print("please check whether the input has to written in int or string")
except IndexError:
    logging.error("your value is not in the index ")
    print("your value is not in the index ")
except KeyboardInterrupt:
    logging.error("terminal is interupted due to CTRL+C")
    print("terminal is interupted due to CTRL+C")
except:
    print("Something is Error please check it")
    logging.error("Error has been occured")