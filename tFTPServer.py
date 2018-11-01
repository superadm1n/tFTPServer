'''
Copyright 2018 Kyle Kowalczyk
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Basic HTTP server written in python to serve static web pages
'''

import tftpy
import argparse
import os

parser = argparse.ArgumentParser("tFTPServer.py")
parser.add_argument("--port", help="Port to serve on (Default: 8000)", type=int)
parser.add_argument("--ipaddr", help="IP Address to serve on (Default: 127.0.0.1)", type=str)
parser.add_argument("--dir", help="Directory to serve (Default will serve the directory the file is in)", type=str)
args = parser.parse_args()

if not args.port:
    port = 69
else:
    port = args.port

if not args.ipaddr:
    ipaddr = '0.0.0.0'
else:
    ipaddr = args.ipaddr

if not args.dir:
    dir = os.path.dirname(os.path.abspath(__file__))
else:
    dir = args.dir


try:
    print('Serving directory "{}" on port {} listening on address {}'.format(dir, port, ipaddr))
    server = tftpy.TftpServer(dir)
    server.listen(ipaddr, port)
except KeyboardInterrupt:
    print('Stopping Server')
    server.stop(now=True)
