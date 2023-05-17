import os
import subprocess
import schedule
import time
import base64
import stdiomask
import hashlib
import getpass
import shutil
from cryptography.fernet import Fernet
import zipfile

def extract_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                zip_file_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                    zip_ref.extractall(root)
                    print("Extracted:", zip_file_path)
                #remove the zip files after extraction
                os.remove(zip_file_path)
                print("Deleted:", zip_file_path)

## creating a dir path in ~/ location
def create_directory_paths(dir_name):
    home_dir= os.path.expanduser("~")
    dir_path = os.path.join(home_dir, dir_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_path

def rsync_with_permissions(src_dir, dest_dir, new_perms):
    #command = f"sudo rsync -avz --chmod={new_perms}, {src_dir}, {dest_dir}"
    rsync_args = ["sudo", "rsync", "-avz", "--chmod=" + new_perms, src_dir, dest_dir]
    subprocess.run(rsync_args)
    #chown the folder
    new_owner = getpass.getuser()
    chown_args = ["sudo", "chown", "-R", new_owner, dest_dir]
    subprocess.run(chown_args)

#takes an input pwd and pads and hashes it and save it to cache
def pad_password(password):
    digest = hashlib.sha256(password.encode()).digest()
    return digest[:32]

def store_password_in_cache(fernet):
    print("caching", fernet)

def get_fernet_from_cache():
    fernet = retrieve_fernet_from_cache()
    return fernet

"""#encrypt folder contents to create a backup
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
                fernet=Fernet(key)
                encrypted_data = fernet.encrypt(file_data)

            with open(destination_path, 'wb') as file:
                file.write(encrypted_data)
                # set permissions to source
                #os.chmod(destination_path, permissions)
"""
#run scheduled scripts
def run_script(sch_sync):
    subprocess.Popen(["python3", sch_sync])