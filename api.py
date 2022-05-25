from fastapi import FastAPI
import uvicorn

# create a FastAPI instance
app = FastAPI()


# create a path operation
@app.get('/get_qr')
# define the path operation function
def root():
	return {'message': 'qr_data'}


if __name__ == "__main__":
	uvicorn.run('api:app', port=80)
