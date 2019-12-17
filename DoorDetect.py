import time
import datetime
import os
import sys
import urllib2
from wia import Wia
from sense_hat import SenseHat

wia = Wia()
wia.access_token = "d_sk_yxhosMPKxwC9HIg2pZLxi4w3"

WRITE_API_KEY='ON0J9PUVWMEQZ9RH'
baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()
sense.set_rotation(270)
sense.clear()
red = (255,0,0)
green = (0,255,0)

# create database on DB server (Macbook Pro), if it does not already exist
os.system("mysql -uroot -h192.168.0.45 --password='steviey19' -e \"CREATE DATABASE IF NOT EXISTS doorOpenDB\"")
os.system("mysql -uroot -h192.168.0.45 --password='steviey19' -e \"CREATE TABLE IF NOT EXISTS doorOpenDB.OpenEvents (doorOpen TIMESTAMP)\"")

# count arguments
args = len(sys.argv)-1

if args != 0: # if there is a time threshold argument provided
  wake_up = sys.argv[1]
  threshold = datetime.datetime.strptime(wake_up, "%H:%M:%S")

# store current time in variable
current_time = time.strftime("%H:%M:%S", time.localtime())
now = datetime.datetime.strptime(current_time, "%H:%M:%S")

def writeData(x): # function to send data to thingspeak
  conn = urllib2.urlopen(baseURL + '&field1=%s' % (x))
  print(conn.read())
  conn.close()

while True:
  doorOpen = False # doorOpen event reset
  motion = sense.get_accelerometer_raw()

  x = round(motion['x'], 4)
  y = round(motion['y'], 4)
  z = round(motion['z'], 4)

  # print accelerometer readings to console
  print("x={0}, y={1}, z={2}".format(x, y, z))
  print(now.time())

  while x > 0.8: # door is opened
    if doorOpen == False: # if door had been closed until while loop was triggered
      doorOpen = True # set status of door to open

      # save door open event timestamp to DB server
      os.system("mysql -h 192.168.0.45 -uroot --password='steviey19' -e \"insert into doorOpenDB.OpenEvents(doorOpen) VALUES(CURRENT_TIMESTAMP)\"")

      writeData(x) # send data to thingspeak

      wia.Event.publish(name="door open test", data = motion) # publish event to wia

      if args == 0: # if no time threshold argument has been provided
        sense.show_message("Back to bed kiddo!", text_colour = red) # display message
      else:
	if now.time() < threshold.time():
          sense.show_message("Back to bed kiddo!", text_colour = red) # display message
        else:
	  sense.show_message("Good morning!", text_colour = green) # display message

    x = sense.get_accelerometer_raw()['x'] # check for whether door has been closed

  time.sleep(.5)
