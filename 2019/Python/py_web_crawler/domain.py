from urllib.parse import urlparse


# Get domain name(exmple.com)

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name(name.exmple.com)

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

# print(get_domain_name('https://stackoverflow.com/questions/71151/html-parser-in-python')) #To test