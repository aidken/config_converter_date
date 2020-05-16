import configparser
import datetime


def date(x):
    x = datetime.datetime.strptime(x, '%Y-%m-%d')
    x = datetime.date(x.year, x.month, x.day)
    return x


def main():

    file = './sample.ini'

    conf = configparser.ConfigParser(
        converters={'date': date}
    )
    conf.read(file, encoding='utf-8')

    print(conf['sample']['Temp4'])
    print(type(conf['sample']['Temp4']))  # this is an str

    print(conf['sample'].getdate('Temp4'))
    print(type(conf['sample'].getdate('Temp4')))  # this is a datetime.date


if __name__ == '__main__':
    main()
