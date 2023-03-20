import zipfile
import os

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('c.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir("C:/project/python/System/b.txt", zipf)
    zipdir('C:/project/python/System/a.txt', zipf)
    zipf.close()