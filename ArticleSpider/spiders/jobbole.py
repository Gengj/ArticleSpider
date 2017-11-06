# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112793/']

    def parse(self, response):


        #=========通过XPATH提取数据===============#

        # 文章标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]

        # 文章创建日期
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace("·"," ").strip()

        # 点赞数量
        praise_nums = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])

        # 收藏数量
        bookmark_nums = str(response.xpath("//span[contains(@class,'bookmark-btn')]/text()"))
        re_match = re.match('.*(\d+).*',bookmark_nums)
        if re_match:
            bookmark_nums = int(re_match.group(1))
        else:
            bookmark_nums = 0

        # 评论数量
        conment_nums = str(response.xpath("//a[@href='#article-comment']/span/text()"))
        re_match = re.match('.*(\d+).*', conment_nums)
        if re_match:
            conment_nums = int(re_match.group(1))
        else:
            conment_nums = 0

        # 正文内容
        content = response.xpath("//div[@class='entry']").extract()

        # 标签内容列表
        category_tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        category_tag_list = [element for element in category_tag_list if not element.strip().endswith("评论")]
        tags = ','.join(category_tag_list)

        #=========通过CSS选择器提取数据===============#



        pass
