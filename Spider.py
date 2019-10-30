from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

    # Class Vaiables (shared among all instances)
    project_name = ''
    base_url = ''
    damain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self , project_name , base_url , domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.damain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(directory= Spider.project_name)
        create_data_files(project_name=Spider.project_name , base_url=Spider.base_url)
        Spider.queue = file_to_set(file_name=Spider.queue_file)
        Spider.crawled = file_to_set(file_name=Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name , page_url):
        """
        ye tabe ke name thread & relative addres webpage ro migireh va ba komak method gather_link tamam link haye crawl mikone
        va safhaye queue & crawl ro update mikone
        vaziate har thread ro niz print mikoneh
        :param thread_name:
        :param page_url: the relative address of webpage
        :return:
        """
        if page_url not in Spider.crawled :
            print(thread_name + ' now crawling '+page_url)
            print('Queue :'+ str(len(Spider.queue)) + ' | Crawled :'+str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        """
        ye tabe ke addrese web ro migireh va ba estefadeh az class LINKFINDER tamam link haye on addres ro da ghalabe SET pass mide
        :param page_url: the relative address of webpage
        :return: a SET of links
        """
        html_string = ''
        try:
            response =urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url , page_url)
            finder.feed(html_string)
        except:
            print(' Error : can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue : continue
            if url in Spider.crawled : continue
            if Spider.damain_name not in url : continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_fo_file(Spider.queue,Spider.queue_file)
        set_fo_file(Spider.crawled,Spider.crawled_file)
