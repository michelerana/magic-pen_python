from pen_person import *

george = Person("George")
bic = NormalPen()
montblanc = MagicPen("Python is a wonderful language")


print bic.color
bic.color = "blue" 
print bic.color
print montblanc.color

if MagicPen.isMagicOn() == 1:
    print "true";
		
print montblanc.getText("Programming Language")
		
MagicPen.toggleMagic()
		
if MagicPen.isMagicOn() == 0:
    print "false"

print montblanc.getText("Programming Language")
		
print george.name
george.name = "Eric Arthur"
george.write(bic, "1984")
george.write(montblanc, "Big Brother is watching you")
