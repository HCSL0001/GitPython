import json  #解析JSON
import xml.etree.ElementTree as etree  #解析XML

#用于解析JSON文件
#parsed_data()方法，返回包含所有数据的字典，装饰器property用于使parsed_data()变得更像一个普通的属性而非方法。
class JSONDataExtractor:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

#用于解析XML文件
#parsed_data()方法，返回由xml.etree.Element组成的、包含所有数据的列表。
class XMLDataExtractor:

    def __init__(self, filepath):
        self.tree =  etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

#dataextraction_factory()是一个工厂方法。它根据输入文件的扩展名，返回一个JSONDataExtractor或一个XMLDataExtractor的实力。
def dataextraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
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
    sqlite_factory = extract_data_from('data/person.sq3')
    print(sqlite_factory)

    #第二部分
    #使用工厂方法处理JSON文件。（在数据非空的情况下）该解析方法能够展示电影的标题、年份、导演姓名以及体裁。
    json_factory = extract_data_from('data/movies.json')
    json_data = json_factory.parsed_data
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

    #最后一部分
    #使用工厂方法处理XML文件。Xpath用于寻找所有姓为Liar的person元素。对于每一个匹配的人，将展示其基本姓名与电话号码信息。
    xml_factory = extract_data_from('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text) 
              for p in liar.find('phoneNumbers')]
        print()
    print()


if __name__ == '__main__':
    main()
