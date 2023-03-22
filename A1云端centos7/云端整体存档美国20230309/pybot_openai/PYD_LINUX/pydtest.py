
import openai
import platform
import operator
import importlib
import sys,os

currentDir = os.getcwd()
os.chdir('..') # .. to go back one dir | you can do "../aFolderYouWant"
sys.path.insert(0, os.getcwd())

systemname = platform.platform()
systembits = platform.architecture()
if (operator.eq(('64bit', 'WindowsPE'),systembits)):
    pyddir="PYD_WIN_AMD64" #pyddir="PYD_WIN_X86"
elif (('64bit', 'ELF') == systembits ):
    pyddir="PYD_LINUX"
else: #苹果('64bit', '')
    pyddir="PYD_OTHERS"
print(systembits)
print(pyddir)

pybot_openai_key = importlib.import_module(pyddir+".pybot_openai_key")

os.chdir(currentDir) # to go back to your home directory

key = pybot_openai_key.apikey() #


print(key)
