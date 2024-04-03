My computer's python version 3.11.3. Using Windows operating system. Visual Studio code editor

Installation/Setup:
I use vs terminal
* Setup virtual environment
	python -m venv venv (venv is the name of virtual environment. You can use your own)
* Activate virtual environment 
	venv\Scripts\activate.ps1
* Install necessary module using follwing command
	pip install fastapi sqlalchemy uvicorn psycopg2 pydantic pydantic[email] httpx requests
		OR
	Simple type pip install -r requirements.txt as I freeze all of these follwing installation
	
	python.exe -m pip install --upgrade pip
* For run app use follwing command
	uvicorn main:app --reload
type or click from editor terminal
http://127.0.0.1:8000/docs

Test API:
In this above link there is 2 option
1. User is generate the password based on given length.
	*Get Request
	*Post Request(Generate-Password based on length. Length value should be 6 or more as
	I use some of condition for strong password. Also I add another email field. Valid email formate required)
	Click postrequest section /generate-password then
	click try it out
	give an valid email formate in email field and an integer value must greter than 6
	then click on execute button
Input:
Email: lizaakter@gmail.com
Length: 8

output:
{
  "Email": "lizaakter@gmail.com",
  "password": "8kvQuTNe",
  "length": 8
}
2. Integrate a third-party API using open weathermap api.
	Show some of current data for London city.
Click on this GET/openweatherapi/
then Try it Out then click Execute 
	
Output:
{
  "city": "London",
  "Temperature": "10.04",
  "Humidity": "92%",
  "Wind Speed": 2.57,
  "Description": "overcast clouds"
}



Error Handling: For invalid input
Email should be unique and followed by valid email formate
	In this api I use EmailStr for validation. This is from pydantic import EmailStr
Password length should be at least 6. At this moment I generate a random secure password. Output password contains random character and digit.
	When I will implement user login that time I will use password hasing and json web token authentication.	
