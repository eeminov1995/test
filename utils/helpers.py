from flask import current_app

def add_header(response):
    if 'text/html' in response.headers['Content-Type']:
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
    else:
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Content-Type'] = 'application/json'
    return response
