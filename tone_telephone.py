# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 02:50:06 2017

@author: Wei-Ming Weng (2305670)
"""

import numpy as np
import matplotlib.pyplot as plt
import peakutils
#checking the datas in the moodle
#http://www.eecs.umich.edu/courses/eecs206/public/lab/lab7/lab7.pdf

samplef=1000
#We know that DTMF frequencies are 697, 770, 852, 941, 1209, 1336, 1477
#soundf取一半就好了
def analogf_detector(soundf):
    samplef=1000#due to the assighment request   
    threshold=2
    resolution=0.001
    goal=np.array([0,0,0,0,0,0,0,0])
    for i in range(int(threshold/resolution)):
        if(threshold<soundf[int(303/samplef*len(soundf))] and goal[1]==0):
            print('has analog frequency 697 Hz')
            goal[0]=goal[0]+1
            goal[1]=goal[1]+1
        if(threshold<soundf[int(230/samplef*len(soundf))] and goal[2]==0):
            print('has analog frequency 770 Hz')
            goal[0]=goal[0]+1
            goal[2]=goal[2]+1
        if(threshold<soundf[int(148/samplef*len(soundf))] and goal[3]==0):
            print('has analog frequency 852 Hz')
            goal[0]=goal[0]+1
            goal[3]=goal[3]+1
        if(threshold<soundf[int(59/samplef*len(soundf))] and goal[4]==0):
            print('has analog frequency 941 Hz')
            goal[0]=goal[0]+1
            goal[4]=goal[4]+1
        if(threshold<soundf[int(209/samplef*len(soundf))] and goal[5]==0):
            print('has analog frequency 1209 Hz')#####################################3
            goal[0]=goal[0]+1
            goal[5]=goal[5]+1
        if(threshold<soundf[int(336/samplef*len(soundf))] and goal[6]==0):
            print('has analog frequency 1336 Hz')
            goal[0]=goal[0]+1
            goal[6]=goal[6]+1
        if(threshold<soundf[int(477/samplef*len(soundf))] and goal[7]==0):
            print('has analog frequency 1477 Hz')
            goal[0]=goal[0]+1
            goal[7]=goal[7]+1
        if(goal[0] != 2):
            threshold=threshold-resolution
        elif(goal[0]==2):
            break
        
    
    
      
#importing the data from moodle
sound_track_0 = np.loadtxt('ending_0.dat')
time=sound_track_0[:,0]
sound=sound_track_0[:,1]
#plt.plot(sound,linewidth=0.5)

#do FFT to all the imported data 
#manually cutting the data
soundf_0=np.fft.fft(sound[1900:2200])
soundf_1=np.fft.fft(sound[2300:2500])
soundf_2=np.fft.fft(sound[2700:2900])
soundf_3=np.fft.fft(sound[4100:4300])
soundf_4=np.fft.fft(sound[4500:4700])
soundf_5=np.fft.fft(sound[4800:5100])
soundf_6=np.fft.fft(sound[6200:6400])
soundf_7=np.fft.fft(sound[6600:6800])
soundf_8=np.fft.fft(sound[7000:7250])
soundf_9=np.fft.fft(sound[8200:8400])
soundf_10=np.fft.fft(sound[8500:8700])

print('0 part has')
analogf_detector(abs(soundf_0))
print('1 part has')
analogf_detector(abs(soundf_1))
print('2 part has')
analogf_detector(abs(soundf_2))
print('3 part has')
analogf_detector(abs(soundf_3))
print('4 part has')
analogf_detector(abs(soundf_4))
print('5 part has')
analogf_detector(abs(soundf_5))
print('6 part has')
analogf_detector(abs(soundf_6))
print('7 part has')
analogf_detector(abs(soundf_7))
print('8 part has')
analogf_detector(abs(soundf_8))
print('9 part has')
analogf_detector(abs(soundf_9))
print('10 part has')
analogf_detector(abs(soundf_10))






"""
plt.plot(abs(soundf_0))
"""
#testing the function whether it works or not
"""
print('ending_0 data ')
analogf_detector()
"""
#Attempt2
#try np.convolution
"""
M=6
filter_697=np.zeros(M)
for k in range(M):
    filter_697[k]=np.sin(2*np.pi*697*k/samplef)
result_697=np.convolve(filter_697,sound_track_1)
resultf_697=np.fft.fft(result_697)
#plt.plot(resultf_697)

filter_770=np.zeros(M)
for k in range(M):
    filter_770[k]=np.sin(2*np.pi*770*k/samplef)
result_770=np.convolve(filter_770,sound_track_1)
resultf_770=np.fft.fft(result_770)
plt.plot(resultf_770)

filter_852=np.zeros(M)
for k in range(M):
    filter_852[k]=np.sin(2*np.pi*852*k/samplef)
result_852=np.convolve(filter_852,sound_track_1)
resultf_852=np.fft.fft(result_852)
#plt.plot(resultf_852)

filter_941=np.zeros(M)
for k in range(M):
    filter_941[k]=np.sin(2*np.pi*941*k/samplef)
result_941=np.convolve(filter_941,sound_track_1)
resultf_941=np.fft.fft(result_941)
#plt.plot(resultf_941)

filter_1336=np.zeros(M)
for k in range(M):
    filter_1336[k]=np.sin(2*np.pi*1336*k/samplef)
result_1336=np.convolve(filter_1336,sound_track_1)
resultf_1336=np.fft.fft(result_1336)
#plt.plot(resultf_1336)

filter_1209=np.zeros(M)
for k in range(M):
    filter_1209[k]=np.sin(2*np.pi*1209*k/samplef)
result_1209=np.convolve(filter_1209,sound_track_1)
resultf_1209=np.fft.fft(result_1209)
#plt.plot(resultf_1209)

filter_1477=np.zeros(M)
for k in range(M):
    filter_1477[k]=np.sin(2*np.pi*1477*k/samplef)
result_1477=np.convolve(filter_1477,sound_track_1)
resultf_1477=np.fft.fft(result_1477)
#plt.plot(resultf_1477)
"""



