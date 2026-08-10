import subprocess as sub
import sys
from sys import exit as getout

class sotelosint:
    def __init__(self, name="-h", argument="-s", prefix="patata", num="patata"):
        self.name = name
        self.argument = argument
        self.prefix = prefix
        self.num = num
    def hunt(self):
        def show_help():
            print("SoteloSint - All-in-One OSINT Tool")
            print("Usage: python archivo.py [target] [argument(subarguments)] [phone]")
            print("Available arguments:")
            print("  -s : Sherlock (Search for usernames)")
            print("     b : Opens your web browser in order to show you every profile he has find")
            print("     c : Exports findings into a structured CSV spreadsheet. Best for data analysis")
            print("     n : Includes adult and explicit content websites in the scan (disabled by default)")
            print("     o : Sets maximum response wait time. Setting it to 5-10s speeds up the scan drastically.")
            print("     t : Routes requests through the Tor network to hide your real IP.")
            print("     u : Changes Tor IP after every single request. Slower, but bypasses aggressive anti-bot systems")
            print("     x : Disables the creation of the default TXT output file to keep your directory clean")
            print("  -m : Maigret (Advanced username search)")
            print("     a : Force maigret to scan every web in its database")
            print("     c : bypass cloudflare security blocks")
            print("     f : Limits the scan to an expecific number of webs, based on the global popularity of those (Need to specify a number)")
            print("     g : Graph file output")
            print("     h : HTML file output")
            print("     o : Sets maximum response wait time. it is recomended to setting it to 5-10s, so the scan speeds up drastically. (Need to specify a number)")
            print("     t : Tell maigret that you want to use Tor services")
            print("     x : XMind file output")
            print("  -H : Holehe (Check accounts by email)")
            print("     c : CSV file output")
            print("     o : Sets maximum response wait time. Setting it to 5-10s speeds up the scan drastically.")
            print("     u : Only shows the webs the user does use, though if one of those is rate-limited, it may not appear aswell")
            print("  -i : Ignorant (Check accounts by phone number)")
            print("     n : does not erase the previus content of the terminal")
            print("  -a : All (Execute all tools sequentially) using the following arguments: (note: knowing that sherlock, nor the other programs will export the output to a txt file, we recomend you using the > to redirect the whole output to a only file)")
            print("     sherlock order: -scn")
            print("     maigret order: -macg")
            print("     holehe order: -Hc")
            print("     ignorant order: -in")
            getout()
        def sherlock():
            b = 'b' in self.argument
            c = 'c' in self.argument  
            n = 'n' in self.argument
            t = 't' in self.argument and 'u' not in self.argument
            u = 'u' in self.argument
            x = 'x' in self.argument

            cmd = ["sherlock", self.name]

            if b: cmd.append("--browse")
            if c: cmd.append("--csv")
            if n: cmd.append("--nsfw")
            if u: cmd.append("--unique-tor")
            elif t: cmd.append("--tor")
            if x: cmd.append("--no-txt")

            try:
                sub.run(cmd)
            except FileNotFoundError:
                print("You don´t have installed Sherlock in your computer, or maybe, you're not in your venv")
            except KeyboardInterrupt:
                print("The scan have been interrupted correctly")
            except ConnectionError:
                print("Your Internet conection in failing, check if you are conected to the net")
            except Exception as e:
                print(f"Unexpected error: {e}")
        def maigret():
            a = "a" in self.argument
            c = "c" in self.argument
            f = "f" in self.argument
            g = "g" in self.argument
            h = "h" in self.argument
            o = "o" in self.argument
            t = "t" in self.argument
            x = "x" in self.argument

            cmd = ["maigret", self.name]

            if a: cmd.append("-a")
            if c: cmd.append("--cloudflare-bypass")
            #File Output Formats
            if g: cmd.append("-G")
            if h: cmd.append("-H")
            if t: cmd.append("--tor-proxy")
            if x: cmd.append("-X")

            try:
                if f and not o and not a:
                    cmd.extend(["--top-sites", self.prefix]) # is like append, but adds more than one element at a time
                elif not f and o:
                    cmd.extend(["--timeout", self.prefix])
                elif f and o and not a:
                    cmd.extend(["--top-sites", self.prefix, "--timeout", self.num])
                sub.run(cmd)
            except FileNotFoundError:
                print("You don´t have installed Sherlock in your computer, or maybe, you're not in your venv")
            except KeyboardInterrupt:
                print("The scan have been interrupted correctly")
            except ConnectionError:
                if "o" in self.argument:
                    print("You do not have Tor services installed, active or in the right port")
                else:
                    print("Your Internet conection in failing, check if you are conected to the net")
            except TimeoutError:
                print("You take so long")
            except Exception as e:
                print(f"Unexpected error: {e}")
        def holehe():
            c = "c" in self.argument
            o = "o" in self.argument
            u = "u" in self.argument

            if not '@' in self.name:
                self.nameH = self.name + "@gmail.com"
            elif not any(dom in self.name for dom in ['gmail', 'hotmail', '.com']): #Comprueba si falta cualquiera de estas cosas
                self.nameH, self.rest = self.name.split("@", 1)
                self.nameH = self.nameH + "@gmail.com"
            else:
                self.nameH = self.name

            cmd = ["holehe", self.nameH]

            if c: cmd.append("-C")
            if o and self.prefix.isdigit(): cmd.extend(["-T", self.prefix])
            if u: cmd.append("--only-used")

            try:
                sub.run(cmd)
            except FileNotFoundError:
                print("You don´t have installed holehe in your computer, or maybe, you're not in your venv")
            except KeyboardInterrupt:
                print("The scan have been interrupted correctly")
            except ConnectionError:
                print("Your Internet conection in failing, check if you are conected to the net")
            except Exception as e:
                print(f"Unexpected error: {e}")
        def ignorant():
            n = "n" in self.argument

            cmd = ["ignorant"]

            if self.prefix.isdigit() == False:
                if self.name.isdigit() == True and len(self.name) >= 11 and len(self.name) <= 15 and self.name.isdecimal() == False:
                    if " " not in self.name:
                        self.num = self.name[2:] #Starts from the 3rd character to the end.
                        self.iprefix = self.name[:2] #Takes the first 2 characters.
                        cmd.extend([self.iprefix, self.num])
                        if n: cmd.append("--no-clear")
                        sub.run(cmd)
                        getout()
                    else:
                        cmd.append(self.name)
                    if n: cmd.append("--no-clear")
                    try:
                        sub.run(cmd)
                    except ValueError:
                        print("Dude, that's not a phone number")
                    getout()
                else:
                    print("You can only use numbers with this argument")
                    getout()
            elif self.prefix.isdigit() == True and len(self.prefix) <= 3 and len(self.prefix) >= 1 and self.num.isdigit() == True and self.name.isdecimal() == False:
                cmd.extend([self.prefix, self.num])
                if n: cmd.append("--no-clear")
                sub.run(cmd)
            elif self.prefix.isdigit() == True and len(self.prefix) > 3 and self.num.isdigit() == False:
                self.num = self.prefix[2:] #Starts from the 3rd character to the end.
                self.iprefix = self.prefix[:2] #Takes the first 2 characters.
                cmd.extend([self.iprefix, self.num])
                if n: cmd.append("--no-clear")
                sub.run(cmd)
            else:
                print("I... Actually I don´t know how did you break the program, unless you did not use numbers as a argument")
        def all_in(): # Good luck, you'll need it. Finding all that info you're looking for in one go, is like hitting the jackpot.
            self.argument = "-scn"
            sherlock()
            self.argument = "-macg"
            maigret()
            self.argument = "-Hc"
            holehe()
            if len(sys.argv) >= 4:
                self.argument = "-in"
                ignorant()
        if self.argument == "-h" or self.argument == "-help" or self.argument == "--help" or self.name == "-h" or self.name == "-help" or self.name == "--help":
            show_help()
        elif self.argument.startswith("-s"):
            sherlock()
        elif self.argument.startswith("-m"):
            maigret()
        elif self.argument.startswith("-H"):
            holehe()
        elif self.argument.startswith("-i"):
            ignorant()
        elif self.argument == "-a":
            all_in()
        else:
            print("You have write an unexisting argument, so, this is the help screen")
            show_help()

if len(sys.argv) <= 1:
    sol = sotelosint()
elif len(sys.argv) == 2:
    sol = sotelosint(sys.argv[1])
elif len(sys.argv) == 3:
    sol = sotelosint(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    sol = sotelosint(sys.argv[1], sys.argv[2], sys.argv[3])
elif len(sys.argv) == 5:
    sol = sotelosint(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print("You must write a minimum of one argument and a maximum of three.") # Opción por defecto si ejecutas solo "python archivo.py"
    getout()

sol.hunt()
