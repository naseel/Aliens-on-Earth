from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class pdfFormat:
	def saveToFile(self,currentObject):
		c = canvas.Canvas("alient.pdf")
		c.drawString(100,750,"Reg.No: "+str(currentObject.regID))
		c.drawString(100,700,"Code Name: "+currentObject.codName)
		c.drawString(100,650,"Blood Colour: "+currentObject.bloodColour)
		c.drawString(100,600,"No.of Antinas: "+str(currntObject.numAntinas))
		c.drawString(100,550,"No.of Legs: "+str(currentObject.numLegs))
		c.drawString(100,500,"Home planet: "+currentObject.homePlanet)
		c.drawString(100,450,"No of days of visit: "+currentObject.howLong)	
		c.save()
