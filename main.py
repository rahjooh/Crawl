import threading
from queue import Queue
from Spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

#thread queue
queue  = Queue()

Spider(project_name=PROJECT_NAME,base_url=HOMEPAGE,domain_name=DOMAIN_NAME)
