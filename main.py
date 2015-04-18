from pen_person import NormalPen, MagicPen, Person

george = Person("George")
bic = NormalPen()
montblanc = MagicPen("Python is a wonderful language")


print bic.color
bic.color = "blue"
print bic.color
print montblanc.color

if MagicPen.magicOn != 0:
    print "true"

print montblanc.getText("Programming Language")

MagicPen.magicOn = 0

if MagicPen.magicOn == 0:
    print "false"

print montblanc.getText("Programming Language")

print george.name
george.name = "Eric Arthur"
george.write(bic, "1984")
george.write(montblanc, "Big Brother is watching you")
