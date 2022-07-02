from fastapi import FastAPI

app = FastAPI()

# объявление роута
@app.get('/')
def index():
	return 'Hello from team app'