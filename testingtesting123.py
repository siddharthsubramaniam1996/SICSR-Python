import os

directory = '/home/siddharth/Desktop/ssss/'

[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '_').lower()) for f in os.listdir(directory)]
