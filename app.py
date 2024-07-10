from fastapi import FastAPI
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class CloudVendors(str, Enum):
    aws = "aws"
    azure = "azure"
    gcp = "gcp"

cloudevendors = {


    'aws'  : ["ec2", "s3"],
    'azure' : ["vm", "vnet"],
    'gcp' : ["gcr", "gke"]
}

app = FastAPI()
@app.get("/home")
async def home():
    return "welcome home:"

@app.get("/courses/{coursename}")
async def courses(coursename: CloudVendors):
    #return f"{coursename} is the opted course"
    return cloudevendors.get(coursename)



@app.get("/payments")
async def payments():
    return "please complete the payments"

@app.get("/workshops")
async def workshops():
    return "welcome to workshop of master classs Terraform"


