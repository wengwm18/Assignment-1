# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:39:00 2017

@author: Wei-Ming Weng (2305670)
"""

import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import struct
from scipy import sparse
from scipy.sparse.linalg import spsolve
import peakutils


#https://stackoverflow.com/questions/15576798/create-32bit-float-wav-file-in-python

#baseline correction
#https://zanran_storage.s3.amazonaws.com/www.science.uva.nl/ContentPages/443199618.pdf

def baseline_als(y, lam, p, niter=10):                                                                        

    s  = len(y)                                                                                               
    # assemble difference matrix                                                                              
    D0 = sparse.eye( s )                                                                                      
    d1 = [np.ones( s-1 ) * -2]                                                                             
    D1 = sparse.diags( d1, [-1] )                                                                             
    d2 = [np.ones( s-2 ) * 1]                                                                             
    D2 = sparse.diags( d2, [-2] )                                                                             

    D  = D0 + D2 + D1                                                                                         
    w  = np.ones( s )                                                                                         
    for i in range( niter ):                                                                                  
        W = sparse.diags( [w], [0] )                                                                          
        Z =  W + lam*D.dot( D.transpose() )                                                                   
        z = spsolve( Z, w*y )                                                                                 
        w = p * (y > z) + (1-p) * (y < z)                                                                     

    return z




"""
def float32_wav_file(sample_array, sample_rate):
  byte_count = (len(sample_array)) * 4  # 32-bit floats
  wav_file = ""
  # write the header
  wav_file += struct.pack('<ccccIccccccccIHHIIHH',
    'R', 'I', 'F', 'F',
    byte_count + 0x2c - 8,  # header size
    'W', 'A', 'V', 'E', 'f', 'm', 't', ' ',
    0x10,  # size of 'fmt ' header
    3,  # format 3 = floating-point PCM
    1,  # channels
    sample_rate,  # samples / second
    sample_rate * 4,  # bytes / second
    4,  # block alignment
    32)  # bits / sample
  wav_file += struct.pack('<ccccI',
    'd', 'a', 't', 'a', byte_count)
  for sample in sample_array:
    wav_file += struct.pack("<f", sample)
  return wav_file
"""

#Part 1
#https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
#https://stackoverflow.com/questions/18644166/how-to-manipulate-wav-file-data-in-python
rate,data = wavfile.read("Firstattempt.wav")
print (rate)
#Part 2
data_value=data[:,1]
#plt.plot(data_value)
#baseline correction
"""
z=baseline_als(data_value, 10000000000, 0.1, niter=10)
data_value=data_value-z
"""

#Fourier transform
dataf=np.fft.fft(data_value)
#plt.plot(abs(dataf))
print(len(dataf))
faxis=np.linspace(0,rate,len(dataf))
#plt.plot(faxis,abs(dataf))
#It is mirrored ,somehow correct

#Part 3
#Since we know that human voices lays around 2~5kHz,and the recording only has houman voice in it,
#By deleting the frequencies that arent in this region to enhance the voice 
#It is common for data to have an undesired baseline. 
#https://pythonhosted.org/PeakUtils/tutorial_a.html
#First attempt
k1=int(len(dataf)/rate*1000)
k2=int(len(dataf)/rate*5000)
print(k1)
print(k2)


#trying to found the average background noise and subtract them
"""
noise=np.average(dataf[100000:100001])
print('noise=',noise)
print('dataf[0]=',dataf[100000])
for i in range (len(dataf)):
    dataf[i]=dataf[i]-noise
print('dataf[0]=',dataf[100000])
plt.plot(abs(dataf))
"""
#plt.plot(faxis,abs(dataf))
#dataf[k2+1:len(dataf)-k2]=0
#Justify the cutoff frequency


#enhance the human sound
amplify=10
dataf[k1:k2+1]=amplify*dataf[k1:k2+1]#amplifing the amplitudes
dataf[len(dataf)-k2:len(dataf)-k1+1]=amplify*dataf[len(dataf)-k2:len(dataf)-k1+1]#mirror
#plt.plot(faxis,abs(dataf))
#justify centre frequency and bandwidth



#reversing the fft
data_clean=np.fft.ifft(dataf)
data_clean=np.real(data_clean)
#Normalizing the data_clean in range 1~-1 to throw into the formula
"""
max_data=np.max(data_clean)
min_data=np.min(data_clean)
for i in range (len(data_clean)):
    data_clean[i]=np.float32(2*(data_clean[i]-min_data)/(max_data-min_data)-1)"""
"""
z=baseline_als(data_clean, 10000000000, 0.1, niter=10)
data_clean=data_clean-z


base=peakutils.baseline(data_clean,100)
data_clean=data_clean-base
""" 
#plt.plot(base)


data_clean=np.float32(data_clean/np.max(np.abs(data_clean)))
wavfile.write('finalresult.wav',44100,data_clean)


#plt.plot(data_clean)








