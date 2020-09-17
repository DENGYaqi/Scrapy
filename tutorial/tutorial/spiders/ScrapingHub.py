import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        
        # Title
        #for title in response.css('.post-header>h2'):
        #    yield {'title': title.css('a ::text').get()}

        # Text of Thumbnail page
        for text in response.css("div.post-content"):
            if (text.css("p::text").extract()) != [] or text.css("em::text").extract() != [] or text.css("i::text").extract() != [] or text.css("span::text").extract() != [] or text.css("a::text").extract() != []:
                yield{
                    'text' : text.css("p::text").extract(),
                    'linktext' : text.css("em::text").extract(),
                    'italictext' : text.css("i::text").extract(),
                    'spantext' : text.css("span::text").extract(),
                    'atext' : text.css("a::text").extract()
                }
            else:
                yield{
                    'text' : 'No synopsis'
                }

        # Nex page
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)