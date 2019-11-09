#!/usr/bin/python3

import cmd
class Commands(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self, args):
        """end_of_file"""
        print("endo of file")
    
    def do_quit(self, args):
        """quit cmd"""
        print("chao bye")
        return True

    def emptyline(self):
        """no realiza nada"""
        pass
    
if __name__ == "__main__":
    interprete = Commands()
    interprete.cmdloop()