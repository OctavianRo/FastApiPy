# creating virtual environment
py -3 -m venv venv

### Make sure that we are using the correct python exe file


###  We use Uvicor to get the app up and running
uvicorn app.main:app --reload

To check if we can access the API from google.com and if we have resolved the CORS policy 
fetch('http://localhost:8000').then(res => res.json()).then(console.log)