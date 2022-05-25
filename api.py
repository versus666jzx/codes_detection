import fastapi
import uvicorn

# import FastAPI
from fastapi import FastAPI

# create a FastAPI instance
app = FastAPI()


# create a path operation
@app.get('/get_qr')
# define the path operation function
def root():
	return {'message': 'qr_data'}