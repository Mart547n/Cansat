# CanSat
The CanSat Libary is used on our raspberry zero w

# File Structure
The Cansat project has two main folders data and src a subfolder of is the lib folder, this contains the libaryes used to comunicate with the different sensors etc, the src folder also contains a cupple of python files like data.py (for handeling data) and main.py for runing the intere project as well as the small file server runing in the background.

# The File Server
The File server is build with flask, you can "download" the data by going to the ip of the host computer and giving it the following port for exsample 'http://localhost:5000/download/acc' returns a blank page with the acceleration data
