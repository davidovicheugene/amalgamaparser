import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup as bs

def lxml_title(htmlText):
    tree = lxml.html.document_fromstring(htmlText)
    text_original = tree.xpath("/html/head/title/text()")
    print(text_original)

def lxml_get_class_eng(htmlText):
    tree = lxml.html.document_fromstring(htmlText)
    text_original = tree.xpath('//*[@class="original"]/text()')
    for i in text_original:
        print(i)

def lxml_get_class_rus(htmlText):
    tree = lxml.html.document_fromstring(htmlText)
    text_original = tree.xpath('//*[@class="translate"]/text()')
    for i in text_original:
        print(i)


def main():
    url = 'https://www.amalgama-lab.com/songs/e/eminem/my_darling.html'
    htmlText = requests.get(url).text
    lxml_title(htmlText)
    lxml_get_class_eng(htmlText)
    lxml_get_class_rus(htmlText)

if __name__ == "__main__":
    main()
