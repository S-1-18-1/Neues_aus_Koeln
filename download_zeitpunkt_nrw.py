import requests
import os.path

start_id=440975 

end_id=441375

output_path = "data"

while  start_id <= end_id:
    url = 'https://zeitpunkt.nrw/ulbbn/download/ftpack/plain/' + str(start_id)
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 404:
        print("404: %s" %url)
        start_id+=1
        continue
    
    filename = r.headers.get("Content-Disposition").split("filename=")[1]
    filename = filename.split("(")[-1]
    filename = filename.removesuffix(").txt\"")
    filename_list = filename.split(".")
    
    filepath= "%s/%s" %(output_path, filename_list[2])
    filename= "%s_%s_%s_%s.txt" %(filename_list[2], filename_list[1], filename_list[0], start_id)
    
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    if os.path.isfile("%s/%s" %(filepath, filename)):
        print ("File %s from %s is already existing" %(filename,url))
    else: 
        open("%s/%s" %(filepath, filename), 'wb').write(r.content)
        print(filename+" saved successfully!")
    start_id+=1

print("Done!")

