from flask import Flask, send_file
from data import dataHandler
import socket

# The data handler object
dH = dataHandler(r = False)

# The file server implementation
app = Flask(__name__)

@app.route('/download/<category>')
def download(category, methods = ['POST']):
   if (category in dH.categories):
      # Download the .txt file
         path = dH.getPath(category)
         return send_file(path, attachment_filename = '{0}.txt'.format(category))
   else:
      # Trow an error
      return 'Wooooops that was not a correct category please reload with a new url...'

if (__name__ == "__main__"):
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8", 80))
   ip = s.getsockname()[0]
   s.close()
   print('server is running... on {0}:5000'.format(ip))
   app.run(debug = True, port = 5000, host = ip)