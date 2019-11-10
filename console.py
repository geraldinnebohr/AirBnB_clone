#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import time

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

    def do_create(self, args):
        """creates a new instance""" 
        #print(type(args))
        if len(args) == 0:
            print("** class name missing **")
            return
        
        token = args.split()

        try:
            newInstance = eval(token[0])()
            #time.sleep(2)
            newInstance.save()
            #time.sleep(2)
            print(newInstance.id)
        except:
            print("** class doesn't exist **")
        
            
    
if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()