from fastapi import FastAPI

app = FastAPI()

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

# объявление роута
@app.get('/')
def index():
	return 'Hello from team app'

@app.get('/about')
def about():
	return 'This our my start-up'


@app.get('/team')
def my_team():
	return team

@app.get('/team/{name}')
def team_detail(name):
	name = name.capitalize()

	if name in team:
		return team[name]
	else:
		return 'К сожалению нет такого пользователя, но вы всегда можете зарегистрироваться у нас по ссылке <ссылка>'