import time, os, glob
from datetime import datetime

class Logger: # This class is used to log the data ect.
   
   def getTimeMiliSec(self):
      """ Returns the current time in miliseconds """
      return int(round(time.time() * 1000))

   def logMsg(self, message = '', level = 'info'):
      """ Logs the message to the log """
      if (message != ''):
         # Get the path to the log file
         path = self.getPath(logName = 'log')
         with open(path, 'a+') as log:
            # Log the message
            log.write('[{0}]: {1}. \n'.format(level, message))

   def getPath(self, logName = ''):
      """ Returns the path to a datalog if the logName argument is = None then return the data path """ 
      if (logName != '' and logName != 'log'):
         # Returns the path to a specific log
         path = os.path.dirname(os.path.realpath(__file__))
         path = path[:-3] + ('data\\{0}.txt'.format(logName))
      elif (logName == 'log'):
         # Return the path to the log file
         path = os.path.dirname(os.path.realpath(__file__)) + '/{0}.txt'.format(logName)
      else:
         # Returns the path to the data directory
         path = os.path.dirname(os.path.realpath(__file__))
         path = path[:-3] + 'data'
      print('path to {0}: {1}'.format(logName, path))
      return path

   def readDataLog(self, category):
      """ Args:
            Category takes a string, can be ether one of these:
               (acc, temp, pre) 
      """
      # Save the data to the data diretory
      path = self.getPath(logName = category)
      # Open the file and return its content
      with open(path, 'r') as f:
         data = f.read()
         return data
   
   def resetData(self, logNames = ['log']):
      """ Resets the data logs (specified in the logNames list) """
      for logName in logNames:
         # Opens the log
         with open ("{0}.txt".format(logName), 'a') as log:
            if (logName == 'log'):
               log.write('Startup Time: {0}'.format(datetime.now().time()))
            else:
               # Dele everything in the log
               log.write('')

   def getCategories(self):
      """ Returns all of the categories """
      # Make a list of files 
      files = []
      for file in glob.glob("{0}\\*.txt".format(self.getPath())):
         files.append(file)
      
      # Create a categories lst
      categories = []
      for file in files:
         file = file[49:-4]
         categories.append(file)

      return categories 

   def saveData(self, category, time, data = 'None'):
      """ Args: 
            The data:
               (self exsplanitory) 
            Category takes a string, can be ether one of these:
               (acc, temp, pre), care if you use any other categories than these the program will save to a random file
      """
      if (type(data) == list or type(data) == tuple):
         # Format the data differently
         newData = [';' + (str(d)) for d in data]
         data = ''.join(newData)
      else:
         # Format the data in the regular way
         data = ';{0}'.format(str(data))

      path = self.getPath(category)
      try:
         with open(path, 'a+') as file:
            # Write the time and data to the datalog of the category specified
            file.write("{0}{1}\n".format(time, data))
      except IOError:
         # log the error if there is an error
         self.logMsg(message ='File Not Found...\n  {0}'.format(path), level = 'error')

if (__name__ == "__main__"):
   # Perform a test
   logger = Logger()
   logger.saveData("temp", time.time(), data="FUCK OF")