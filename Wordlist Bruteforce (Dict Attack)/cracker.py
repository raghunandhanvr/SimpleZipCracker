'''
Simple ZIP cracker with Dictonary Attack
This will work only when the password is inside your worlist
'''

import zipfile

z = zipfile.ZipFile('Your zip file with extension')                #Add the locked zip file name

wordlist = open('Add your wordlist with extension', 'r').read()    #Add the worlist name with extension
wordlist = wordlist.splitlines()

tries = 0

for word in wordlist:
    try:
        tries += 1
        z.setpassword(word.encode('acsii'))
        z.extract('Content inside zipfile with extension')         #Add the content names with extension. 
                                                                   #If you doesn't know the content inside Zip add a env file as black with func name
        print( f"Tries : {tries} and Password : {word}")
        break
    except:
        pass