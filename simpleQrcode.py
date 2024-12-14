## qrcode generation

import PyQRCode

name = 'romio'
k = pyqrcode.create(name) 
k.png('test.png',scale =10)


import os
os.system('test.png')