'''
@Author: your name
@Date: 2020-07-04 15:04:51
@LastEditTime: 2020-07-04 18:38:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python_learning\spider\grab\grab_test.py
'''
import logging

from grab.spider import Spider, Task

logging.basicConfig(level=logging.DEBUG)


class ExampleSpider(Spider):
    def task_generator(self):
        for lang in '312407', '312407', '228989':
            url = 'https://www.douyu.com/%s' % lang
            yield Task('search', url=url, lang=lang)

    def task_search(self, grab, task):
        print('%s: %s' % (task.lang,
                          grab.doc('//*[@id="js-player-title"]/div/div[2]/div[1]/div[1]/div[2]/div[2]/span').text()))


bot = ExampleSpider(thread_number=2)
bot.run()