# Darna
##DARNA Healthy Intent v1.0- An open source intiative - self custody of your health data
##feel free to contribute
##Early stage. Beta and under development and isnt secure. Please take all steps to safeguard your data. 

What is this project?
======================
Darn the siloed health system!! 
This project is an open-source software that helps you store your health data that is currently saved in different places like electronic health records, fitness apps, and wearable devices. 

With this software, you can bring all your health data together in one place on your computer at home. When you visit a new doctor, you can choose to share your health data with them on demand through email, link etc. This way, you have full custody of your health data and can decide who to share it with.

I created this project because I had trouble moving my own health data when I switched healthcare providers. As someone who works in the healthcare space, I see that current EHR solutions make it difficult to port your data, even though there are regulatory requirements to do so. It's frustrating to see that some institutions still rely on fax and scan to move data around, which shows how outdated and hidden these data porting techniques are.

This is just the first iteration of the project, and I anticipate that there will be many more iterations before it takes a good form. But my goal is to make it easier for people to take ownership of their health data and store it in one place on their own computer. This way, they can decide who to share it with and have more control over their own health.

License?
========
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; 

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Snapshots:
=============
<img src="https://github.com/seapoe1809/Darna/assets/129666906/f3a34322-8402-485c-b8d0-cc70bf9cd2bc" width="200", height="300"/>
![IMG_5570]![IMG_5572](https://github.com/seapoe1809/Darna/assets/129666906/7feb1a14-7e6a-4273-b571-1f1a282350b3){:height="200px" width="400px"}.
(https://github.com/seapoe1809/Darna/assets/129666906/a4a53580-2943-4942-bf03-06d913ac8a4e)
![IMG_5575](https://github.com/seapoe1809/Darna/assets/129666906/3e5e2600-eab8-40a8-9e15-c17fa8a46e6c)
![IMG_5570](https://github.com/seapoe1809/Darna/assets/129666906/0d6b7ae8-b95b-4306-ad80-99a193f99dad)





![IMG_5573](https://github.com/seapoe1809/Darna/assets/129666906/ae934f4a-cde2-426c-846b-6d03fd1c673d)
![IMG_5581](https://github.com/seapoe1809/Darna/assets/129666906/bc569065-d8d8-4238-bd94-26943e20d74e)

![IMG_5576](https://github.com/seapoe1809/Darna/assets/129666906/3b8481ac-ccd5-4fcd-95ea-c614c4ece37d)
![IMG_5577](https://github.com/seapoe1809/Darna/assets/129666906/cbf00dd4-b45d-4137-8306-e90bdae8159b)

![IMG_5578](https://github.com/seapoe1809/Darna/assets/129666906/a59bdd51-caa0-409d-994f-27c716b82b93)
![IMG_5580](https://github.com/seapoe1809/Darna/assets/129666906/a94d831b-df02-4389-94fa-39aae382e380)


=======================================
#linux os (any distro as long as docker runs)
#git
#docker
#python3

For my project, I decided to make the software only for Linux users. The first step is to install Nextcloud, which is a versatile self-cloud management tool that is open source, which I am passionate about.

Once installed, the drive becomes your self hosted cloud drive at home, meaning you can store your data on it and access it from anywhere with no other 3rd party involved. I chose Nextcloud because it has built-in security features, and it already has apps available for iOS, Android, and desktop and allows you to use your computer to be the cloud.

To make things even easier, I used Python for some automation to move files on your computer, create encrypted backups, and create some basic visualizations of your health data. This way, you can easily manage your health data, keep it secure, and view it in a way that makes sense to you.

Please note that this is only the first version of the project, and I plan on adding more features and making improvements in the future.

step 1: Install and configure nextcloud
=======================================

a) Make sure you have docker and python3. If not go to docker.com and python3; get a free acct and then install. Once done do the following:
 Install Git and git clone Darna repo:
 
 
              $sudo apt-get install git
              $git clone https://github.com/seapoe1809/Darna
              $cd Darna
              $pip install -r requirements.txt
              $python3 setup_darna.py
        

That should take you to step c as below

b) Subsequently on terminal you could run if you prefer. The step above should automatically do this for you:

             $sudo docker run --sig-proxy=false --name nextcloud-aio-mastercontainer --restart always --publish 80:80 --publish 8080:8080 --publish 8443:8443 --volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config --volume /var/run/docker.sock:/var/run/docker.sock:ro --env NEXTCLOUD_DATADIR="/home/darnahi/" nextcloud/all-in-one:latest
 
 ##This starts docker containers  and also creates a folder data on your computer /home/darnahi/ that will serve as your external drive to store your files
 ##Important: If umbrel is running, the ports conflict. So ideal would be to use the native nextcloud app on umbrel
 
c) go to your web browser at https://<your-ip-address>:8080 to complete the rest of installation. Follow instructions on your webpage. Save your seed phrase in a text file.
 
d) You should port forward in your router login. Goto advanced settings and add port forwarding to your device IP addr, external and internal: 443 and save.
  
e) You should obtain a domain address to allow easy access from anywhere and also phone apps. It gives needed security certificates needed for your browsers to function well. To get one, you could get for free as listed on splash page or just buy one. I bought mine from google domains. If you wish, I can give you a secure subdomain for free, but would need your public IP address.
  
f) If you do buy one, login to your domain management account and go to DNS section and configure as shown in the Nextcloud splash page. You could get you public IP from typing in google 'whats my ip'
  
g) It should then take you to next page where you choose the modules you need. I would suggest choosing all except 'talk' module.
  
h) It should take almost 10 min to get it up and running, and finally will give you a username and password. eg. "admin" "asdnilsdfvblidfsvblisd98yy89y08ykjn".
 
i) Launch your desktop app at https://<your sub domain> and enter your username and pwd.
 
j) download your nextcloud app and enter your 'https://<your sub domain>' which will prompt for password and then you should be done.


Step 2: Download your health data in nextcloud from iphone
=========================================================

a) On apple health app, click the profile icon, then choose "Export All Health Data" and save the zip file in nextcloud to 'Health_server'.
 
b) If you have data on EPIC MyChart or your doctors gateway, login and go to Menu, search 'sharing' or 'export', click 'yourself' and download a zip file to 'Health_server'.
 
c) Scan PDF's: On nextcloud, choose the '+' menu in the lower center and make scanned pdf's of your health documents and save to the Health_server


 ##Why nextcloud and not any cloud
 =================================
 Nextcloud allows you to store your data on your computer even if you were remote. Technically any cloud works but that is your choice. Im tired of others reselling my data.
 
 
 
 Step 3: Sync files to your health server.
 =========================================
 Goto your home folder and enter the following python3 commands:
        
                 $cd Darna
               
                 $python3 syncmyfiles.py
       
 
 This step should lead to unzipping and setting you up with files in your health server. Followed by creating an encrypted backup in Darna folder.
 
##stuck at domain validation for nextcloud and you feel you have completed all steps:
 https://github.com/nextcloud/all-in-one#how-to-skip-the-domain-validation
       sudo docker run --sig-proxy=false --name nextcloud-aio-mastercontainer --restart always --publish 80:80 --publish 8080:8080 --publish 8443:8443 --volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config --volume /var/run/docker.sock:/var/run/docker.sock:ro --env NEXTCLOUD_DATADIR="/home/darnahi/" --env SKIP_DOMAIN_VALIDATION=true --add-host <domain-name>:<public-ip-address> nextcloud/all-in-one:latest
 
 ## having trouble with nginx not responding the way it should. You might have to recompile it per instructions here: https://nginx.org/en/linux_packages.html?&_ga=2.69118673.19204514.1685092846-863965323.1683102994#Debian
## Help needed for android nextcloud app setup, downloads and PDF scans
 
Sources and references:
1. https://github.com/nextcloud
