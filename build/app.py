import os
import codecs
import binascii
import random 


def encrypt(plaintext, key):
    print("-------- Encryption --------")
    print("Key: " + key)
    ciphertext = ""

    #Checking the length of both key and plaintext
    if(len(key) != len(plaintext)):
      print("error: length is incorrect!")
    else:
      for i in range(len(plaintext)):
        #XOR the plaintext and secret key
        c = ord(plaintext[i]) ^ ord(key[i])
        #Setting the length of the encryption to that of the keys 32
        d = "{:01x}".format(c)
        ciphertext += d
      #writing too result file
      c_file = open("./data/ciphertext.txt", "w")
      c_file.write(ciphertext)
      c_file.close()
      print("Encrypted string: " + ciphertext)

# Used to get text from each corresponding file
key = open("./data/key.txt", "r")
key = key.read()
plaintext = open("./data/plaintext.txt", "r")
# Converting plaintext to binary 
plaintext = ''.join(format(ord(x), '08b') for x in plaintext.read())

#Instantiating the function
encrypt(plaintext,key)



def decrypt(ciphertext, key):
    print ("-------- Decryption --------")
    decrypted = ""
    msg = codecs.decode(ciphertext, 'UTF-8')

    if(len(key) != len(plaintext)):
      print("error: length is incorrect!")
    else: 
      for i in range(len(msg)):
        #XOR 
        c =  ord(msg[i]) ^ ord(key[i])
        #Setting the length of the encryption to that of the keys 32
        d = "{:01x}".format(c)
        decrypted += d
      result = int(decrypted, 2)
      #Converting binary to plaintext
      result = binascii.unhexlify('%x' % result)
      #removing the leading b from conversion to normal plaintext
      result = result.decode('utf-8')
      #writing too result file
      r_file = open("./data/result.txt", "w")
      r_file.write(result)
      r_file.close()
      print ("Decrypted string: " + str(result))

# Used to get text from each corresponding file
ciphertext = open("./data/ciphertext.txt", "r")
ciphertext = ciphertext.read()
#Encoding the ciphertext to readable UTF-8
ciphertext = ciphertext.encode(encoding='UTF-8')
key = open("./data/key.txt", "r")
key = key.read()
decrypt(ciphertext, key)

def keyGen():
    security_key = ""
    #where i take in input from user
    security_param = input("Please enter security parameter k: ") 

    #ensuring that the user input meets qaulified amount
    if(int(security_param) >= 1 and int(security_param) <= 128):
      for i in range(int(security_param)):
        #generation a random key
        key = str(random.randint(0, 1))
        temp = key
        security_key += temp 
      #writing to newkey file
      sk_file = open("./data/newkey.txt", "w")
      sk_file.write(security_key)
      sk_file.close()
      print("New security key: " + security_key)
    else:
      print("Invalid Security Param") 

keyGen()


