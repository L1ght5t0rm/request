import requests

url=''


get={
    'key':'value',
}

cookies={
    'key':'value',
}

headers={
    'key':'value',
}

post={
    'key':'value',
}

#file

#post_file_path='path/to/your/local/file'
try:
    _=post_file_path
    filename=__import__('os').path.basename(post_file_path)
    with open(post_file_path,'rb') as f:
        files={'f':(filename,f.read())}
except NameError:
    post_file_path=None



def tget():
    x=requests.get(url,params=get,cookies=cookies,headers=headers)
    print('\n\nResponse:\n',x.text)
    print('\n\nResponse Cookies:\n\t',x.cookies.get_dict())
    print('\n\nResponse Headers:')
    for header,value in x.headers.items(): print(f'\t{header}: {value}')
    print(x.headers)

def tpost():
    if post_file_path:
        x=requests.post(url,params=get,data=post,cookies=cookies,headers=headers,files=files)
    else:
        x=requests.post(url,params=get,data=post,cookies=cookies,headers=headers)
    print('\n\nResponse:\n',x.text)
    print('\n\nResponse Cookies:\n\t',x.cookies.get_dict())
    print('Response Headers:')
    for header,value in x.headers.items(): print(f'{header}: {value}')
    print(x.headers)

try: tget()
except Exception as e: print(e)
print('='*40)
try: tpost()
except Exception as e: print(e)


