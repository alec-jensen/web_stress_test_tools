import web_stress_tools
import argparse
import logging


parser = argparse.ArgumentParser(description='Web Stress Tools')
parser.add_argument('-i', '--ip', help='Target IP', required=True)
parser.add_argument('-p', '--port', help='Target port',
                    required=True, type=int)
parser.add_argument('-t', '--threads', help='Number of threads',
                    required=False, type=int, default=4)
parser.add_argument('-m', '--method', help='Method',
                    required=True, choices=['syn'])
parser.add_argument('-v', '--verbose', help='Verbose',
                    required=False, action='store_true', default=False)

args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

if args.method == 'syn':
    web_stress_tools.syn(args.ip, int(args.port), int(args.threads))
