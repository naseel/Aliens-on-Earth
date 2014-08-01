from GetDetls import GetDetls
import os

class AlienFriend:
	registerID=None
	def __init__(self):
		self.registerID = 1001	
	def getDetails(self):
		while True:
			print "1.Register\n2.Exit"
			userChoice=input()
			if userChoice==1:
				print "\n"
				doReg = GetDetls()
				doReg.getVal(self.registerID)
				print "List of File Format Available\n....................... "
				files = [f for f in os.listdir('.') if os.path.isfile(f)]
				for currentFile in files:
					if "Format" in currentFile and "pyc" not in currentFile:
						print currentFile[:-9]

				print "\nConvert To : "
				fileType = raw_input() 
				try:
					exec("from "+fileType+"Format import "+fileType+"Format") 
					doWrite = eval(fileType+"Format()")

				except:
					print("Error, file is being processed in PDF format") 
					fileType = "pdf" 
					exec("from "+fileType+"Format import "+fileType+"Format") 
					doWrite = eval("pdfFormat()")

				doWrite.saveToFile(doReg)
				print "\nRegistration Successful"
				print "Your Reg.No is: "+str(self.registerID)+"\n\n"
				self.registerID=self.registerID+1
			if userChoice==2:
				print "Exiting..."
				exit()
newAlienFriend = AlienFriend()
newAlienFriend.getDetails()
