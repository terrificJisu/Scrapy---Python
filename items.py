# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HanbitMediaItem(scrapy.Item):
    # define the fields for your item here like:
    # Book title
    book_title = scrapy.Field()

    # Book Author
    book_author = scrapy.Fiedl()

    # Book Translator
    book_translator = scrapy.Field()

    # Book Publichment Date
    book_pub_date = Field()

    # ISBN
    book_isbn = Field()
    
    pass
