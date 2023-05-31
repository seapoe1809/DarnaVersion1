##This file with help with rest of setup after adding your health files and apple export.zip to the Darnahi folder in nextcloud. It begins by rsyncing, unzipping, creating an encrypted backup, starting up grafana to ingest apple data into influxdb and running a sync in background every 3 days. 

import unzip_py
import os
import schedule
import threading
import subprocess
from cryptography.fernet import Fernet

#label a path to dir
#the dir to nexcloud files
src_dir= "/home/darnahi/admin/files/Darnahi/"

#the main dir to store and unzip files
dir_name = 'Health_server'
HS_path = unzip_py.create_directory_paths(dir_name)

#the original git setup dir
dir_name = 'Darna'
parent_dir = unzip_py.create_directory_paths(dir_name)

#the dir to store encrypted file
dir_name = 'Darna/encrypt_backup'
encrypt_dir_path = unzip_py.create_directory_paths(dir_name)

#once we have mapped the dir; the step is to sync the files to these dir
#rsync the health info from /home/darnahi/admin/files/Health_server into the new dir

#rsync file from nexcloud to the HS dir
dest_dir= HS_path
new_perms = "750"

##unzip files from the folder if any
unzip_py.rsync_with_permissions(src_dir, dest_dir, new_perms)

#dir/ extract location
unzip_py.extract_zip_files(HS_path)

#Setting up grafana in apple-health-grafana
grafanadir= f'{parent_dir}/apple-health-grafana/'
subprocess.run(['docker-compose', '-f', f'{grafanadir}/docker-compose.yml', 'pull'])
subprocess.run(['docker-compose', '-f', f'{grafanadir}/docker-compose.yml', 'up', '-d', 'grafana', 'influx'])
subprocess.run(['docker-compose', '-f', f'{grafanadir}/docker-compose.yml', 'up', 'ingester'])

#forget password to secure
password = None

#open and run sync files every 3 days using cron job.
print(" Setting up a cron job to sync files between nextcloud darnahi dir and HS_path every 3 days.\n")
print("To stop the cronjob '$crontab -e' \n")
print("comment it out by using '#'. Then save and exit")

def run_rsync():
	unzip_py.rsync_with_permissions(src_dir, dest_dir, new_perms)	

schedule.every(3).days.do(run_rsync)
def run_schedule():
	while True:
		schedule.run_pending()
		unzip_py.time.sleep(1)
schedule_thread = threading.Thread(target=run_schedule, daemon=True)
#create a background thread as start it as a daemon
schedule_thread.start()


#Encrypting the files and saving it as backup
#input password and then pad it to be used by Fernet
password =unzip_py.stdiomask.getpass("\n ENTER PASSWORD TO ENCRYPT BACKUP DATA:\n")
#password = input("Enter password: \n")

padded_password = unzip_py.pad_password(password)
padding = len(padded_password) % 4
if padding != 0:
    padded_password += '=' * (4 - padding)
key = unzip_py.base64.urlsafe_b64encode(padded_password)
def store_password_in_cache(fernet):
    print("caching", fernet)
fernet = Fernet(key) #create a fernet object
store_password_in_cache(fernet)
def get_fernet_from_cache():
    fernet = retrieve_fernet_from_cache()
    return fernet

#write encrypted data backup directory in parent darna dir
source_folder = HS_path
destination_folder = encrypt_dir_path
def encrypt_folder_contents(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename + '.encrypted')

        if os.path.isdir(source_path):
            #if its a dir, recursively encrypt its contents
            encrypt_folder_contents(source_path, destination_path)
        else:
            with open(source_path, 'rb') as file:
                file_data = file.read()
                #permissions = os.stat(source_file).st_mode

                encrypted_data = fernet.encrypt(file_data)

            with open(destination_path, 'wb') as file:
                file.write(encrypted_data)

#calling the function to being encrypting
print("...Encrypting the data to a backup file in ~/Darna. This might take some time")
#encrypt_folder_contents(source_folder, destination_folder)
#Keep main thread running
while True:
	unzip_py.time.sleep(1)





