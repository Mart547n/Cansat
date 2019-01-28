# A file for helper functions
import time, os

def getTimeMiliSec():
   """ Returns the current time in miliseconds """
   return int(round(time.time() * 1000))

def logMsg(message = '', level = 'info'):
   """ Logs the message to the log """
   if (message != ''):
      # Get the path to the log file
      path = getPath(logName = 'log')
      with open(path, 'a+') as log:
         # Log the message
         log.write('[{0}]: {1}. \n'.format(level, message))
         print('[{0}]: {1}. \n'.format(level, message))

def getPath(logName = ''):
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
   path = os.path.dirname(os.path.realpath(__file__))
   path = path[:-3] + ('data\\{0}.txt'.format(category))
   # Open the file and return its content
   with open(path, 'r') as f:
      data = f.read()
      return data

if (__name__ == '__main__'):
   # Perform a test
   logMsg(message = 'det virker...', level = 'info')