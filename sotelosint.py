import subprocess as sub
import sys
from sys import exit as getout

class sotelosint:
    def __init__(self, name="-h", argument="-s", num="2008"):
        self.name = name
        self.argument = argument
        self.num = num
    def hunt(self):
        if self.argument == "-h" or self.argument == "-help" or self.argument == "--help" or self.name == "-h" or self.name == "-help" or self.name == "--help":
            print("SoteloSint - All-in-One OSINT Tool")
            print("Usage: python archivo.py [target] [argument] [phone]")
            print("Available arguments:")
            print("  -s : Sherlock (Search for usernames)")
            print("  -m : Maigret (Advanced username search)")
            print("  -H : Holehe (Check accounts by email)")
            print("  -i : Ignorant (Check accounts by phone number)")
            print("  -a : All (Execute all tools sequentially)")
            getout()
        if self.argument == "-s":
            sub.run(["sherlock", self.name])
        if self.argument == "-m":
            sub.run(["maigret", self.name])
        if self.argument == "-H":
            if not '@' in self.name:
                self.nameH = self.name + "@gmail.com"
            elif not any(dom in self.name for dom in ['gmail', 'hotmail', '.com']): #Comprueba si falta cualquiera de estas cosas
                self.nameH, self.rest = self.name.split("@", 1)
                self.nameH = self.nameH + "@gmail.com"
            else:
                self.nameH = self.name
            sub.run(["holehe", self.nameH])
        if self.argument == "-i":
            if self.num.isdigit() == False:
                if self.name.isdigit() == True:
                    sub.run(["ignorant", self.name])
                    getout()
                else:
                    print("You can only use numbers with this argument")
                    getout()
            sub.run(["ignorant", self.num])
        if self.argument == "-a":
            if '@' in self.name:
                self.nameH, self.rest = self.name.split("@", 1)
            else:
                self.nameH = self.name
            sub.run(["sherlock", self.nameH])
            sub.run(["maigret", self.name])

            if not '@' in self.name:
                self.nameH = self.name + "@gmail.com"
            elif not any(dom in self.name for dom in ['gmail', 'hotmail', '.com']): #Comprueba si falta cualquiera de estas cosas
                self.nameH, self.rest = self.name.split("@", 1)
                self.nameH = self.nameH + "@gmail.com"
            else:
                self.nameH = self.name
            sub.run(["holehe", self.nameH])
            if len(self.num) >= 14 or len(self.num) <= 10:
                print("You have a mistake in the phone number, so I'm skipping it")
            else:
                self.prefix = self.num[:2] #Pilla todo lo que haya antes del caracter numero 2
                self.numH = self.num[2:] #Pilla todo lo posterior al caracter numero 2
                if self.prefix.isdigit() == False or self.numH.isdigit() == False:
                    getout()
                sub.run(["ignorant", self.prefix, self.numH])
if len(sys.argv) <= 1:
    sol = sotelosint()
elif len(sys.argv) == 2:
    sol = sotelosint(sys.argv[1])
elif len(sys.argv) == 3:
    sol = sotelosint(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    sol = sotelosint(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("You must write a minimum of one argument and a maximum of three.") # Opción por defecto si ejecutas solo "python archivo.py"
    getout()

sol.hunt()
