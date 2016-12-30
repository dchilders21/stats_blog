print('Trying to create a post')
import requests

url = "http://127.0.0.1:8000/api/posts"
#client = requests.session()
#client.get(url)
csrftoken = requests.get(url).cookies['csrftoken']
#csrftoken = client.cookies['csrftoken']
#csrftoken = 'DK0b6yGb05PiIFJhPpzGSgV6kXhtaiiFXPKvUdHYCXcyjtlafJYudEGvLsx8bHaL'
print(csrftoken)
header = {'X-CSRFToken': csrftoken}
cookies = {'csrftoken': csrftoken}
payload = {
    'csrfmiddlewaretoken': csrftoken,
    'title': 'test_title',
    'content': 'test_content'
}

r = requests.post(url, data=payload, headers=header, cookies=cookies)