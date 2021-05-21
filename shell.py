import requests

path = input('enter image path >>');

response = requests.post(
    'https://api.remove.bg/v1.0/removebg?',
    files={'image_file': open(path, 'rb')},
    data={'size': 'auto', 'bg_color': '#ffffff'},
    headers={'X-Api-Key': 'MF8X99DWyaPjzLRx5qXNpFqN'},
)

image_name = input("enter image name >>");
if response.status_code == requests.codes.ok:
    with open(image_name + '.jpg', 'wb') as out:
        out.write(response.content)
        print("wow! background removed!!!")
else:
    print("Error:", response.status_code, response.text)
