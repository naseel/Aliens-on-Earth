from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
class pdfgen:
	def saveToFile(self,currentObject):
		c = canvas.Canvas("alient.pdf")
		c.drawString(100,750,"Reg.No: "+str(currentObject.ri))
		c.drawString(100,700,"Code Name: "+currentObject.cn)
		c.drawString(100,650,"Blood Colour: "+currentObject.bc)
		c.drawString(100,600,"No.of Antinas: "+str(currentObject.na))
		c.drawString(100,550,"No.of Legs: "+str(currentObject.nl))
		c.drawString(100,500,"Home planet: "+currentObject.hp)
		c.drawString(100,450,"No of days of visit: "+currentObject.hl)	
		c.save()
