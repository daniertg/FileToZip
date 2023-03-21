import os
from zipfile import ZipFile

# ambil input dari pengguna
num_files = int(input("Masukkan jumlah file yang ingin ditulis: "))

# buat list kosong untuk menampung nama file yang akan ditulis
filenames = []

# loop untuk meminta input nama file dari pengguna
for i in range(num_files):
    filename = input(f"Masukkan nama file ke-{i+1}: ")
    filenames.append(filename)

# buat object zip file
with ZipFile('C:/project/python/System/huruf3.zip', 'w') as zip_object:

    # loop untuk menulis setiap file ke dalam zip
    for filename in filenames:
        with open(filename, 'w') as f:
            f.write(f"Ini adalah isi file {filename}")

        zip_object.write(filename)

# Check to see if the zip file is created
if os.path.exists('C:/project/python/System/huruf3.zip'):
   print("ZIP file created")
else:
   print("ZIP file not created")