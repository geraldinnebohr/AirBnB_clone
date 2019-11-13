# The Holberton AIRBnB CLONE                                                                                               
![alt text](https://media.makeameme.org/created/gets-airbnb-says.jpg "fun AirB&B")             
## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## the HBNB console                                                                                                   
----
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

   -Create a new object (ex: a new User or a new Place)  
   -Retrieve an object from a file, a database etc…  
   -Do operations on objects (count, compute stats, etc…)  
   -Update attributes of an object  
   -Destroy an object  
   
## Commands and how to use it                                                                                     
the command interpreter allow us to handle our data requirements with the following commands
                                                                                                                      
| Command | Function |                                                                                                
| ------- | ------------------------------------ |
| create | create a new instace of a class |
| show | show the info of an instance of a class |
| destroy | destroy a instance of a class |
| update | update the info of the objects in an instance |
| all | update the info of the objects in an instance |
| quit | exit the console |
| help | show the help of the commands |

## Objects
this is the objects that you can pass to the command console

| Object | Function |                                                                                                
| ------- | -------- |
| city | city of the reservation |
| state | country state of the reservation |
| place | Name of the place of reservation |
| user | Name of the user who reserves|
| amenity | Benefits of the place |
| review | review of the room and the guest |

### Start using the console
start the console with
```./console```
you will see:
```(hbnb)```
and can start to use the hbnb console
## How to use the HBNB console
### Syntax:
``` <command> <classname> <id>```
id don't apply to create command
### For help:
```help <command>```
### Examples:
#### For Help:
```
(hbnb)help create
create a new instace of a class
(hbnb)
```
#### For standard commands:
```
(hbnb)create User
993e570d-9b4e-449c-84b3-085ab454d3ce
(hbnb)
```
It will create a new User
``` 
(hbnb)create BaseModel
d711be23-73d9-4fbd-92f5-fe9ec7044d6d
(hbnb)show BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
[BaseModel] (d711be23-73d9-4fbd-92f5-fe9ec7044d6d) {'id': 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d', 'created_at': '2019-07-04T02:20:53.149558', 'updated_at': '2019-07-04T02:20:53.149791'}
(hbnb)
 ```
 It will create a new BaseModel and show the objects of the instance
 
```
(hbnb)destroy BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
['BaseModel', 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d']
(hbnb)
```
## Authors
[Geraldinne "market" Bohorquez] (https://github.com/geraldinnebohr)  
[Hugo "Hache" Trujillo] (https://github.com/hacheG)
