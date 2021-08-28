import urllib.request,json
from .model import Post
import requests
def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']


def new_post(endpoint, post):
    posts_url = base_url.format(endpoint)
    print(posts_url)
    print(post)
    result=requests.post(posts_url, json=post)
    print(result)



def get_posts(endpoint):
    '''
    Function that gets the json response to our url request
    '''
    get_post_url = base_url.format(endpoint)
    print(get_post_url)
    with urllib.request.urlopen(get_post_url) as url:
        get_data = url.read()
        response = json.loads(get_data)
        if response['data']:
            # results_list = response['data']
            results = response['data']
    print(results)           
            # results = process_pitches(results_list)  
    return results