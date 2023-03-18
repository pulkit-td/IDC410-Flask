# IDC410 - Flask
## _Requirements_

----

**Clone above repository using the command**
- git clone _git@github.com:pulkit-td/IDC410-Flask.git_

**_or_ Download the code**
- Click on Code
- Click on Download ZIP 

----

**Python Dependencies**

- flask
- scikit-learn

To install these dependencies, run _**pip install -r requirements.txt**_

----

**Install Postman**

Download and install postman from https://www.postman.com/downloads/

----

**How to Run Flask serve and call REST api**

- Run the flask server (We are assuming that the server is running locally and port is 5000)
  1. Naviagte to root of the cloned repo.
  2. Run **pip install -r requirements.txt** to install dependencies.
  3. Run **python app.py** or **python3 app.py** (the server is now running on **localhost:5000**)
  
  Note - You have to run step 2 only once in a python env.
  
- Open Postman
  1. Click on New
  2. Click on HTTP Request
  3. Select required request method
  4. Enter the request URL eg. localhost:5000/health_check
  5. Enter the request payload according to your request.
