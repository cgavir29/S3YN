import re

PAT_ANT = '[0-9]{6}'
# PAT_ANT = '[0-9]{6}\s[0-9]{6}\s[0-9]{1,3}' # Fecha Hora ?
PAT_POS = '([a-zA-Z]+)\s?'


def parse1(line):
    result = line.split(':', 1)
    ant = ' '.join(re.findall(PAT_ANT, result[0]))
    pos = ' '.join(re.findall(PAT_POS, result[1]))

    return ant + ': ' + pos


def parse2(line):
    ant1 = line[:13] + line[line.find(':'):]

    return ant1


with open('HDFS.log', 'r') as hdfs:
    for i in range(1000):
        print(parse1(hdfs.readline().strip()))
