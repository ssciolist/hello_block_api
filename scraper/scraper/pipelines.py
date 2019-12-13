# -*- coding: utf-8 -*-
from scrapy.pipelines.files import FilesPipeline


class ExcelPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        import re
        url = request.url
        # use regex to capture everything from the last '/'

        match = re.search('.{4}\/([a-zA-Z0-9_ .%-]*)$', url)
        name = match.group()
        return name
