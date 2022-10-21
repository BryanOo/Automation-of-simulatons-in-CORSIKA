import pandas as pd
import numpy as np
import math
import fnmatch
from io import open
import os
from subprocess import call

#######################HEADER########################
###----> FIRST PART OF THE PROGRAM SIMULATES USING CORIKA FOR A RANGE OF ENERGIES.
###----> VARIABLES DEFINITIONS 
###----> NSHOWS => number of showers per simulation
###----> ENERGIES => range of energies
###----> PARTICLES => type of particles to simulation

class simulation:
    bitInformation = "Simulations are realise using one energy or using an range of energies"
    def __init__(self, E0, theta, phi) -> bitInformation:
        self.__E0 = E0
        self.__theta = theta
        self.__phi = phi
    def inputFile(self, iFile):
        with open("{}".format(iFile), "r") as text1:
            input = text1.read()
        return input
"""VARIABLES DECLARATION"""
nSimu = str(input("Insert the number of simulation: ")) ###Number of simulation
nameFolder = "Run{}".format(nSimu)
os.system("mkdir ../Simulations/{}".format(nameFolder))
def index():
    indexCity = np.array(places.index)
    for i in indexCity:
        os.system("mkdir ../Simulations/{}/{}".format(nameFolder, i))
places = pd.read_csv("Places_data.txt", header = 0, delim_whitespace=True)
index() ### FILE CONTAINS THE INFORMATION ABOUT THE SITES
particles = np.array([1, 14, 402, 1407, 5226])
energies = np.concatenate((np.arange(0.1, 10, 0.3), np.power(10, np.arange(1, 5 + 0.025, 0.025))))
if __name__ == "main":
    NSHOW = int(input("Insert the number of shower per runner: ")) ###NUMER OF SHOWERS PER RUNNER
    ##################OPENING AND READING OF ALL-INPUTS FILE##################
    with open("all-inputs.txt", "r") as text1:
        input = text1.read()  ##FILE AT WHICH WE'LL CHANGE PARAMETERS OF THE SHOWERS 
    def SEED_HAD(): ## GENERATOR TO SEED FOR THE HADRONIC PART
        SEEDH = 1
        counterh = 1
        while counterh <= places["Height"].size*particles.size*energies.size:
            yield (SEEDH)
            SEEDH += 2
            counterh += 1
    SEED_HAD = SEED_HAD()
    def SEED_EGS4(): ## GENERATOR TO SEED FOR THE ELECTROMAGNETIC PART
        SEEDE = 1
        countere = 1
        while countere <= places["Height"].size*particles.size*particles.size:
            yield (SEEDE*2)
            SEEDE += 1
            countere+=1
    SEED_EGS4=SEED_EGS4()
    ###########MAIN PART###########
    counter = 1
    for i,r,mx,mz in zip(places["Height"], np.array(places.index), places["MagnetX"], places["MagnetZ"]):
        for j in particles:
            os.system('mkdir ../Simulations/{}/{}/{}'.format(nameFolder, r, j))
            os.system('mkdir ../Simulations/{}/{}/{}/Binaries'.format(nameFolder, r, j))
            for l,m,n in zip(energies, SEED_HAD, SEED_EGS4):
                all_inputs = open('all-inputs{}'.format(counter), 'w')
                all_inputs.write(input.format(counter, NSHOW, j, l, l, m, n, i, mx, mz))
                all_inputs.close()
                os.system("./corsika77410Linux_QGSII_urqmd_thin <all-inputs{}> output{}.txt".format(counter,counter))
                os.system("rm all-inputs{}".format(counter))
                if counter <= 99:
                    if counter <= 9:
                        os.system("mv output{}.txt ../Simulations/{}/{}/{}/Binaries".format(counter, nameFolder, r, j))
                    else:
                        os.system("mv output{}.txt ../Simulations/{}/{}/{}/Binaries".format(counter, nameFolder, r, j))
                elif counter >= 100 and counter <= 999:
                    os.system("mv output{}.txt ../Simulations/{}/{}/{}/Binaries".format(counter, nameFolder, r, j))
                elif counter >= 1000 and counter <= 9999:
                    os.system("mv output{}.txt ../Simulations/{}/{}/{}/Binaries".format(counter, nameFolder, r, j))
                elif counter >= 10000 and counter <= 99999:
                    os.system("mv output{}.txt ../Simulations/{}/{}/{}/Binaries".format(counter, nameFolder, r, j))
                else:
                    os.system("mv output{}.txt ../Simulations/{}/{}/{}/Binaries".format(counter, nameFolder, r, j))
                counter += 1
    '---------------------CORSIKA READER----------------------------'
    with open('readpartExample.cc', 'r') as Text2:
        Reader = Text2.read()
    for i in np.arange(1,particles.size*particles.size*places["Height"].size+1):
        if i <= 99:
            if i <= 9:
                Corsika_reader = open('readpartExample{}.cc'.format(i), 'w')
                Corsika_reader.write(Reader.replace(":v", "DAT0000{}".format(str(i).zfill(2))))
            else:
                Corsika_reader = open('readpartExample{}.cc'.format(i), 'w')
                Corsika_reader.write(Reader.replace(":v", "DAT0000{}".format(i)))
        elif i >= 100 and i <= 999:
            Corsika_reader = open('readpartExample{}.cc'.format(i), 'w')
            Corsika_reader.write(Reader.replace(":v", "DAT000{}".format(i)))
        elif i>=1000 and i<=9999:
            Corsika_reader = open('readpartExample{}.cc'.format(i), 'w')
            Corsika_reader.write(Reader.replace(":v", "DAT00{}".format(i)))
        elif i >= 10000 and i <= 99999:
            Corsika_reader = open('readpartExample{}.cc'.format(i), 'w')
            Corsika_reader.write(Reader.replace(":v", "DAT0{}".format(i)))
        else:
            Corsika_reader = open('readpartExample{}.cc'.format(i), 'w')
            Corsika_reader.write(Reader.replace(":v", "DAT{}".format(i)))
