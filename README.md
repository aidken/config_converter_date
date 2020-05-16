# config_converter_date
A date converter for Python [configparser](https://docs.python.org/3/library/configparser.html).

config_converter_date.py has a callable <code>date</code>. Pass this to argument <code>converters</code>.

    import configparser

    conf = configparser.ConfigParser(
        converters={'date': date}
    )

Then you can parse [ISO date format](https://www.iso.org/iso-8601-date-and-time-format.html) in your conf file as [datetime](https://docs.python.org/3/library/datetime.html).date value.

    import configparser

    conf = configparser.ConfigParser(
        converters={'date': date}
    )

    # assume this file has [sample] Temp4: 2020-05-15
    conf.read(file)

    print(conf['sample']['Temp4'])
    print(type(conf['sample']['Temp4']))  # this is an str

    print(conf['sample'].getdate('Temp4'))
    print(type(conf['sample'].getdate('Temp4')))  # this is a datetime.date
