from scrapy import Spider ,Request

class BlogSpider(Spider):
    name = 'bloggy'
    start_url=['https://blog.Scrapinghub.com']

    def parse(self , response):

        area = response.css('div.post-listing')

        for article in area.css('div.post-item'):
            title = article.css('h2 a::text').extract_first()
            date = article.css('span.date a::text').extract_first()
            author = article.css('span.author a::text').extract_first()
            comment = article.css('span.custom_listing_comments a::text').extract_first()

            yield{
                'title' : title, 
                'date' : date,
                'author' : author,
                'comment' : comment,
            }
            url = response.css('a.next-posts-links:attr(href)').extract_first()
            if url:
                yield Request(url,callback=self.parse)
            #run
            #scrapy runspider mscrapy.py -o blog.csv
