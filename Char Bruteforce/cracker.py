'''
Simple ZIP cracker with BruteForce Attack
This will work only when the password is Alphabetical Character
If the password is too long this take more time to crack the password
'''

import zipfile

chlist   = 'abcdefghijklmnopqrstuvwxyz'           #The character list 
finish = []

for current in range(4):
    a = [i for i in chlist]
    for x in range(current):
        a = [y + i for i in chlist for y in a]
    finish = finish + a

z = zipfile.ZipFile('Your zip file with extension')                #Add the locked zip file name

tries = 0

for word in finish:
    try:
        tries += 1
        z.setpassword(word.encode('ascii'))
        z.extract('Content inside zipfile with extension')         #Add the content names with extension. 
                                                                   #If you doesn't know the content inside Zip add a env file as black with func name
        print( f"Tries : {tries} and Password : {word}")
        break
    except:
        pass
