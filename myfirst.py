from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def blog_list():
    return {"Name": "Nagendra"}

@app.get('/contactus')
def get_sravan():
    return 'Hello please reach us at sravan@gmail.com'

@app.get('/blog/1')
def blog_id():
  return {'data':1}

@app.get('/blog/2')
def blog_id():
    return {'data':2}


#when /blog/unpublished is placed below here it doesnt throws error

@app.get('/blog/unpublished')   
def unpublished():
    return {'data':'unpublished blogs list'}

@app.get('/blog/{id}')
def blog_id_dynamically(id: int):
    return {'data':id}
# when /blog/unpublished is placed below here it throws error
# @app.get('/blog/unpublished')   
# def unpublished():
#     return {'data':'unpublished blogs list'}

@app.get('/root')
def read_root():
    return {
        "aws": {
        
           "instance-id": "t2.micro", 
           "ami-id":"amixxxxxxxxxxxxx",
           "region": "us-east-1",
           "name": "myec2instance"
                }
                
            }

@app.get('/about')
def about():
    return {'data': 'about page'}

users = []

@app.get('/users')
async def users_list():
    return users

@app.post('/users')
async def create_user(user):
    users.append(user)
    return "success"

