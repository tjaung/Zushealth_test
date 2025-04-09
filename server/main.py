from PrivateNetwork import PrivateNetwork
from pprint import pprint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator

app = FastAPI()
pn = PrivateNetwork() # global var just for demo


origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Key(BaseModel):
    devices: list[str]
    
    # @field_validator("devices")
    # def check_atleast_two(cls, v):
    #      if not v or len(v) < 2:
    #           raise ValueError("Error: Must provide at least two devices")

@app.post("/add_key")
async def add_key(request: Key):
     print(request.devices)
     devices = tuple(request.devices)
     pn.add_key(devices)

     return {
        "networks": pn.get_networks(),
        "devices": pn.get_devices(),
        "next_network": pn.get_network_count()
     }

@app.get("/")
async def root():
        return run_network_demo()

def run_network_demo():
    pn.add_key(("Alice", "Bob")) # 1
    pn.add_key(("Alice", "Carlos")) # 2
    pn.add_key(("Alice", "David")) # 3
    pn.add_key(("Alice", "Bob", "Carlos", "David")) # 4
    pn.add_key(("Bob", "Carlos", "David")) # 5
    pn.add_key(("Bob", "Alice")) # 6 should print an error

    output = {
        "networks": pn.get_networks(),
        "devices": pn.get_devices(),
        "next_network": pn.get_network_count()
    }
    return output
