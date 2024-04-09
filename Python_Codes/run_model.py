# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:32:25 2023

@author: moritzw
"""
import shutil
import glob
import os


def run_model(nproc,pathres):
    # os.chdir(pathres)
    os.system('cd %s;  /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep --np %s --partmesh' %(pathres,str(nproc)))
    os.system('cd %s;  /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep  --np %s --prepall' %(pathres,str(nproc)))
    os.system('cd %s; mpirun -np %s /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/padcswan' %(pathres,str(nproc)))
    
    try: 
        os.system('taskkill /F /IM padcswan_SH.exe')
    except:
        print('ADCIRC  +  SWAN run finished succesfully')
    
    dir_list = glob.iglob(os.path.join(pathres, "PE0*"))
    for path in dir_list:
        if os.path.isdir(path):
            shutil.rmtree(path)
            
            
def run_ramp_model(nproc,pathres):
    # os.chdir(pathres)
    os.system('cd %s;  /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep --np %s --partmesh' %(pathres,str(nproc)))
    os.system('cd %s;  /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep  --np %s --prepall' %(pathres,str(nproc)))
    os.system('cd %s; mpirun -np %s /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/padcirc' %(pathres,str(nproc)))
    
    try: 
        os.system('taskkill /F /IM padcswan_SH.exe')
    except:
        print('ADCIRC  +  SWAN run finished succesfully')
        
    os.system('cp %sfort.67 %s' %(os.path.join(pathres + 'PE0000/'),pathres))
    
    dir_list = glob.iglob(os.path.join(pathres, "PE0*"))
    for path in dir_list:
        if os.path.isdir(path):
            shutil.rmtree(path)
            
            

def run_model_hotstart(nproc,pathres):
    # os.chdir(pathres)
    os.system('cd %s;  /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep --np %s --partmesh' %(pathres,str(nproc)))
    os.system('cd %s;  /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep  --np %s --prepall' %(pathres,str(nproc)))
    os.system('cd %s; /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep --np %s  --hotlocalize 67'%(pathres,str(nproc)))
    os.system('cd %s; /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/adcprep --np %s  --hotglobalize 67'%(pathres,str(nproc)))
    os.system('cd %s; mpirun -np %s /media/judith/10TB/ADCIRC55/adcirc_v55.01SH/padcswan' %(pathres,str(nproc)))
    
    try: 
        os.system('taskkill /F /IM padcswan_SH.exe')
    except:
        print('ADCIRC  +  SWAN run finished succesfully')
    
    dir_list = glob.iglob(os.path.join(pathres, "PE0*"))
    for path in dir_list:
        if os.path.isdir(path):
            shutil.rmtree(path)