from htmlentitydefs import codepoint2name, name2codepoint

import re


__version__ = '1.0.2'


def encode(source):
    new_source = ''
  
    for char in source:
        if ord(char) in codepoint2name:
            char = '&%s;' % codepoint2name[ord(char)]
        else:
            char = '&#%s;' % ord(char)
        new_source += char

    return new_source


def decode(source):
    for entitie in re.findall('&(?:[a-z][a-z0-9]+);', source):
        entitie = entitie.replace('&', '')
        entitie = entitie.replace(';', '')
        source = source.replace('&%s;' % entitie, unichr(name2codepoint[entitie]))
    for entitie in re.findall('&#x(?:[A-Fa-f0-9]+);', source):
        entitie = entitie.replace('&#x', '')
        entitie = entitie.replace(';', '')
        iEntitie = int(entitie,16)
        source = source.replace('&#x%s;' % entitie, unichr(iEntitie))
    for entitie in re.findall('&#(?:[0-9]+);', source):
        entitie = entitie.replace('&#', '')
        entitie = entitie.replace(';', '')
        source = source.replace('&#%s;' % entitie, unichr(int(entitie)))
    return source
