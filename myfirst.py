from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {
        "aws": {
        
           "instance-id": "t2.micro", 
           "ami-id":"amixxxxxxxxxxxxx",
           "region": "us-east-1"
           "name": "myec2instance"
                }
                
            }

