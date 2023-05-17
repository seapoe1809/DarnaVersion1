import os
import subprocess
import webbrowser
import time

##setup with git: sudo apt-get install git
##git clone"https://github.com/seapoe1809/Darna"
##cd into the dir

##cmd to start process python3 setup_darna.py
print(' Will try to install rsync (to help sync the Health_server), caffeine (to prevent the device from falling asleep.')

#get rsync to import zip files from Health_server
#get caffeine to help the computer stay awake and not fall asleep so it is available to nexcloud app
subprocess.run(['sudo', 'apt-get', 'install', 'rsync'])
subprocess.run(['sudo', 'apt-get', 'install', 'caffeine'])

#check for docker and install if unavailable
try:
    subprocess.run(['docker', 'version'], check=True)
except subprocess.CalledProcessError:
    print('Installing docker')
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', 'docker.io'], check=True)
    except subprocess.CalledProcessError:
        print('Installation failed; please see docker.com instructions')
print('Good news, Docker already installed')

#install nextcloud mastercontainer and get it up and running

os.system('sudo docker run --sig-proxy=false --name nextcloud-aio-mastercontainer --restart always --publish 80:80 --publish 8080:8080 --publish 8443:8443 --volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config --volume /var/run/docker.sock:/var/run/docker.sock:ro --env NEXTCLOUD_DATADIR="/home/darnahi/" nextcloud/all-in-one:latest')

#lets all the above startup and subsequently opens browser
print("Waiting for installation to complete!")
time.sleep(5)
print("The browser to Nextcloud will open to complete set up. Also a browser to duckdns.org")
print("if you wish to get a free DNS to help with security certificates.")

#opens browser at <ip address: 8080>
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
url ='{ip_address}:8080'
#open duckdns.org to get free DNS to help with security access; you need it to complete
url2='https://www.duckdns.org/'
webbrowser.open(url)

#make a new dir to expand healthdata into
new_dir_name = 'Health_server'
home_dir = os.path.expanduser("~")
new_dir_path = os.path.join(home_dir, new_dir_name)
subprocess.run(['mkdir', new_dir_path)
#change into the new dir
os.chdir(new_dir_path)
subprocess.run([['mkdir', 'encrypt_backup'])
