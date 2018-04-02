import urllib.request
#import cv2
import numpy as np
import os
import _thread 
import time 

#neg_images_link = "" 
#neg_image_urls 

try:
   neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
   neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
   list_of_url = neg_image_urls.split('\n')

except Exception as e:
       print(str(e)) 
   

def ThreadSetup():

     pic_num = 1

     if not os.path.exists('neg'):
        os.makedirs('neg')

     #list_of_url.append("test")
     #print("number of Images is : "+str(list_of_url[0]))
     print("number of Images is : "+str(len(list_of_url)))
     time.sleep(3)
     # Berechnung Thread Job 
     job = int(round(len(list_of_url)/8)) # durch anzahl von Threads = 8
     print(job)

     try:
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-1", 0, job) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-2", job+1, job*2 ) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-3", job*2 +1, job*3 ) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-4", job*3 +1, job*4) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-5", job*4 +1, job*5 ) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-6", job*5 +1, job*6) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-7", job*6 +1, job*7) )
        _thread.start_new_thread( Thread_store_raw_images, ("Thread-8", job*7 +1, job*8) )


     except:
        print ("Error: unable to start thread")
        
     while(1):
          pass
    

# define a function for the thread ... url photo download 
def Thread_store_raw_images(ThreadName , begin_ , to_):
  
     print("Start Thread " + ThreadName)
     time.sleep(3)
     pic_num = begin_
     for  i in range(begin_ , to_+1):
   
          try:
               print(ThreadName +" download image at url : "+str(list_of_url[i]))
               print(ThreadName +" image number : "+str(i))

               urllib.request.urlretrieve(str(list_of_url[i]), "neg/"+str(pic_num)+".jpg")
               img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
               # should be larger than samples / pos pic (so we can place our image on it)
               resized_image = cv2.resize(img, (100, 100))
               cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
               pic_num += 1
				
          except Exception as e:
               print(str(e))  
				
				
     print(ThreadName+ " Job finished .") 
     if not os.path.exists('Thread Job finished :'+ThreadName):
        os.makedirs('Thread Job finished :'+ThreadName)

# define a function for the thread ... url photo download 
def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
    
    num_of_url = neg_image_urls.split('\n')
    print("number of Images is : "+str(len(num_of_url)))

    for i in neg_image_urls.split('\n'):
        try:
            print(i)

            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e)) 
            
def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line) 

#store_raw_images()
create_pos_n_neg()
#ThreadSetup()
