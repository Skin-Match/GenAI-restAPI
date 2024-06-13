
# Generative AI API

Rest API made by Flask, for generative AI model used for Skin Match App.


## Setup

Here is how to setup the api to run locally on your computer.

**1. Make Environment on Your Local Computer**

On cmd, use this command:
```bash
  cd "your/folder/project/path"
```
```bash
  python venv env
```
```bash
  cd env
```
```bash
  cd Scripts
```
```bash
  cd Activate.bat
```
Go in to your project folder directory
```bash
  cd ..
```
```bash
  code .
```

**2. Clone This Repository and Customize**

a. Change the project ID and location according to your own project.

b. Go to your GCP, make a service account with roles of:
```bash
  Vertex AI User
  Storage Object Viewer
```
c. Get the key in json.

d. Save the key in credential folder, or any seperate folder.

e. Change the credential path in the app.py.

**3. Install Dependencies**
```bash
    pip install -r requirements.txt
```

**4. Run**
```bash
    python app.py
```
