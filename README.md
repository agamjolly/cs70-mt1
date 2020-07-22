# CS70 MT1 Unofficial Statistics 
Unofficial crowdsourced statistics for CS70 Summer 2020 Midterm 1.

## Data
The data for this form was collected using Google Forms and assembled in an Excel file. This file was then imported into Python and cleaned using Pandas. 

## Installing Dependencies
All dependencies for the app can be installed using the `requirements.txt` file located in the root of the directory.

To install dependencies, run 
```bash
pip3 install -r requirements.txt
```

To run the app, simply run the `main.py` file after installing all dependencies. 

Alternatively, you could follow the deployment steps given below and skip everything.

## Deploying
Make sure you have Docker installed on your VPS server/local machine. 

To build a Docker image, run
```bash
docker build -t cs70 .
```

Now to mount the image and run locally till the CLI process ends, run
```bash
docker run -p 80:80 cs70
```

On a VPS, run the following to run the container in the background. 
```bash
docker run -d --restart unless-stopped -p 80:80 cs70
```

<h6>Developed by <a href="www.aagamjolly.com">Agam Jolly</a> :D</h6>
