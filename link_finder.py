from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    # ye class baraye biron keshidane link haye ye address web dar ghalebe SET
    def __init__(self,base_url,page_url):
        """
        :param base_url: the home page main address
        :param page_url: the relative address which we need to parse
        self.links :  the sublinks which exist in the page_url
        """
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        """
        a funcion for add all links
        :param tag: the tag to parse
        :param attrs: all attributes to parse
        :return:
        """
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

finder = LinkFinder()
finder.feed("""<!DOCTYPE html>
<html>
<body>

<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>

</body>
</html>
""")