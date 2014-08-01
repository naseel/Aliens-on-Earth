class txtFormat:
	def saveToFile(self,currentObject):
		f=open("alien.txt","a")
		f.write("Reg.No: "+str(currentObject.regID)+"\n")
		f.write("Code Name: "+currentObject.codName+"\n")
		f.write("Blood Colour: "+currentObject.bloodColour+"\n")
		f.write("No.of Antinas: "+str(currentObject.numAntinas)+"\n")
		f.write("No.of Legs: "+str(currentObject.numLegs)+"\n")
		f.write("Home planet: "+currentObject.homePlanet+"\n")
		f.write("No of days of visit: "+currentObject.howLong+"\n\n")
		f.close()

