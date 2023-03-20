import os
from zipfile import ZipFile
# Create a ZipFile Object
with ZipFile('C:/project/python/System/huruf2.zip', 'w') as zip_object:
   # Adding files that need to be zipped
   zip_object.write('b.txt')
   zip_object.write('a.txt')

# Check to see if the zip file is created
if os.path.exists('C:/project/python/System/huruf.zip'):
   print("ZIP file created")
else:
   print("ZIP file not created")