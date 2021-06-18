# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:25:33 2021

@author: Alexander Vining
"""
#packages from FLIR software development
import fnv
import fnv.reduce
import fnv.file 

import os
import datetime as dt

#%%
#set up text file for writing metadata
os.chdir("C:\\Users\\avining\\Documents\\Balsa_Spatial_Analysis\\DOCS")
metadata_file = open("video_file_timestamp_metadata_cam2.txt", "w") #create seperate files for cam1 and cam2, run loop once for each
#%%
#get timestamp of first and last frame in every file
os.chdir("F:\\BCI Ochroma Cam2") #external hard drive with thermal videos must be attached to the F Drive. Be sure to rename for each run of loop
os.listdir()
for folder in os.listdir():
    print("evaluating " + folder)
    os.chdir(folder)
    metadata_file.write("Folder: " + folder + "\n\n")
    year = int(folder[0:4]) #gets year from folder name, used to convert .seq timestamps
    
    for file in os.listdir():
        print("getting file " + file)
        im = fnv.file.ImagerFile(file)
        
        #get start time
        im.get_frame(0) #sets reference frame of im object to the first frame
        start_time = im.frame_info[0]['value'] #first element of frame_info object (index 0) is "Time", which holds name, value, unit, and type
        
        start_timestamp = dt.datetime(year, 1,1) + dt.timedelta(days = int(start_time[:3]) -1, #first three characters of timestamp give days since start of year. Subtract one because this number will be added to the 1st (one day already counted)
                                                     hours = int(start_time[4:6]),
                                                     minutes = int(start_time[7:9]),
                                                     seconds = int(start_time[10:12]),
                                                     microseconds = int(start_time[13:])) 
        metadata_file.write("File: " + file + "\n" + "start = " + start_timestamp.strftime("%Y-%m-%d_%H-%M-%S-%f") + "\n")
        
        #get end time
        im.get_frame(im.num_frames - 1) #set frame reference attribute to last frame
        end_time = im.frame_info[0]['value'] #first element of frame_info object (index 0) is "Time", which holds name, value, unit, and type
        
        end_timestamp = dt.datetime(year, 1,1) + dt.timedelta(days = int(end_time[:3]) -1, #first three characters of timestamp give days since end of year. Subtract one because this number will be added to the 1st (one day already counted)
                                                     hours = int(end_time[4:6]),
                                                     minutes = int(end_time[7:9]),
                                                     seconds = int(end_time[10:12]),
                                                     microseconds = int(end_time[13:])) 
        metadata_file.write("end = " + end_timestamp.strftime("%Y-%m-%d_%H-%M-%S-%f") + "\n\n")
        
    os.chdir("..")
    
metadata_file.close()
    
    
    

