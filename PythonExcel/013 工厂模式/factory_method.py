import json  #解析JSON
import xml.etree.ElementTree as etree  #解析XML
import pandas as pd #解析xlsx csv

#解析JSON文件
class JSONDataExtractor:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

#解析XML文件
class XMLDataExtractor:
    class XMLDataExtractor:

        def __init__(self, filepath):
            self.tree = etree.parse(filepath)

        @property
        def parsed_data(self):
            return self.tree

#解析xlsx文件
class XLSXDataExtractor:
    print()

#解析csv文件
class CSVDataExtractor:
    print()

#判断扩展名
def dataextraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    elif filepath.endswith('xlsx'):
        extractor = XLSXDataExtractor
    elif filepath.endswith('csv'):
        extractor = CSVDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)

#extract_data_from()是dataextraction_factory()的一个装饰器。它增加了异常处理机制。
def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj

#函数main()展示了如何使用工厂方法。
#第一部分
#确保异常处理机制的有效性。
def main():
    #sqlite_factory = extract_data_from('data/person.sq3')
    sqlite_factory = extract_data_from('data/test.json')
    print(sqlite_factory)

    # 第二部分
    # 使用工厂方法处理JSON文件。（在数据非空的情况下）该解析方法能够展示电影的标题、年份、导演姓名以及体裁。
    json_factory = extract_data_from('data/test.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} node')
    '''
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()
    '''
    #判断是否为字典
    print(type(json_data) == dict)

if __name__ == '__main__':
    main()