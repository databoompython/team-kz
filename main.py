from fastapi import FastAPI

app = FastAPI()

# объявление роута
@app.get('/')
def index():
	return 'Hello from team app'

@app.get('/about')
def about():
	return 'This our my start-up'


@app.get('/team')
def my_team():
	team = {
	  "Helen": {
	    "department": "Management",
	    "age": 21,
	    "salary": 1500000
	  },
	  "Ali": {
	    "department": "Design",
	    "age": 25
	  },
	  "Katya": {
	    "department": "IT",
	    "age": 26
	  },
	  "Polina": {
	    "department": "Designer",
	    "age": 21,
	    "salary": 1500000,
	    "alumni": "NU"
	  }
	}
	
	return team

#@aap.get('/team/{team}')