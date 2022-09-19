import requests
import os.path

def download(start_id:int, end_id:int, output_path:str):
    """downloads txt-files from zeitpunkt.nrw of a specific range of IDs

    :param start_id: first ID
    :type start_id: int
    :param end_id: last ID
    :type end_id: int
    :param output_path: output directory
    :type output_path: str
    """
  

    while  start_id <= end_id:

        # structure is a base url + ID, which redircts to a txt-file
        url = 'https://zeitpunkt.nrw/ulbbn/download/ftpack/plain/' + str(start_id)
        r = requests.get(url, allow_redirects=True)

        # some IDs aren't in use,  when getting 404 errors over a long period of time, it might make sense to interrupt the process and manually enter the ID of the next newspaper volume
        if r.status_code == 404:
            print("404: %s" %url)
            start_id+=1
            continue
        
        #generating the filename
        file_name = r.headers.get("Content-Disposition").split("filename=")[1]
        file_name = file_name.split("(")[-1]
        file_name = file_name.removesuffix(").txt\"")
        file_name_list = file_name.split(".") 
        file_path= "%s/%s" %(output_path, file_name_list[2])
        # it makes sense to integrate the ID into the filename, because on some days there have been two or more volumes
        file_name= "%s_%s_%s_%s.txt" %(file_name_list[2], file_name_list[1], file_name_list[0], start_id)
        
        #saving the downloaded file
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        if os.path.isfile("%s/%s" %(file_path, file_name)):
            print ("File %s from %s is already existing" %(file_name,url))
        else: 
            open("%s/%s" %(file_path, file_name), 'wb').write(r.content)
            print(file_name+" saved successfully!")

        # getting the next ID
        start_id+=1

    print("Done!")

if __name__ == '__main__':
    
    download(440975, 441375, "test")