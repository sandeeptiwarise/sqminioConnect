import logging
import traceback
from minio import Minio
import os
#from minio.error import ResponseError, BucketAlreadyExists


# Fucntion to return instances of minio client
def getMinioClient(access, secret):
    return Minio(
        'localhost:9000',
        access_key=access,
        secret_key=secret,
        secure=False
    )
     
if __name__ == '__main__':
    # Creating object of of MinioClient 
    minioClient = getMinioClient('sqtestkey','sqtestsecret')

    # Creating a new bucket in our minioClient
    #if(not minioClient.bucket_exists('sqtestbucket')):
    #    try:
    #        minioClient.make_bucket('sqtestbucket')
    #    except ResponseError as Indentifier:
    #        raise
    
    # reach storage
    try:
        if not minioClient.bucket_exists("sqtestbucket"):
            # make bucket
            minioClient.make_bucket('sqtestbucket')
            logging.debug("Bucket Object storage got created and is connected")
    except:
        # raise error if storage not reachable
        logging.critical("Bucket Object storage not reachable")

    # Now go to terminal MinIOProject/sqminioConnect$ and execute the script to get 
    # a new bucket in minio - python3 sqminioConnect.py

    # Go To - sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev/mdata$ ls
    # sqtestbucket - bucket got created

    # sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev$ sudo chmod -R 757 /home/dev/mdata
    # [sudo] password for sandeepdevsys: 
    # sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev$ cd mdata
    # sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev/mdata$ touch test.txt

    # Upload test.txt named as sqminiotest.txt to sqtestbucket

    try:
        with open('/home/dev/mdata/test.txt','rb') as testfile:
            statdata = os.stat('/home/dev/mdata/test.txt')
            minioClient.put_object(
                'sqtestbucket',
                'sqminiotest.txt',
                testfile,
                statdata.st_size 

            )
            logging.critical("File got uploaded")
    except:
        # raise error if file is not uploaded
        logging.critical("File not uploaded")
        traceback.print_exc() 
    
    # (venv) sandeepdevsys@sandeepdevsys-Lenovo-G50-80:~/Documents/Project/MinIOProject/sqminioConnect$ python3 sqminioConnect.py
    # sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev/mdata$ cd sqtestbucket/
    # sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev/mdata/sqtestbucket$ ll

    
    # ## Remove the file object from bucket
    try:
        minioClient.remove_object('sqtestbucket','sqminiotest.txt')
        logging.critical("File got deleted")
    except:
        # raise error if file is not deleted
        logging.critical("File not deleted")
        traceback.print_exc() 

    # (venv) sandeepdevsys@sandeepdevsys-Lenovo-G50-80:~/Documents/Project/MinIOProject/sqminioConnect$ python3 sqminioConnect.py
    # sandeepdevsys@sandeepdevsys-Lenovo-G50-80:/home/dev/mdata/sqtestbucket$ ll

    # # Removing the bucket for the user created 
    try:
        minioClient.remove_bucket('sqtestbucket')
        logging.critical("Bucket Got Deleted")
    except:
        # raise error if bucket is not
        logging.critical("Bucket not deleted")
        traceback.print_exc() 

    # (venv) sandeepdevsys@sandeepdevsys-Lenovo-G50-80:~/Documents/Project/MinIOProject/sqminioConnect$ python3 sqminioConnect.py
    
    
