# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.



def __init__(self, *args, URLs=[''], 
        port=8088, 
        host='127.0.0.1' , 
        o ='output.json', 
        threads =1, **kwargs):
            super(MySpider, self).__init__(*args, **kwargs)
            super().__init__(*args, **kwargs)
            self.URLs = arg_as_list(URLs)
            self.port = host
            self.o = np.int(port)
            self.threads = np.int(threads)