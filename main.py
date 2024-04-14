from flask import Flask, render_template, request
import pickle as pk
from urllib.parse import urlparse
import whois
import socket
import ssl
import requests
import tldextract
import datetime
import dns.resolver

application = Flask(__name__)
model = pk.load(open('mymodel.pkl', 'rb'))


def count_slash_url(url):
    return url.count('/')

def count_underline_directory(url):
    return url.count('_')

def file_length(url):
    parsed_url = urlparse(url)
    return len(parsed_url.path.split('/')[-1])

def length_url(url):
    return len(url)

def time_domain_activation(domain):
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        activation_duration = datetime.datetime.now() - creation_date
        return activation_duration.days
    except:
        return None

def count_dot_domain(domain):
    return domain.count('.')

def asn_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        asn_info = requests.get(f'https://api.iptoasn.com/v1/as/ip/{ip_address}')
        return asn_info.json()['as_number']
    except:
        return None

def ttl_hostname(domain):
    try:
        ttl = dns.resolver.resolve(domain, 'A').rrset.ttl
        return ttl
    except:
        return None

def time_domain_expiration(domain):
    try:
        domain_info = whois.whois(domain)
        expiration_date = domain_info.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        expiration_duration = expiration_date - datetime.datetime.now()
        return expiration_duration.days
    except:
        return None

def time_response(url):
    try:
        response = requests.get(url)
        return response.elapsed.total_seconds()
    except:
        return None

def count_hyphen_url(url):
    return url.count('-')

def count_percent_params(url):
    return url.count('%')

def count_vowels_domain(domain):
    vowels = 'aeiou'
    return sum(1 for char in domain if char in vowels)

def count_hyphen_params(url):
    return urlparse(url).query.count('-')

def count_dot_url(url):
    return urlparse(url).netloc.count('.')

def count_equal_url(url):
    return urlparse(url).query.count('=')

def count_nameservers(domain):
    try:
        return len(dns.resolver.resolve(domain, 'NS'))
    except:
        return None

def count_mx_servers(domain):
    try:
        return len(dns.resolver.resolve(domain, 'MX'))
    except:
        return None

def count_ip_resolved(domain):
    try:
        return len(socket.gethostbyname_ex(domain)[-1])
    except:
        return None

def count_slash_params(url):
    return urlparse(url).query.count('/')

def count_redirects(url):
    try:
        response = requests.get(url)
        return len(response.history)
    except:
        return None

def count_tld_url(url):
    extracted = tldextract.extract(url)
    # Sum the lengths of subdomain, domain, and suffix parts
    return len(extracted.subdomain) + len(extracted.domain) + len(extracted.suffix)

   

def tls_ssl_certification(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return ssl.DER_cert_to_PEM_cert(cert)
    except:
        return None

def count_underline_url(url):
    return url.count('_')

def domain_spf(domain):
    try:
        records = dns.resolver.resolve(domain, 'TXT')
        for record in records:
            if 'v=spf1' in record.strings[0]:
                return True
        return False
    except:
        return False

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        url = request.form.get('url')
        domain = urlparse(url).netloc
    
    features = {
        "qty_slash_url": count_slash_url(url),
        "qty_underline_directory": count_underline_directory(url),
        "file_length": file_length(url),
        "length_url": length_url(url),
        "time_domain_activation": time_domain_activation(domain),
        "qty_dot_domain": count_dot_domain(domain),
        "asn_ip": asn_ip(domain),
        "ttl_hostname": ttl_hostname(domain),
        "time_domain_expiration": time_domain_expiration(domain),
        "time_response": time_response(url),
        "qty_hyphen_url": count_hyphen_url(url),
        "qty_percent_params": count_percent_params(url),
        "qty_vowels_domain": count_vowels_domain(domain),
        "qty_hyphen_params": count_hyphen_params(url),
        "qty_dot_url": count_dot_url(url),
        "qty_equal_url": count_equal_url(url),
        "qty_nameservers": count_nameservers(domain),
        "qty_mx_servers": count_mx_servers(domain),
        "qty_ip_resolved": count_ip_resolved(domain),
        "qty_slash_params": count_slash_params(url),
        "qty_redirects": count_redirects(url),
        "qty_tld_url": count_tld_url(url),
        "tls_ssl_certification": tls_ssl_certification(domain),
        "qty_underline_url": count_underline_url(url),
        "domain_spf": domain_spf(domain),
    }
    import numpy as np
    feature_values = [value for value in features.values()]
    feature_values_reshaped = np.array(feature_values).reshape(1, -1)

    prediction =model.predict(feature_values_reshaped)[0]
    if prediction==1:
        return render_template('index.html', prediction_text=f'The website is malicious')
    elif prediction==0:
        return render_template('index.html', prediction_text=f'The website is malicious')

if __name__ == '__main__':
    application.run(debug=True)
