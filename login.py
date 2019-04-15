# Load proxies
proxies = []
proxies_fp = open('myproxies.txt', 'r') # A list of your proxies, use private ones!
for proxy in proxies_fp:
        proxies.append(proxy)


cookiejar = cookielib.CookieJar()

def perform_request(url, opener, credientials):
        # Instantiate our request object
        request = urllib2.Request(url)

        # Perform the request, returning a pointer to the result set.
        result = opener.urlopen(request, credentials)

        return result

credentials ={
        'username' : 'username',
        'password' : 'password'
        }

encoded_credentials = urllib.urlencode(credentials)

def main():
        # Get random proxy
        proxy = random.choice(proxies)

        # Install our proxy
        opener = urllib2.build_opener(
            urllib2.ProxyHandler({'http': proxy}),
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(cookiejar),
            )
        urllib2.install_opener(opener)
        a = perform_request(url, opener, encoded_credentials)
