import os,pathlib
print(os.path.realpath(__file__))
print(pathlib.Path(__file__))
print(os.path.realpath('.'))
print(pathlib.Path('.'))