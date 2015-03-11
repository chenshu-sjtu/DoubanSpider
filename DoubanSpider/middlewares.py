# -*- coding: utf-8 -*-

from DoubanSpider.agents import AGENTS
import random

class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        ua = random.choice(AGENTS)
        if ua:
            request.headers.setdefault('User-Agent', ua)
