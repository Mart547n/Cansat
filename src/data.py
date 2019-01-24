import os
import glob
import time

class dataHandler:
   
   def __init__ (self):
      # Initalise the handler
      self.categories = self.getCategories()
      self.miliTime = lambda: int(round(time.time() * 1000))
      self.startTime = self.miliTime()

   def getCategories(self):
      """ gets the categories """
      # Go to the data path
      path = os.path.dirname(os.path.realpath(__file__))
      path = path[:-3] + ('data')

      # Make a list of files
      files = []
      for file in glob.glob("{0}\\*.txt".format(path)):
         files.append(file)
         
      categories = []
      # Modify the list to return the names of the catecories only
      for file in files:
         file = file[49:-4] # Remove the .txt exstention and the path
         categories.append(file)

      return categories

   def saveData(self, category, data = 'None'):
      """ Args: 
          The data:
             (self exsplanitory) 
          Category takes a string, can be ether one of these:
             (acc, temp, pre), care if you use any other categories than these the program will save to a random file
      """
      # Take care of the fact that data can have a different type rather then sting
      if (type(data) == list):
         # Format the data differently
         newData = [';' + (str(d)) for d in data]
         data = ''.join(newData)
         print(data)
      else:
         data = ';{0}'.format(str(data))

      # Save the data to the data diretory
      path = os.path.dirname(os.path.realpath(__file__))
      path = path[:-3] + ('data\\{0}.txt'.format(category))
      try:
         with open(path, 'a') as file:
            # Write to the file time first then the values
            file.write("{0}{1}\n".format((self.miliTime() - self.startTime), data))
      except IOError:
         # Log the error
         print('\nFile Not Found...\n  {0}'.format(path))

   def sendData(self):
      # TODO: Create this function
      pass

if (__name__ == '__main__'):
   # It works 
   dataH = dataHandler()
   dataH.saveData(category='acc', data=[2, 2])