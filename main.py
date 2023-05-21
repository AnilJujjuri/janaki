import uvicorn
from app import app
from sr import sr



if __name__=="__main__":
    uvicorn.run(sr, host='localhost', port=8095)
    uvicorn.run(app, host='localhost', port=8095)
