# The Toddler Gatekeeper
## wit-2019-compsys-02 IOT Assignment using Raspberry Pi and Sense Hat

Original proposal: https://github.com/kento-mc/wit-2019-compsys-02/blob/master/proposal.md

The Toddler Gatekeeper is an IOT solution for monitoring the door of a child's bedroom. It uses the Raspberry Pi and Sense Hat to detect the door of the room being opened, and logs these door-open events to the Wia IOT platform, which then notifies any subscribers via Twitter and/or SMS. This is to allow parents or caregivers to monitor a child trying to leave the room. They can use the built in Wia visualisations to track these door-open events over time. The Raspberry Pi also connects remotely to a database server and adds each door-open event to a local database.

The Toddler Gatekeeper also uses the functionality of the Sense Hat to communicate to the children who try to open the door. When arming the Gatekeeper, the user can set a time threshold (e.g. 7:00am) before which, if the Gatekeeper is triggered it will display a message in red and play a recording of the parent/caretaker's voice over a bluetooth speaker, telling the child to get back to bed (Whether a child obeys is beyond the scope of the Gatekeeper's functionality!).






#### Remote Database implementation

I set up a new database called doorOpenDB on my laptop to store records of doorOpen events. 


I granted remote access to the raspberry pi to allow records to be added to the OpenEvents table when the doorOpen event is generated by DoorDetect.py running on the pi.

First I had to create a user for the pi:
CREATE USER 'root'@'192.168.0.143' IDENTIFIED BY 'my_password';

Then I was able to grant privileges:
GRANT ALL PRIVILEGES ON *.* TO root@192.168.0.143 WITH GRANT OPTION;

#### Audio player implementation

dafads

#### Bluetooth implementation

https://unix.stackexchange.com/questions/96693/connect-to-a-bluetooth-device-via-terminal
https://computingforgeeks.com/connect-to-bluetooth-device-from-linux-terminal/
