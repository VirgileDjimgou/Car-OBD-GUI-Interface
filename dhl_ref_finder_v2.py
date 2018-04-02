#import urllib.request
import numpy as np
import os
import _thread
import time
import requests
import multiprocessing
import tkinter as tk
from timeit import default_timer as timer

import sys


def create_window():
    window = tk.Toplevel(root)

# init all global var ...

try:
    neg_images_link = 'https://nolp.dhl.de/nextt-online-public/de/search?piececode='
    t1_job = t1_actual =0
    t2_job = t2_actual =0
    t3_job = t3_actual =0
    t4_job = t4_actual =0
    t5_job = t5_actual =0
    t6_job = t6_actual =0
    t7_job = t7_actual =0
    t8_job = t8_actual =0


except Exception as e:
    print(str(e))

def ThreadSetupScalable(interval_ref):

    pic_num = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')
    print("number of Core this Computer  is : "+str(multiprocessing.cpu_count()))
    time.sleep(3)
    # Berechnung Thread Job
    job = int(round(interval_ref)/8) # durch anzahl von Threads = 8
    print(job)

    try:
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-1", 0, job) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-2", job+1, job*2 ) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-3", job*2 +1, job*3 ) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-4", job*3 +1, job*4) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-5", job*4 +1, job*5 ) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-6", job*5 +1, job*6) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-7", job*6 +1, job*7) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-8", job*7 +1, job*8) )


    except:
        print ("Error: unable to start thread")

    while(1):
        pass


def ThreadSetup(from_ , to_, ):
    interval = 0
    CoreNumber = 0
    print(interval)
    CoreNumber = multiprocessing.cpu_count()
    if (CoreNumber < 1):
        print("this Script cannot be processed with multiprocessing Option ...")
        print("the programm will be abort .....")
        time.sleep(5)
        sys.exit()
    else:
        print("number of Core this Computer  is : "+str(multiprocessing.cpu_count()))

    if(from_ < to_ ):
        interval = to_ - from_
    else:
        print ("you must enter a correct value .....the interval that you entered is not correct !")
        ###  stop the programm ...
        print("the programm will be abort .....")
        time.sleep(5)
        sys.exit()

    pic_num = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')
    time.sleep(3)
    # Berechnung Thread Job
    job = int(interval/8) # durch anzahl von Threads = 8
    print(job)

    try:
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-1", 0, job) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-2", job+1, job*2 ) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-3", job*2 +1, job*3 ) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-4", job*3 +1, job*4) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-5", job*4 +1, job*5 ) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-6", job*5 +1, job*6) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-7", job*6 +1, job*7) )
        _thread.start_new_thread( Thread_find_refInfos, ("Thread-8", job*7 +1, job*8) )

        ## special Thread  to refresh all Threads Informations of the console ....
        _thread.start_new_thread( Thread_find_refInfos, ("Thread_InfosPrinter") )
    except:
        print ("Error: unable to start Pool of thread")

    while(1):
        pass

def InfosTreadJob(ThreadName):
    print(ThreadName)

# define a function for the thread .
def Thread_find_refInfos(ThreadName , begin_ , to_):
    print("Start Thread " + ThreadName)
    time.sleep(3)
    pic_num = begin_
    for  i in range(begin_ , to_+1):

        try:
            print(ThreadName +" actually process  url : "+str(list_of_url[i]))
            #urllib.request.urlretrieve(str(list_of_url[i]), "neg/"+str(pic_num)+".jpg")
            r = requests.get("https://nolp.dhl.de/nextt-online-public/de/search?piececode=" + i)


        except Exception as e:
            print(str(e))


    print(ThreadName+ " Job finished .")


#store_raw_images()
#create_pos_n_neg()
ThreadSetup(200,500)
