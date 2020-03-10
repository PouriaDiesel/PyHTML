from functions import *

if __name__ == '__main__':
    django_init()
    render_a_html('index.html', 'RenderedIndex.html', {"title": "HelloWorld!", "text": "Hello World!"})
