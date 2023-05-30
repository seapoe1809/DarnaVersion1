import os
import subprocess
import webbrowser
import shutil
import time
from pathlib import Path
import socket

##setup with git: sudo apt-get install git
##git clone"https://github.com/seapoe1809/Darna"
##cd into the dir

##cmd to start process python3 setup_darna.py
print(' Step 1: Will try to install rsync (to help sync the Health_server files), caffeine (to prevent the device from falling asleep while running nextcloud home directory.')

#get rsync to import zip files from Health_server
#get caffeine to help the computer stay awake and not fall asleep so it is available to nexcloud app
subprocess.run(['sudo', 'apt-get', 'install', 'rsync'])
subprocess.run(['sudo', 'apt-get', 'install', 'caffeine'])

#Darna.hi will use third party https://github.com/k0rventen/apple-health-grafana to visualize the apple health data. Cloning repository in the current directory and modifying the volume: of yml file...
grafana_repository='https://github.com/k0rventen/apple-health-grafana'
result = subprocess.run(['git', 'clone', grafana_repository])
if result.returncode ==0:
 	print("repository cloned...")
else: 	
	print("failed to clone the repository :(")
	

	
#Making the necessary directories:
#make a new dir to expand healthdata into
new_dir_name = 'Health_server'
home_dir = Path.home()
HS_path = os.path.join(str(home_dir), new_dir_name)
subprocess.run(['mkdir', HS_path])

#Copying static and template folder for flask_server to the Health_server dir and write HS_path and ip_addr to variables.py subsequently
shutil.copytree('templates', f'{HS_path}/templates')
shutil.copytree('static', f'{HS_path}/static')

#opens browser at <ip address: 8080>
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#write to variables.py
url =f'{ip_address}:8080'
content = f"HS_path = '{HS_path}'\nip_address= '{ip_address}'\n"	
file_path = os.path.join(HS_path, 'variables.py')
# Open the file in write mode and write the content
with open(file_path, 'w') as file:
    file.write(content) 

#write volume in docker-compose file for apple-health-grafana
#modify the volume in docker-compose.yml
volume = f'    - {HS_path}/export.zip:/export.zip'
grafanadocker= f'{home_dir}/Darna/apple-health-grafana/docker-compose.yml'
with open(grafanadocker, 'r') as file:
	lines = file.readlines()
	
if len(lines)>=1:
	lines[-1]= volume

with open(grafanadocker, 'w') as file:
	file.writelines(lines)	

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


#open duckdns.org to get free DNS to help with security access; you need it to complete
url2='https://www.duckdns.org/'
webbrowser.open(url)

