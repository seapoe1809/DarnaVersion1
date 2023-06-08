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


<img src="https://github.com/seapoe1809/Darna/assets/82007659/0b1e0ed2-bcbd-4a5c-8680-cadb17fc9055" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/96ff06aa-3739-4596-9ead-240359e40a48" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c9a21783-9c57-464a-9f8e-d71f658c7793" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/0b126f2a-d66f-4bc2-a90f-1a49efb2281d" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/478d54cd-5e25-4134-ba6c-21a67220b5f7" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c1756960-15b9-495e-97f2-7e0927c7cb31" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/6807fe69-1305-47dd-8d2c-0ad3bcfbc8fa" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/eb4f9e67-fd06-4b77-aa72-dbb025997014" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/2b88836b-5375-46f8-89a8-a14d766c0813" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/0d4136b1-7b2b-4435-ad05-e74712779f58" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/ffc57183-8ef7-4d9e-bd39-02e580aa115a" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/8ff0cb26-c491-4186-9302-8960f8ebcb54" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/869afa6e-ec9d-4203-a6c9-636d55ca6e57" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/b17eb880-cd9d-4657-8099-1a508f7167a8" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/f1c26f0c-fb38-48e1-8551-5b36de750c91" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/f718336b-e545-43e5-aa50-aa004c274954" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/86ab0bce-a0da-4330-9849-2d1600262f27" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c8272ff2-69db-4984-8ebe-469cb02ee7ab" width =200, height=400>


basic requirements
=======================================
1. linux os (any distro as long as docker runs)
2. git
3. docker
4. python3

For my project, I decided to make the software only for Linux users. The first step is to install Nextcloud, which is a versatile self-cloud management tool that is open source, which I am passionate about.

Once installed, the drive becomes your self hosted cloud drive at home, meaning you can store your data on it and access it from anywhere with no other 3rd party involved. I chose Nextcloud because it has built-in security features, and it already has apps available for iOS, Android, and desktop and allows you to use your computer to be the cloud.

To make things even easier, I used Python for some automation to move files on your computer, create encrypted backups, and create some basic visualizations of your health data. This way, you can easily manage your health data, keep it secure, and view it in a way that makes sense to you.

Please note that this is only the first version of the project, and I plan on adding more features and making improvements in the future.

step 1: Install and configure nextcloud with your computer as cloud
===================================================================
we are using nextcloud as it is open source and allows you to run your computer at home as your cloud. Remember step c in this section can be a little finicky. Appreciate your patience with this. 

a) Make sure you have docker and python3. If not go to docker.com and python3; get a free acct and then install. Once done do the following:
 Install Git and git clone Darna repo:
 
 
              $sudo apt-get install git
              $git clone https://github.com/seapoe1809/Darna
              $cd Darna
              $pip install -r requirements.txt
              $python3 setup_darna.py
        

That should take you to step c as below. If for some reason, you have to re-run setup_darna.py, please delete folder 'Health_server' and rerun the command above.

b) This starts docker containers  and also creates a folder data on your computer /home/darnahi/ that will serve as your external drive to store your files as part of Nextcloud instance.
 ##Important: If umbrel is running, the ports conflict. So ideal would be to use the native nextcloud app on umbrel
 
c) Now go to your web browser at "https://your-ip-address:8080: to complete the rest of installation. This step needs some patience as the initial step could be finicky. The main reason is to set it up so that you can access nextcloud on your computer from outside your home.
  i) You could get your ip_address from $ifconfig. 
  ii} Follow instructions on your webpage. 
  iii) Remember to save your seed phrase in a text file.
 
d) You should port forward 443 in your router. Steps are explained well by nextcloud. Login to your router. Usually instructions are at base of your router. Goto advanced settings and add port forward 443 (both TCP/UDP) to your device IP addr; Make sure you select 443 for bothe external and internal and save.
  
e) You should obtain a domain address to allow easy access from anywhere and also phone apps. It gives needed security certificates needed for your browsers to function well. To get one, you could get for free as listed on splash page or just buy one. I bought mine from google domains. If you wish, I can give you a secure subdomain for free, but would need your public IP address.
  
f) If you do buy one, login to your domain management account and go to DNS section and configure as shown in the Nextcloud splash page. You could get you public IP from typing in google 'whats my ip'
  
g) It should then take you to next page where you choose the nextcloud modules you need. I would suggest choosing all except 'talk' module.
  
h) It should take almost 10 min to get it up and running, and finally will give you a username and password. eg. "admin" "asdnilsdfvblidfsvblisd98yy89y08ykjn". Save it in your password manager or a text file.
 
i) Launch your desktop app at https://your-sub-domain(eg.https://nextcloud.darna.com and enter your username and pwd. 
 
j) download your nextcloud app in ios or android, and enter your 'https://your-sub-domain' which will prompt you for password and then you should be done!
 
##Why nextcloud and not any cloud
 Nextcloud allows you to store your data on your computer even if you were remote and gives you more control. Technically any cloud works but that is your choice. Im tired of others reselling my data.
 
 ##issue: if for some reason you have to re-run setup_darna.py, then delete the Health_server folder and rerun.
 ## find your IP by going to terminal and entering $ifconfig

Step 2: Download your health data in nextcloud from iphone
=========================================================
a) Make a folder called 'Darnahi' in first splash page of Nextcloud. The next py files will use that to sync in your computer. 
 
b) Download ios health files: On apple health app, click the profile icon, then choose "Export All Health Data" and save the zip file in nextcloud to 'Darnahi' folder.
 
b) If you have data on EPIC MyChart or your doctors gateway, login and go to Menu, search 'sharing' or 'export', click 'yourself' and download a zip file to 'Darnahi' folder.
 
c) Scan PDF's: On nextcloud, choose the '+' menu in the lower center and make scanned pdf's of your health documents and save to the 'Darnahi' folder.

 
 
 Step 3: sync files to your health server from the Darnahi Nextcloud folder:
 ==========================================================================
 Goto your home folder Darna and enter the following python3 commands:
        
   
               
                 $python3 syncmyfiles.py
       
 
 This step should lead to unzipping, syncing and setting you up with files in your health server. it should also set up Grafana to view your file. I am using https://github.com/k0rventen/apple-health-grafana code as this person seems to have done a fair job in visualizing the data. This followed by creating an encrypted backup in Darna folder done automatically by the syncmyfiles.py
 
 Step 4: Start the flask server to view your files
 ==================================================
 Go to the Health_server dir and start the flask server.
          
               $cd /home/<user>/Health_server
               $python3 darna.py
 
 
 It should tell you which ip address to go to to start interacting with your data. Hope you like it! Please share feedback and let me know if you woudl like to contribute to this project.
 
 The default password for Darna is 'health' and for Grafana is user:'admin', password:'health'.
 
 To note is the variables.py file that stores some variables that the darna.py file uses. It automatically tries to populate with the IP address and the path to health server. It does however need you to update the Nextcloud username and password to allow the SYNC fuction to work. The SYNC button in UI starts movement of files between Nextcloud and Healthserver but however pushing files back into nextcloud uses the webdav format and hence uses a curl command to push files. For that reason it needs your username and password for Nextcloud.
 Open the variables.py with text editor and add: 
 
                               user = <username> #usually admin
                               pwd = <password_nextcloud> #usually a long string of alphanumerics
 

Also if you have a summary PDF file, label it 'summary.pdf' and place it in static folder for the 'my health file' to autolink to.
 
 
 
 Other issues:
 
##stuck at domain validation for nextcloud and you feel you have completed all steps:
 https://github.com/nextcloud/all-in-one#how-to-skip-the-domain-validation
       sudo docker run --sig-proxy=false --name nextcloud-aio-mastercontainer --restart always --publish 80:80 --publish 8080:8080 --publish 8443:8443 --volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config --volume /var/run/docker.sock:/var/run/docker.sock:ro --env NEXTCLOUD_DATADIR="/home/darnahi/" --env SKIP_DOMAIN_VALIDATION=true --add-host <domain-name>:<public-ip-address> nextcloud/all-in-one:latest
 
## Help needed for android nextcloud app setup, downloads and PDF scans OCR recognition
 
Sources and references:
1. https://github.com/nextcloud
2. https://github.com/k0rventen/apple-health-grafana
3. chat.openai.com
