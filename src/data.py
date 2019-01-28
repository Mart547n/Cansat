import os, glob
from datetime import datetime
from HF import getPath, logMsg

def resetData(logNames = ['log']):
   """ Resets the data logs (specified in the logNames list) """
   for logName in logNames:
      # Opens the log
      with open ("{0}.txt".format(logName), 'w') as log:
         if (logName == 'log'):
            log.write('Startup Time: {0}'.format(datetime.now().time()))
         else:
            # Dele everything in the log
            log.write('')

def getCategories():
   """ Returns all of the categories """
   # Make a list of files 
   files = []
   for file in glob.glob("{0}\\*.txt".format(getPath())):
      files.append(file)
   
   # Create a categories lst
   categories = []
   for file in files:
      file = file[49:-4]
      categories.append(file)

   return categories 

def saveData(category, time, data = 'None'):
   """ Args: 
         The data:
            (self exsplanitory) 
         Category takes a string, can be ether one of these:
            (acc, temp, pre), care if you use any other categories than these the program will save to a random file
   """
   if (type(data) == list or tuple):
      # Format the data differently
      newData = [';' + (str(d)) for d in data]
      data = ''.join(newData)
   else:
      # Format the data in the regular way
      data = ';{0}'.format(str(data))

   path = getPath(category)
   try:
      with open(path, 'a+') as file:
         # Write the time and data to the datalog of the category specified
         file.write("{0}{1}\n".format(time, data))
   except IOError:
      # log the error if there is an error
      logMsg(message ='File Not Found...\n  {0}'.format(path), level = 'error')
   