class txtgen:
	def saveToFile(self,currentObject):
		f=open("alien.txt","a")
		f.write("Reg.No: "+str(currentObject.ri)+"\n")
		f.write("Code Name: "+currentObject.cn+"\n")
		f.write("Blood Colour: "+currentObject.bc+"\n")
		f.write("No.of Antinas: "+str(currentObject.na)+"\n")
		f.write("No.of Legs: "+str(currentObject.nl)+"\n")
		f.write("Home planet: "+currentObject.hp+"\n")
		f.write("No of days of visit: "+currentObject.hl+"\n\n")
		f.close()

