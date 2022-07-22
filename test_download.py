import requests
import os.path

start_id=428015

end_id=428260

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
    
    filepath= "%s/%s_%s_%s_%s.txt" %(output_path, filename_list[2], filename_list[1], filename_list[0], start_id)

    if os.path.isfile(filepath):
        # volume = filename.split("1887-1932 ")[1]
        # volume = volume.split(" (")[0]
        print ("File %s from %s is already existing" %(filepath,url))
        #filepath += "_"+volume
    open('%s/%s' %(filename_list[2], filepath), 'wb').write(r.content)
    print(filepath+" saved successfully!")
    start_id+=1

print("Done!")

