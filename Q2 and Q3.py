# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:39:00 2017
@author: Wei-Ming Weng (2305670)
"""
import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import matplotlib.pylab as matplt

#Part 1
#https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
#https://stackoverflow.com/questions/18644166/how-to-manipulate-wav-file-data-in-python
rate,data = wavfile.read("Q3.wav")

#Part 2
taxis=np.linspace(0,len(data)/rate,len(data))
plt.subplot(211)
matplt.title('Time Domain')
matplt.xlabel('time(s)')
matplt.ylabel('amplitude')
plt.plot(taxis,data)
#Fourier transform
dataf=np.fft.fft(data)
faxis=np.linspace(0,rate,len(dataf))
plt.subplot(212)
matplt.title('Frequency Domain')
matplt.xlabel('frequency(Hz)')
matplt.ylabel('amplitude')
plt.plot(faxis,abs(dataf))

#Part 3
#Get rid of DC components
k0=int(len(dataf)/rate*50)
dataf[0:k0+1]=0#0~50Hz removed
dataf[len(dataf)-k0:len(dataf)]=0#mirror
#enhance the sound from 2kHz~5Hz
amplify=10
k1=int(len(dataf)/rate*2000)
k2=int(len(dataf)/rate*5000)
dataf[k1:k2+1]=amplify*dataf[k1:k2+1]#amplifing the amplitudes
dataf[len(dataf)-k2:len(dataf)-k1]=amplify*dataf[len(dataf)-k2:len(dataf)-k1]#mirror
#reversing the fft
data_clean=np.fft.ifft(dataf)
data_clean=np.real(data_clean)
#Normalize the data_clean
data_clean=np.float32(data_clean/np.max(np.abs(data_clean)))
wavfile.write('answer_to_Q3.wav',44100,data_clean)









