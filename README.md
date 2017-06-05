# Web Application User Guide

## 1 Installation

This web application was implemented by Django framework with the sqlite3 database. This user guide aims to introduce the web server installation and web page introduction. 
The web application bases on NAOqi API so that the NAOqi environment is necessary. See here to find out how to install Python SDK and NAOqi for python on your server (multiple operating system suported): http://doc.aldebaran.com/2-1/dev/python/install_guide.html.
To use Django framework, Django needs to be installed. See here to find how to install Django on your server (multiple operating system suported): https://docs.djangoproject.com/en/1.11/intro/install/
To use this this application, please ensure the robot is connected into the same Local Area Network or LAN with you server device. 

## 2 Settings and Start Server
Before running the application, you need to config some parameters. Please specific the IP address and port of the Robot in Util.py script. Please note that this parameter may change when the server and robot reconnect to LAN in different orders according to your LAN DHCP settings.
To start server, use the command: python manage.py runserver [Server IP]:[Server Port]
Then users can access to our application by typing [Server IP]:[Server Port] in URL bar of their browser.
Due to the time limit, the admin page is not implemented, which caused the complicated work before user runs the server. In the future, users will not need to modify the codes to change the settings.

## 3 Application Usage
### 3.1 Create Motion List
In our application, the robot will perform as the description of the motion list. Users can create or delete motion lists. To create motion list, in the MOTION LISTS Section, user needs to click Create New button and type in the name to finish the creation. 
### 3.2 Active Motion List
The robot will only process the requests of one motion list in the same time. In this case, users need to active a motion list from the existing motion lists. And then the next section of the webpage will display the name of the motion list that user selected. 
### 3.3 Create Motions
If one of the motion lists is activated, its name will be displayed in the next section of the web page. And then user can create motion by clicking New Motion button. A window will populate for user to choose the motions they want to create. The motions include walk, stand, rest, lay, speak, customize and steps. When user choose different motions, the content of the window will change and user needs to fill the form to specify the parameters.
When a motion is created, it will show in a list with its motion types.
### 3.4 Run Motion List
Click the Run button to run the motion list.
### 3.5 Change the order of the motions in the list
Drag and drop the items in the list to change the orders.
### 3.6 Delete Motion
Click Delete button at the right side of each list item to delete the motions.
### 3.7 Delete Motion List
Click the DELETE LIST button to delete the current motion list. Please note that all the motions in the motion list will be deleted and not recoverable.
### 3.8 Information Display
The robot information shows in the Information Section. To see more information, click the Robot Setting Page to jump to the Nao Setting Page.
