#!/usr/bin/python3

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, args):
        """end_of_file"""
        print("end of file")
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("chao bye")
        return True

    def emptyline(self):
        """don't make nothing"""
        pass
    
if __name__ == "__main__":
    interpret = HBNBCommand()
    interpret.cmdloop()