# The Toddler Gatekeeper
## wit-2019-compsys-02: IOT Assignment using Raspberry Pi and Sense Hat

[Original Proposal](https://github.com/kento-mc/wit-2019-compsys-02/blob/master/proposal.md "Project Proposal")

The Toddler Gatekeeper is an IOT solution prototype for monitoring the door of a child's bedroom. It uses the Raspberry Pi and Sense Hat to detect the door of the room being opened, and logs these door-open events to the Wia IOT platform, which then notifies any subscribers via Twitter and/or SMS. This is to allow parents or caregivers to monitor a child trying to leave the room. They can use the built in Wia visualisations to track these door-open events over time. The Raspberry Pi also connects remotely to a database server and adds each door-open event to a local database.

The Toddler Gatekeeper also uses the functionality of the Sense Hat to communicate to the children who try to open the door. When arming the Gatekeeper, the user can set a time threshold (e.g. 7:00am) before which, if the Gatekeeper is triggered it will display a message in red and play a recording of the parent/caretaker's voice over a bluetooth speaker, telling the child to get back to bed. Whether a child obeys is beyond the scope of the Gatekeeper's functionality!


## Setup and running the Toddler Gatekeeper

Ensure you have the necessary packages for the Sense Hat installed on your Raspberry Pi. To achieve the full functionality you will also need to install the appropriate packages for Wia and mpg123 (see below), as well as installing mysql-server on your laptop or desktop. You will also need to set up accounts on Wia and/or Thingspeak and configure them to communicate with the Raspberry Pi. 

To mount your Raspberry Pi and Sense Hat to the wall and door, see the instructions [HERE](https://drive.google.com/open?id=1fzZrt7k5KipFu2s-yZfC-tg-IWoR8rIe "How to set up the Gatekeeper").

1. Save the script DoorDetect.py and the audio-files directory to a directory of your choice on the Raspberry Pi.
2. Amend the portions that contain your personal Wia access token, Thingspeak write API key, remote database host IP, path to audio-files directory, etc. You may also wish to customize the messages to be displayed on the Sense Hat LEDs
3. Connect your Raspberry Pi to a bluetooth speaker (see below).
4. SSH into the Raspberry Pi and change directory to the one which contains the DoorDetect.py script.
5. Run the script: 

        $ python DoorDetect.py
  
6. Alternatively, you may enter a time theshold for what message is displayed by including an argument in the HH:MM:SS format.

        $ python DoorDetect.py 15:00:00
  
7. Check that the terminal is displaying accelerometer data, e.g.:

        x=0.9177, y=0.3992, z=0.0366
        x=0.9181, y=0.3979, z=0.0348
        x=0.9177, y=0.3992, z=0.0361
  
8. Open the door to trigger the script and you will see:
  
        a. The LEDs display the message specified in the script. Either 
        b. The bluetooth speaker play the corresponding audio message.
        c. The event will be logged to the remote database.
        d. The event will be logged on Wia or Thingspeak, depending on your settings.
        e. A notification to your personal device of the type you prefer based on your Wia or Thingspeak settings.
        f. A terminal notification that the door is open and the timestamp.
  
9. Closing the door will re-arm the Gatekeeper. It will continue to run until the script has been terminated.


## Remote Database implementation

Before running the DoorDetect.py script:

1. Create a new database called doorOpenDB on the database server machine to store records of doorOpen events. 
2. Grant remote access to the Raspberry Pi to allow records to be added to the OpenEvents table when the doorOpen event is generated by DoorDetect.py running on the Pi.
3. Create a user for the Pi:

        CREATE USER 'root'@'pi_ip_address' IDENTIFIED BY 'my_password';

4. Grant privileges:

        GRANT ALL PRIVILEGES ON *.* TO root@pi_ip_address WITH GRANT OPTION;


## Audio player implementation

Information on using mpg123:

  https://opensource.com/life/16/8/3-command-line-music-players-linux


## Bluetooth implementation

Information on setting up bluetooth:

  https://www.sigmdel.ca/michel/ha/rpi/bluetooth_02_en.html
  https://unix.stackexchange.com/questions/96693/connect-to-a-bluetooth-device-via-terminal
  https://computingforgeeks.com/connect-to-bluetooth-device-from-linux-terminal/
