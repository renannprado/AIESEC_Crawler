# -*- coding: utf-8 -*-
import os
from scrapy.http import FormRequest
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

__author__ = 'renann'


class AIESECCrawler_old(InitSpider):
    name = "AIESECCrawler_old"
    baseURLTNForm = "http://www.myaiesec.net/exchange/viewtn.do?operation=executeAction&tnId="
    baseFolder = "./internships/"
    fileExtension = ".html"
    allowed_domains = ["myaiesec.net"]
    #allowed_domains = ["localhost"]
    login_url = "http://myaiesec.net/login.do"
    #this array is aligned with start_urls array
    #also used as folder names
    countryList = \
        [
            "United Kingdom"
            ,"Norway"
            ,"United States"
            ,"Canada"
            ,"The Netherlands"
            ,"Estonia"
            ,"Sweden"
        ]

    start_urls = \
        [
            """http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=01.01.2010&date_to=31.12.2020&regions=13427109&subRegionsId=13429306&subRegionsId=13429832&subRegionsId=13429912&subRegionsId=13427445&subRegionsId=13429811&subRegionsId=13428571&subRegionsId=13431008&subRegionsId=13429341&subRegionsId=13430323&subRegionsId=13429676&subRegionsId=13429571&subRegionsId=13430248&subRegionsId=13431223&subRegionsId=13427530&subRegionsId=13428341&subRegionsId=13431554&subRegionsId=13428231&subRegionsId=13429997&subRegionsId=13431323&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78"""
            ,"""http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=01.01.2010&date_to=31.12.2020&regions=13427019&subRegionsId=13427510&subRegionsId=13432034&subRegionsId=13431989&subRegionsId=1000000389&subRegionsId=13432074&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78"""
            ,"""http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=01.01.2010&date_to=31.12.2020&regions=13426586&subRegionsId=1000000047&subRegionsId=13429116&subRegionsId=13429596&subRegionsId=13431649&subRegionsId=49425124&subRegionsId=13428576&subRegionsId=21076709&subRegionsId=13429336&subRegionsId=1000000206&subRegionsId=13430698&subRegionsId=13428521&subRegionsId=1000000429&subRegionsId=13429731&subRegionsId=13429436&subRegionsId=13429416&subRegionsId=13428686&subRegionsId=13428486&subRegionsId=1000000182&subRegionsId=13429646&subRegionsId=20993958&subRegionsId=13430358&subRegionsId=48880892&subRegionsId=13428291&subRegionsId=13431424&subRegionsId=13431168&subRegionsId=13428391&subRegionsId=13429196&subRegionsId=13428926&subRegionsId=13429486&subRegionsId=13431098&subRegionsId=13430022&subRegionsId=1000000430&subRegionsId=13431188&subRegionsId=13429761&subRegionsId=13430298&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78&selectedSkillsProp=90&selectedSkillsProp=105&selectedSkillsProp=29&selectedSkillsProp=120&selectedSkillsProp=161&selectedSkillsProp=181&selectedSkillsProp=179"""
            ,"""http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=01.01.2010&date_to=31.12.2020&regions=13427190&subRegionsId=13428861&subRegionsId=13430308&subRegionsId=13428656&subRegionsId=13430943&subRegionsId=13429982&subRegionsId=13428371&subRegionsId=13429301&subRegionsId=1000000376&subRegionsId=1000000065&subRegionsId=13428451&subRegionsId=13429071&subRegionsId=13430458&subRegionsId=13430408&subRegionsId=1000000425&subRegionsId=13428411&subRegionsId=13428456&subRegionsId=13430063&subRegionsId=13430823&subRegionsId=13429376&subRegionsId=13429426&subRegionsId=13430763&subRegionsId=13429681&subRegionsId=13430463&subRegionsId=13429456&subRegionsId=13429391&subRegionsId=13429181&subRegionsId=13428791&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78&selectedSkillsProp=90&selectedSkillsProp=105&selectedSkillsProp=29&selectedSkillsProp=120&selectedSkillsProp=161&selectedSkillsProp=181&selectedSkillsProp=179"""
            ,"""http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=01.01.2010&date_to=31.12.2020&regions=13426794&subRegionsId=13429852&subRegionsId=1000000443&subRegionsId=13430773&subRegionsId=1000000244&subRegionsId=13430653&subRegionsId=13429126&subRegionsId=13431273&subRegionsId=13430643&subRegionsId=13430998&subRegionsId=13428401&subRegionsId=13430973&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78&selectedSkillsProp=90&selectedSkillsProp=105&selectedSkillsProp=29&selectedSkillsProp=120&selectedSkillsProp=161&selectedSkillsProp=181&selectedSkillsProp=179"""
            ,"""http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=01.01.2010&date_to=31.12.2020&regions=13427091&subRegionsId=1000000272&subRegionsId=13431999&subRegionsId=13431959&page=1&questiontext=&browsetype=tn&xchangetype=GI&tncode=&getTN=gepTN&status=-1&duration_from=20&duration_to=78&selectedSkillsProp=63&selectedSkillsProp=118&selectedSkillsProp=64&selectedSkillsProp=117&selectedSkillsProp=67&selectedSkillsProp=116&selectedSkillsProp=164&selectedSkillsProp=69&selectedSkillsProp=73&selectedSkillsProp=72&selectedSkillsProp=90&selectedSkillsProp=155&selectedSkillsProp=105&selectedSkillsProp=23&selectedSkillsProp=156&selectedSkillsProp=167&selectedSkillsProp=28&selectedSkillsProp=169&selectedSkillsProp=29&selectedSkillsProp=91&selectedSkillsProp=109&selectedSkillsProp=30&selectedSkillsProp=120&selectedSkillsProp=161&selectedSkillsProp=94&selectedSkillsProp=108&selectedSkillsProp=92&selectedSkillsProp=181&selectedSkillsProp=175&selectedSkillsProp=179&selectedSkillsProp=178&selectedSkillsProp=184"""
            ,"""http://www.myaiesec.net/exchange/browseintern.do?operation=BrowseInternSearchResult&page=1&program=browse&statusid=9&buttontype=&countrycode=&orgsearchtext=&date_from=03.03.2000&date_to=03.03.2020&regions=13426766&subRegionsId=13429491&subRegionsId=13430688&s"""
        ]

    listOfTNToBeScraped = []

    def init_request(self):
        return Request(url=self.login_url, callback=self.doLogin)

    def doLogin(self, response):
        print("Logging in the system")
        return [FormRequest(url=self.login_url).from_response(response, formdata=dict(
            userName="AIESEC_EMAIL", password="AIESEC_PASSWORD"), callback=self.initialized)]

    def parse(self, response):
        countryIndex = self.getCountryIndex(response.url)
        folderName = AIESECCrawler_old.countryList[countryIndex]
        print "Current country: %s" % folderName
        hxs = HtmlXPathSelector(response)
        tableTN = hxs.select("//table[@class='resulttableClass']")
        tnInfoCells = tableTN.select("//tr[@bgcolor='#FFFFFF']/td[3] | //tr[@bgcolor='#F7F7F7']/td[3]")
        internshipList = []

        for cell in tnInfoCells:
            tnCode = cell.select("a[@class='linkclass']/text()").extract()[0]
            #print "TNCode: %s" % tnCode
            tnID = cell.select("a/@onclick").extract()[0].split("'")[1]
            #print "tnID: %s" % tnID
            TN = {"ID": tnID, "Code": tnCode, "FolderName": folderName}
            print TN
            internshipList.append(TN)

        requestQueue = []
        newTNCounter = 0
        for TN in internshipList:
            if self.isNewTN(TN["Code"], TN["FolderName"]):
                newTNCounter += 1
                requestQueue.append(self.handleNewTN(TN))
            else:
                print "TN %s already in database" % TN["Code"]

        for request in requestQueue:
            yield request

        print "%d new TNs available in %s" % (newTNCounter, folderName)

    def handleNewTN(self, TN):
        self.createFolder(TN["FolderName"])

        TN_URL = AIESECCrawler_old.baseURLTNForm + TN["ID"]

        callbackFunc = lambda response: self.scrapeNewTN(response, TN)

        return Request(TN_URL, callback=callbackFunc)

    def isNewTN(self, TNCode, countryName):
        folderName = AIESECCrawler_old.baseFolder + countryName
        filePath = folderName + "/" + TNCode + AIESECCrawler_old.fileExtension
        print "FolderName: %s" % folderName
        print "FilePath: %s" % filePath
        if not os.path.exists(filePath):
            return True
        else:
            return False

    def createFolder(self, folderName):
        finalPath = AIESECCrawler_old.baseFolder + folderName

        if not os.path.exists(AIESECCrawler_old.baseFolder):
            os.mkdir(AIESECCrawler_old.baseFolder)

        if not os.path.exists(finalPath):
            os.mkdir(finalPath)

    def scrapeNewTN(self, response, TN):
        print "Scraping TDID: %s" % TN["ID"]
        hxs = HtmlXPathSelector(response)
        TNCode = hxs.select("//table/tr[2]/td[@class='linkclass']/text()").extract()[0]
        pathToWrite = AIESECCrawler_old.baseFolder + TN["FolderName"] + "/" + TNCode + AIESECCrawler_old.fileExtension
        print "PathToWrite: %s" % pathToWrite
        print TN
        open(pathToWrite, "wb").write(response.body)

    def getCountryIndex(self, urlCountry):
        count = -1
        for url in AIESECCrawler_old.start_urls:
            count += 1
            if url == urlCountry:
                return count