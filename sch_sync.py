import unzip_py


src_dir= "/mnt/darnahi/admin/files/Documents/Health_server"

#the main dir to store and unzip files
dir_name = 'Health_server'
HS_dir_path = unzip_py.create_directory_paths(dir_name)

dest_dir = HS_dir_path
new_perms = "750"

#sync data every 7 days
unzip_py.rsync_with_permissions(src_dir, dest_dir, new_perms)

