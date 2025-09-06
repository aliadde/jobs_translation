import subprocess 

# extracty jobs link from first page of OMAN
print("__eaking first page links jobs\n")
subprocess.run('pytest naukrigulf_oman.py  --uc --chrome    --binary-location="/usr/bin/google-chrome"  -s',shell=True)
print("__first page links leaked \n")
# extract data from eeach job
print("__ START extract data from each jobs link \n ")
subprocess.run('pytest extract.py  --uc --chrome    --binary-location="/usr/bin/google-chrome"  -s',shell=True)
print("__DONE all job's links data extracted and stored in jason file \n ")
# translate each job to persian
print("__START translating each job and store in ne json file \n")
subprocess.run('pytest google_translation.py  --uc --chrome    --binary-location="/usr/bin/google-chrome"  -s',shell=True)
print("__DONE translating\n \n \tGOOD LOCK!\t \n  ")
