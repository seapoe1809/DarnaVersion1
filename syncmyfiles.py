import os
import subprocess
import schedule
import time



## creating a dir path in ~/ location
def create_directory_paths(dir_name):
    home_dir= os.path.expanduser("~")
    dir_path = os.path.join(home_dir, dir_name)

#label a path to dir
dir_name = 'Health_server'
HS_dir_path = create_directory_paths(dir_name)


dir_name = 'Health_server/encrypt_backup'
encrypt_dir_path = create_directory_paths(dir_name)

dir_name = 'Darna'
parent_dir = create_directory_paths(dir_name)

#rsync the health info from /home/darnahi/admin/files/Health_server into the new dir
#src_dir = "/home/darnahi/admin/files/Health_server"
def rsync_with_permissions(src_dir, dest_dir, new_perms):
    rsync_args = ["sudo", "rsync", "-avz", "--chmod=" + new_perms, src_dir, dest_dir]
    subprocess.run(rsync_args)
src_dir= "/mnt/darnahi/admin/files/Documents/Health_server"
dest_dir= HS_dir_path
new_perms = "750"

rsync_with_permissions(src_dir, dest_dir, new_perms)

#open and run sync files every 3 days
def run_script(sch_sync):
    subprocess.Popen(["python3", sch_sync.py])

schedule.every(7).days.at("00:00").do(run_script, 'parent_dir')
while True:
    schedule.run_pending()
    time.sleep(1)
