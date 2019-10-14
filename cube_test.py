# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:24:54 2017

@author: user
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:04:55 2017

@author: user
"""
import numpy as np
import scipy.io.wavfile as wavfile
#import data
rate,data = wavfile.read("Q3.wav")
dataf=np.fft.fft(data)
#setup variable
high_pass_f1=800
#follow the given .cpp file and adjust it to python style
dataf_part1=dataf[0:int(len(dataf)*(high_pass_f1/rate))]
dataf_part2=dataf[int(len(dataf)*(high_pass_f1/rate)):len(dataf)-1-int(len(dataf)*(high_pass_f1/rate))]
dataf_part3=dataf[len(dataf)-1-int(len(dataf)*(high_pass_f1/rate)):len(dataf)]
coefficient=np.max(np.abs(dataf_part2))
#normalized
dataf_part2_normalized=dataf_part2/coefficient
dataf_cube=np.power(dataf_part2_normalized,3)
dataf_combine=np.hstack((dataf_part1,dataf_part2+dataf_cube,dataf_part3))
data_result=np.fft.ifft(dataf_combine)
data_result=np.real(data_result)
data_clean=np.float32(data_result/np.max(np.abs(data_result)))
wavfile.write('answer_to_Q5_cube.wav',44100,data_clean)
#cube succeed

















































