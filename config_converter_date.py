import configparser
import datetime


file = './sample.ini'

def date(x):
    x = datetime.datetime.strptime(x, '%Y-%m-%d')
    x = datetime.date(x.year, x.month, x.day)
    return x

conf = configparser.ConfigParser(
    converters={'date': date}
)

conf.read(file)

print(conf['sample']['Temp4'])
print(type(conf['sample']['Temp4']))  # this is an str

print(conf['sample'].getdate('Temp4'))
print(type(conf['sample'].getdate('Temp4')))  # this is a datetime.date
