from numpy import genfromtxt
import os
import numpy as np
import bct.nbs as nbs

''' 
list = os.listdir("followup_ad")
ad_data =  np.empty((90,90,len(list) ) )   
for index in range(len(list)):
#for file_name in list:      
    ad_data[:,:,index] = genfromtxt('followup_ad/' + list[index], delimiter=',')


list = os.listdir("followup")
control_data =  np.empty((90,90,len(list) ) )   
for index in range(len(list)):
#for file_name in list:      
    control_data[:,:,index] = genfromtxt('followup/' + list[index], delimiter=',')

'''
list = os.listdir("baseline_ad")
ad_data =  np.empty((90,90,len(list) ) ) 
for index in range(len(list)):
#for file_name in list:    
    ad_data[:,:,index] = genfromtxt('baseline_ad/' + list[index], delimiter=',')

print np.shape(ad_data)
 
list = os.listdir("baseline")
control_data =  np.empty((90,90,len(list) ) )   
for index in range(len(list)):
#for file_name in list:      
    control_data[:,:,index] = genfromtxt('baseline/' + list[index], delimiter=',')

thresh = 2.3
#pval,adj,_ = nbs.nbs_bct( control_data, ad_data, thresh, k=1000, tail='both', paired=False)
#print np.sum(adj) 
#np.savetxt("foo_2.3mat_ff.edge", adj, delimiter=" ")
