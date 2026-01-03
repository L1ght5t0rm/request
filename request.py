#!/usr/bin/env python3
import requests,re

url=''
pattern=r'<input type="hidden" name="token" value="([^"]+)"'
# pattern=r"aa(.+?)aa"

get={
    'key':'value',
}

cookies={
    'key':'value',
}

headers={
    'key':'value',
    # 'Content-Type':'application/json',
}

post={
    'key':'value',
}

json={
    'key':'value',
}

#post_file_path='path/to/your/local/file'
try:
    _=post_file_path
    filename=__import__('os').path.basename(post_file_path)
    with open(post_file_path,'rb') as f:
        files={'f':(filename,f.read())}
except NameError:
    post_file_path=None
    files=None


def tget() -> 'Response':
    response=requests.get(url,params=get,cookies=cookies,headers=headers)
    return response

def tpost(files=files) -> 'Response':
    if files: response=requests.post(url,params=get,data=post,cookies=cookies,headers=headers,json=json,files=files)
    else: response=requests.post(url,params=get,data=post,cookies=cookies,headers=headers,json=json)
    return response

def parse(response:'Response',debug=False) -> 'dict,str':
    '''Return the response.json(dict) or response.text(str).'''
    if debug:
        detailed(response)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        # Automatic analysis of encoding format for apparent_encoding.
        return response.content.decode(response.apparent_encoding)

def match(response:'Response'):
    content=response.content.decode(response.apparent_encoding) # or use json
    match=re.search(pattern,content)
    if match:
        return match.group(1)
    else:
        detailed(response)
        raise ValueError('No match.')

def detailed(response:'Response'):
    '''Print Details.'''
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError as e:
        print('\nResponse:\n',response.content.decode(response.apparent_encoding))
        print('\nResponse Cookies:\n\t',response.cookies.get_dict())
        print('Response Headers:')
        for header,value in response.headers.items(): print(f'\t{header}: {value}')

# session=requests.Session()
# session.get(url)
# session.post(url,data)

print(parse(tget(),debug=True))
print('='*40)
print(parse(tpost()))





