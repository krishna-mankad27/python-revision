import threading
import time

def walkdog(firstname,lastname):
    time.sleep(8)
    print(f"you finish walking {firstname}{lastname}")
def takeoutrash():
    time.sleep(3)
    print("you took the trash")

def getmail():
    time.sleep(5)
    print("got mail")

chore1 = threading.Thread(target = walkdog,args= ("scoby","dooo"))
chore1.start()
chore2 = threading.Thread(target=takeoutrash)
chore2.start()
chore3 = threading.Thread(target=getmail)
chore3.start()
chore1.join()
chore2.join()
chore3.join()
print("all chores are complete")