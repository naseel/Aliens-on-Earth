from GetDetls import GetDetls
from txtFormat import txtFormat
from pdfFormat import pdfFormat
from foobarFormat import foobarFormat



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
				print "Enter export format"
				print "Convert To : "
				fileType = raw_input() 
				try:
					doWrt =  eval(fileType+"Format()")
				except:
					print("Error, file is being processed in PDF format")
					doWrt =  eval("pdfFormat()")
				doWrt.saveToFile(doReg)
				print "\nRegistration Successful"
				print "Your Reg.No is: "+str(self.registerID)+"\n\n"
				self.registerID=self.registerID+1
			if userChoice==2:
				print "Exiting..."
				exit()
newAlienFriend = AlienFriend()
newAlienFriend.getDetails()
