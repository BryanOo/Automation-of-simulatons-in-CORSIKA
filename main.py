from io import open
import os
import numpy as np
from headerReader import *

contador = 1

for r in np.array(places.index):
    for j in particles:
        for l in energies:
            if contador <= 99:
                if contador <= 9:
                    os.system("./readpartExample{} DAT0000{} >> Data{}.txt".format(contador, str(contador).zfill(2), contador))
                    os.system("rm readpartExample{} readpartExample{}.cc".format(contador,contador))
                    os.system("mv DAT0000{} DAT0000{}.long ../Simulations/{}/{}/{}/Binaries".format(str(contador).zfill(2), str(contador).zfill(2), nameFolder, r, j))
                else:
                    os.system("./readpartExample{} DAT0000{} >> Data{}.txt".format(contador, contador, contador))
                    os.system("rm readpartExample{} readpartExample{}.cc".format(contador,contador))
                    os.system("mv DAT0000{} DAT0000{}.long ../Simulations/{}/{}/{}/Binaries".format(contador, contador, nameFolder, r, j))
            elif contador >= 100 and contador <= 999:
                os.system("./readpartExample{} DAT000{} >> Data{}.txt".format(contador, contador, contador))
                os.system("rm readpartExample{} readpartExample{}.cc".format(contador,contador))
                os.system("mv DAT000{} DAT000{}.long ../Simulations/{}/{}/{}/Binaries".format(contador, contador, nameFolder, r, j))
            elif contador >= 1000 and contador <= 9999:
                os.system("./readpartExample{} DAT00{} >> Data{}.txt".format(contador, contador, contador))
                os.system("rm readpartExample{} readpartExample{}.cc".format(contador,contador))
                os.system("mv DAT00{} DAT00{}.long ../Simulations/{}/{}/{}/Binaries".format(contador, contador, nameFolder, r, j))
            elif contador >= 10000 and contador <= 99999:
                os.system("./readpartExample{} DAT0{} >> Data{}.txt".format(contador, contador, contador))
                os.system("rm readpartExample{} readpartExample{}.cc".format(contador,contador))
                os.system("mv DAT0{} DAT0{}.long ../Simulations/{}/{}/{}/Binaries".format(contador, contador, nameFolder, r, j))
            else:
                os.system("./readpartExample{} DAT{} >> Data{}.txt".format(contador, contador, contador))
                os.system("rm readpartExample{} readpartExample{}.cc".format(contador,contador))
                os.system("mv DAT{} DAT{}.long ../Simulations/{}/{}/{}/Binaries".format(contador, contador, nameFolder, r, j))

            os.system("mv Data{}.txt ../Simulations/{}/{}/{}".format(contador, nameFolder, r, j))    
            contador += 1