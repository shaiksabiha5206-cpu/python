#virtual environmnt means you are own kitchen to install this python -m venv show
#to activate this show\Scripts\activate
#.gitginore file means to ignore our files 
#keep .env file in that our apis then keep it in .gitignore file
#to need to know our api we must have to install pip install python-dotenv

#typing
#age:int=21
#college:str="srit"
#dataclasses
#from dataclasses import dataclass
#from typing import List
#@dataclass
#class User:
   # age:int
 #
 #    marks:List[int]
#u = User(age="twenty",marks=[89,90,78])
#print(u)
#to check this pydantic come
#from dataclasses import dataclass
#from pydantic import BaseModel
#from typing import List,Literal,Field
#class Use(BaseModel):
 #   name:str=Field(...,min_length=7)
  #  age:int=Field(...,ge=20,le=10)
   # marks:List[int]
    #grade:Literal["a","b"]
#u = Use(name="SABIHAS",age=20,marks=[78,90,89,90],grade="a")
#print(u)
print("hello ")
import os
from dotenv import load_dotenv
load_dotenv()
password=os.getenv("password")
api_key=os.getenv("api_key")
print(f"hello{password} {api_key}")
