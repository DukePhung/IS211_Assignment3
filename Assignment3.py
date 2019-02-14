from urllib import request
import csv
import re

urlsite = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
imageCount = {'images': 0, 'non-images': 0}
myfile = 'Weblog_Data.csv'
searchEngine = {}


def downloadData(csv_url):
    """Access csv file from URL and write to local csv file.

    Args:
        csv_url (link): link where the csv file is located

    Returns:
        file: csv file that contains all information on URL.
    """

    response = request.urlopen(csv_url)
    csvfile = response.read()
    csv_str = str(csvfile)
    lines = csv_str.split("\\n")
    dest_url = 'Weblog_Data.csv'
    fx = open(dest_url, 'w')

    for line in lines:
        fx.write(line + '\n')

    fx.close()

    return dest_url


def imageCounter(filename):
    """Access csv file and use re to search data.

    Args:
        filename (file): file used to search for re expressions

    Returns:
        Str: string with image count and percent of count.
    """

    with open(filename, 'rt') as csvFile:

        reader = csv.reader(csvFile)

        for row in reader:
            for element in row:
                if re.search('(jpg|png|gif)$', element, re.IGNORECASE):
                    imageCount['images'] += 1
                else:
                    imageCount['non-images'] += 1

    return ('Image has a total of {} searches and accounts for {:.2f} percent of all searches'.
            format(imageCount['images'], imageCount['images'] / sum(imageCount.values()) * 100))


def popularEngine(filename):
    """Access csv file and use re to search for most popular search engine.

    Args:
        filename (file): file used to search for re expressions

    Returns:
        Str: string with most popular search engine.
    """

    with open(filename, 'rt') as csvFile:

        reader = csv.reader(csvFile)

        for row in reader:
            for element in row:
                if re.search('(safari)\w*', element, re.IGNORECASE):
                    try:
                        searchEngine['Safari'] += 1
                    except KeyError:
                        searchEngine['Safari'] = 1
                elif re.search('(firefox)\w*', element, re.IGNORECASE):
                    try:
                        searchEngine['firefox'] += 1
                    except KeyError:
                        searchEngine['firefox'] = 1
                elif re.search('(chrome)\w*', element, re.IGNORECASE):
                    try:
                        searchEngine['chrome'] += 1
                    except KeyError:
                        searchEngine['chrome'] = 1

        v = list(searchEngine.values())
        k = list(searchEngine.keys())

        return 'The most popular search engine used for searching is {}'.format(k[v.index(max(v))])


if __name__ == '__main__':
    downloadData(urlsite)
    print(imageCounter(myfile))
    print(popularEngine(myfile))
