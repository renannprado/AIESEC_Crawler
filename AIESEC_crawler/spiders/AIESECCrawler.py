# -*- coding: utf-8 -*-
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

__author__ = 'renann'


class AIESECCrawler(CrawlSpider):
    name = "AIESECCrawler"
    allowed_domains = ["myaiesec.net"]
    #allowed_domains = ["localhost"]
    login_url = "http://myaiesec.net/login.do"
    start_urls = [
        "http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=25.02.2000&date_to=25.02.2020&regions=13427109&subRegionsId=13429306&subRegionsId=13429832&subRegionsId=13429912&subRegionsId=13427445&subRegionsId=13429811&subRegionsId=13428571&subRegionsId=13431008&subRegionsId=13429341&subRegionsId=13430323&subRegionsId=13429676&subRegionsId=13429571&subRegionsId=13430248&subRegionsId=13431223&subRegionsId=13427530&subRegionsId=13428341&subRegionsId=13431554&subRegionsId=13428231&subRegionsId=13429997&subRegionsId=13431323&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78"
        #"http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearch&program=browse",
        #"http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId=100345635"
    ]

    #restrict_xpath = """//table[@class='resulttableClass']//tr[@bgcolor='#FFFFFF']/td[3] |
    #                    //table[@class='resulttableClass']//tr[@bgcolor='#F7F7F7']/td[3]"""

    restrict_xpath = ["//table[@class='resulttableClass']"]  #//tr[@bgcolor='#FFFFFF']",
                      #"//table[@class='resulttableClass']//tr[@bgcolor='#F7F7F7']"]
    #Rule(SgmlLinkExtractor(allow="", process_value="getLink"))
    rules = (Rule(SgmlLinkExtractor(restrict_xpaths=restrict_xpath), follow=True, process_links="process_links"),)

    #start_urls = [
    #    "http://localhost/teste/index.html"
        #"http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearch&program=browse",
        #"http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId=100345635"
    #]

    def start_requests(self):
        return [Request(url=self.login_url, callback=self.login)]

        #return [FormRequest(url=self.start_urls[0]).from_response(response, formdata={
        #'userName': "AIESEC_EMAIL", 'password': "AIESEC_PASSWORD"}, callback=self.after_login)]

    def login(self, response):
        print("Logging in the system")
        #print "Response %s" % response
        wtf = [FormRequest(url=self.start_urls[0]).from_response(response, formdata=dict(
            userName="AIESEC_EMAIL", password="AIESEC_PASSWORD"), callback=self.generate_links)]

        return wtf

    def generate_links(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

        pass

    def parse_item(self, response):
        print "bleh"

        #filename = response.url.split("/")[-1]
        #select = HtmlXPathSelector(response).select("/html/head/title/text()").extract()


        hxs = HtmlXPathSelector(response)
        filename = hxs.select("/html/head/title/text()").extract()[0]
        #tnList = hxs.select("//table[@class='resulttableClass']//tr[2]/td[3]/a/@onclick").extract()[0].split("'")[1]
        #tableTN = hxs.select("//table[@class='resulttableClass']")
        #tnList = tableTN.select("//tr[2]/td[3]/a/@onclick").extract()
        #tnList = tableTN.select("//tr[@bgcolor='#FFFFFF']/td[3]/a/@onclick | //tr[@bgcolor='#F7F7F7']/td[3]/a/@onclick").extract()

        #tableTNs = tableTNs.select()
        #TNText =

        #for tn in tnList:
        #    print "TN: %s" % tn.split("'")[1]

        print "Response %s" % response.headers
        #print "URL : %s" % response.url
        #print "Filename: %s" % filename
        #print "TNText: %s" % tnList

        #open("table.html" % filename, "wb").write(str(tableTNs.extract()))
        #link = "http://www.myaiesec.net/exchange/viewtn.do?operation=executeAction&tnId=" + tnList[0].split("'")[1]
        #print link
        #print type(response.url)
        #print type(link)
        #return [Request(url=response.url, callback=self.test), Request(url=response.url, callback=self.test)]
        #return Request(url=link.encode('utf8'), callback=self.parse_item)

        #return Request(url=
        return None

        #open("teste.html", "wb").write(response.body)
        #return [FormRequest.from_response(response, formdata={'userName': "AIESEC_EMAIL",
        #                                                      'password': "AIESEC_PASSWORD"}, callback=self.after_login)]
        #return [FormRequest(url=self.start_urls[0]).from_response(response, formdata={


    #def after_login(self, response):
        #filename = response.url.split("/")[-1]
        #print "Response %s" % response.headers
        #print "URL : %s" % response.url

        #open("%s.html" % filename, "wb").write(response.body)
        #return Request(url=start_urls[0], callback=self.parse_test)

    #def test(self, response):
    #    print("Teste123")
    #    open("teste123.html", "wb").write(response.body)
    #    return None

    def process_links(self, links):
        for link in links:
            print "TESTE %s" % link

        return links

        # fetch the items you need and yield them like this:
        # yield item

        # fetch the next pages to scrape
        #for url in hxs.select("//div[@class='limiter']/a/@href").extract():
        #    absolute_url = "http://www.example.de" + url
        #  yield Request(absolute_url, callback=self.parse_item)
