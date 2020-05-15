from aip import AipOcr
import sys
APP_ID = '17723569'
API_KEY = 'nGtAgM9eiLvcZTG7h0YkZTk5'
SECRET_KEY = 'Xs5GWxd8CZON7fLKOgWlX5u8k2qco3h9'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content(sys.argv[1])

client =  AipOcr(APP_ID,API_KEY,SECRET_KEY)

print(client.basicGeneral(image))
print(client.basicAccurate(image))
print(client.general(image))
print(client.accurate(image))
print(client.enhancedGeneral(image))
print(client.webImage(image))
