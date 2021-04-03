import requests
import json
def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776
   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)
#Environment variable
myToken = XYZ
repo_name_URL = 'https://hub.docker.com/v2/repositories/<>/'
head = {'token': f'{myToken}'}
response = requests.get(repo_name_URL, headers=head, verify=True)
for_repo_name=response.json()
#initialize your list 
repoList = []
for s in for_repo_name['results']:
    name = s['name']
    repoList.append(name)
print(repoList)
#list the sizes of the images
image_tag_url = 'https://hub.docker.com/v2/repositories/<>/%s/tags/'
total = 0
for i in repoList:
    url = image_tag_url % i
    print("Repo name",i)
    response = requests.get(url, headers=head)
    image_sizes=response.json()
    image_size_list = []
    for s in image_sizes['results']:
        name = s['full_size']
        image_size_list.append(name)
        #total = sum(image_size_list)
    for j in image_size_list:
        total+=j
    print(humanbytes(sum(image_size_list))) 
print("Total of all image sizes: ", humanbytes(total))  