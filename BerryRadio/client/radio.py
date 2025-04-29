#Python GUI for FM_TRANSMITTER PROJECT
#RQLCS.

import os
import subprocess
import socket
import termcolor
import Tkinter
import sys
import time
from Tkinter import *
from termcolor import colored
from os import system as shell
from time import sleep

class Radio:

	def __init__(self, frequency, music, hostname, user, password, port):

		self.root = Tk()
       		self.img_border = PhotoImage(file='/opt/berryradio/icon/icon.png')
		self.img_inframe = PhotoImage(file='/opt/berryradio/icon/raspberry.png')
		self.root.tk.call('wm', 'iconphoto', self.root._w, self.img_inframe)
		self.frequency = frequency
		self.music = music
		self.location_fmtransmitter = "/opt/berryradio/fm_transmitter"
		self.PASS_SSH = password
		self.USER_SSH = user
		self.PORT = port
		self.IP_ADDR = hostname
		self.frame()
        	self.root.mainloop()

    	def frame(self):

		self.frame_background = Button(self.root, image=self.img_border, height=380, width=370).place(x=-45,y=-20)
		self.inframeimgright = Button(self.root, image=self.img_inframe, height=25, width=30).place(x=30,y=20)
                self.inframeimgleft = Button(self.root, image=self.img_inframe, height=25, width=30).place(x=240,y=20)
       		self.geometry = self.root.geometry("300x360")
        	self.root.resizable(width=0, height=0)
       		self.title = self.root.title("RaspR4dio")
       		self.configure = self.root.configure(background="grey")
       		self.label_title = Label(self.root,text="BerryR4dio",bg="#464646", fg='pink',font=("Times New Roman",20)).place(x=90,y=20)
       		self.liste = Listbox(self.root,bg="black",width="33",height="8")
       		self.liste.insert(1,"                   -= BerryR4dio =-")
       		self.liste.insert(2,"")
       		self.liste.insert(3, "# Frequency: %s MHz"%(float(sys.argv[1])))
       		self.liste.insert(4, "# Wave Type: FM")
        	self.liste.insert(5, "# Song Name: %s"%(sys.argv[2]))
               	self.liste.insert(6,"")
		self.liste.insert(7, "       %s"%("="*17))
		self.liste.insert(8,"")
		self.liste.insert(9, "HOST: %s"%(self.IP_ADDR))
		self.liste.insert(10,"USER: %s"%(self.USER_SSH))
		for items in range(10):
			self.liste.itemconfig(items,{'fg':'white'})
		self.liste.place(x=18,y=85)
		self.button_github = Button(self.root,text="GitHub",command=self.github).place(x=20,y=310)
	    	self.button_stop = Button(self.root,text="Stop",command=self.stop).place(x=220,y=250)
        	self.button_song_generate_ssh = Button(self.root,text="FM Generate [SSH]",command=self.connexion).place(x=20,y=250)
        	self.button_exit = Button(self.root,text="Exit",command=self.exit).place(x=220,y=310)
    	def connexion(self):
		try:
			print colored("[ * ] Generate FM Station...",'green')
	   		sleep(0.5)
	    		self.payload = "sox -t mp3 /opt/berryradio/msic/%s -t wav - | /opt/berryradio/fm_transmitter/fm_transmitter -f %s -r -" %(self.music,self.frequency)
	    		shell("sshpass -p '%s' ssh  -p %s %s@%s 'cd %s && %s'"%(self.PASS_SSH,self.PORT,self.USER_SSH,self.IP_ADDR,self.location_fmtransmitter,self.payload))
		except (socket.error,SSHException, AuthenticationException) as error_ssh:
			print error_ssh
			sys.exit()

    	def exit(self):

	    	self.root.destroy()

    	def stop(self):
		try:
	    		self.stop_music = "killall fm_transmitter"
	    		shell("sshpass -p '%s' ssh -p %s %s@%s '%s'"%(self.PASS_SSH,self.PORT,self.USER_SSH,self.IP_ADDR,self.stop_music))
	    		print("")
	    		print colored("[ * ] Stop Music !",'red')
	    		sys.exit(2)
		except (socket.error, socket.gaierror, socket.herror) as error_connexion:
			print error_connexion

	def github(self):
		shell("firefox https://github.com/rqlcs")

def help_usage():
	""" Guide d'utilisation """
	help = """
		Usage : berryradio <frequency> <music> <hostname> <user> <password> <port(default 22)>

		<frequency> : [87.5MHz & 108.8MHz] : INT,FLOAT
		<music> : MP3 extension, located in /raspr4dio/msic/
		<hostname> : Raspberry PI  IP ADDRESS
		<user> : SSH Login
		<password> : SSH password
		<port> : 22(default SSH)

		Web Interface at : http://localhost/
	"""
	return help
if __name__=="__main__":
	try:

		if len(sys.argv) < 7 or len(sys.argv) > 7 or sys.argv[1] in ['-h','--help']:
			print(help_usage())
			sys.exit(1)

		if float(sys.argv[1]) < 87.5 or float(sys.argv[1]) > 108:
			print "need to be between 87.5MHz and 108.8MHz"
			sys.exit()

		cnxion = "sshpass -p '%s' ssh -p 22 %s@%s 'ls /opt/berryradio/msic'" %(sys.argv[5],sys.argv[4],sys.argv[3])
		proc = subprocess.Popen(cnxion, shell=True, stdout=subprocess.PIPE)
		list_music = [musics for musics in proc.stdout]
		list_music_strip = [list_music[y].replace('\n','') for y in range(len(list_music))]
       		if sys.argv[2] not in list_music_strip:
                	print "%s not exist at /opt/berryradio/msic/ !" %(sys.argv[2])
                	sys.exit()

		Radio(float(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
	except ValueError:
		print "Error Type ! Frequency Must be INT or FLOAT"
	except (socket.error, socket.gaierror, socket.herror):
		print "Error Connexion."
	except KeyboardInterrupt:
		shell("clear")
		sys.exit()
