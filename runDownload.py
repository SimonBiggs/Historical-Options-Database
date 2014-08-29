import os
import datetime

stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

outputDirectory = 'data/'+stamp

if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

os.environ["OUTPUTDIRECTORY"] = outputDirectory
os.system("runipy Historical\ Database.ipynb  --html "+outputDirectory+"/report.html", shell=True)
