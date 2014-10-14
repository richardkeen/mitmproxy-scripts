import signal
import sys
from libmproxy.flow import Response
from collections import Counter, OrderedDict
import csv

http_hosts = Counter()

def request(context, flow):
    path = flow.request.path
    if flow.request.scheme != 'https':
        http_hosts[flow.request.host] += 1
        
def exit_handler(signum, frame):
    with open('http_audit.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        sorted_http_hosts = OrderedDict(sorted(http_hosts.items(), key=lambda t: t[1], reverse=True))
        for host, count in sorted_http_hosts.iteritems():
            writer.writerow([host, count])

    print '\nResults in http_audit.csv'
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)