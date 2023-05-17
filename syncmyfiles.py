import unzip_py
import os
from cryptography.fernet import Fernet

#label a path to dir
#the dir to nexcloud files
src_dir= "/mnt/darnahi/admin/files/Documents/Health_server"

#the main dir to store and unzip files
dir_name = 'Health_server'
HS_dir_path = unzip_py.create_directory_paths(dir_name)

#the original git setup dir
dir_name = 'Darna'
parent_dir = unzip_py.create_directory_paths(dir_name)

#the dir to store encrypted file
dir_name = 'Darna/encrypt_backup'
encrypt_dir_path = unzip_py.create_directory_paths(dir_name)

#once we have mapped the dir; the step is to sync the files to these dir
#rsync the health info from /home/darnahi/admin/files/Health_server into the new dir

#rsync file from nexcloud to the HS dir
dest_dir= HS_dir_path
new_perms = "750"

##unzip files from the folder if any
unzip_py.rsync_with_permissions(src_dir, dest_dir, new_perms)

#dir/ extract location
unzip_py.extract_zip_files(HS_dir_path)

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

source_folder = HS_dir_path
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
                # set permissions to source
                #os.chmod(destination_path, permissions)

#calling the function to being encrypting
print("...Encrypting the data to a backup file in ~/Darna. This might take some time")
encrypt_folder_contents(source_folder, destination_folder)

#forget password to secure
password = None

#open and run sync files every 3 days

unzip_py.schedule.every(7).days.at("00:00").do(unzip_py.run_script, 'parent_dir')
while True:
    unzip_py.schedule.run_pending()
    time.sleep(1)