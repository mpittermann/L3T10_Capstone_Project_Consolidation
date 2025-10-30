# Django Website Project


To run the program, clone or copy the repository to your local machine
Follow the instructions below for running the website using either
* Virtual Environment - venv
* Docker container

## venv

Be at the path where on your machine where you have your virtual machine setups.
(eg c:\VM\)

Run the following command to create the VM setup
**python -m venv mysite**

Then the following command to activate the VM
**mysite/Scripts/activate**

Next run the following command to install the necessary packages to run the program
(Ensure the command is run in the same folder as the stored requirements file)
**pip install -r requirements.txt**

To start the web server to produce the website run:
**python manage.py runserver**

Open your web browser and proceed to **http://127.0.0.1:8000**

Use ctr-c or ctrl-break to stop the server running.

## Docker

Use the following command to generate the Docker container
**docker build -t mysite ./**

Run the following command
**docker run -d -p 8000:8000 mysite**

Open your web browser and proceed to **http://localhost:8000**
