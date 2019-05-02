#coding:utf-8
class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = path + "?ver=" + "201812182100"
        return UrlManager.buildUrl(path)
