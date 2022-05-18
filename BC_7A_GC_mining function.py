# -*- coding: utf-8 -*-
"""BC_7A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G3_DFBUr9N4Kkne63AqPEd_tgho0X8NO
"""

import hashlib

def sha256(message):
 return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
   assert difficulty >= 1
   prefix = '1' * difficulty
   for i in range(1000):
      digest = sha256(str(hash(message)) + str(i))
      if digest.startswith(prefix):
         print ("after " + str(i) + " iterations found nonce: "+ digest)
      return digest

mine ("test message", 2)