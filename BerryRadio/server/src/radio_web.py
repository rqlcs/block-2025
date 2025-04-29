import os
import sys
os.system("sudo sox -t mp3 /opt/berryradio/msic/%s -t wav - | sudo /opt/berryradio/fm_transmitter -f %s -r -"%(sys.argv[1],sys.argv[2]))

