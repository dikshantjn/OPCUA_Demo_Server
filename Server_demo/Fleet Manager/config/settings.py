"""
This file contains configuration settings for the Robot Manager module, such as the server address and port.
"""

import os

# set default environment variables
os.environ.setdefault('SERVER_HOST', 'localhost')
os.environ.setdefault('SERVER_PORT', '4840')
os.environ.setdefault('SERVER_NAMESPACE', 'SwiftCurrent')

# read environment variables
SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])
SERVER_NAMESPACE = os.environ['SERVER_NAMESPACE']