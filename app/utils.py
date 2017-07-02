# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import datetime

from dateutil.parser import parse


def parse_date(string):
    string = string.replace('年', '-')
    string = string.replace('月', '-')
    string = string.replace('日', '-')
    try:
        result = parse(string)
        return datetime.date(result.year, result.month, result.day)
    except ValueError:
        return None


def is_wiki_about_person(text):
    """
    https://en.wikipedia.org/wiki/Wikipedia:List_of_infoboxes
    """
    def make_pattern(word):
        pattern = '{{'
        words = word.split(' ')
        words_len = len(words)
        for k, v in enumerate(words):
            if k + 1 < words_len:
                pattern += '{}[_\s]*'.format(v)
            else:
                pattern += v
        pattern = pattern + '.*?}}'
        return re.compile(r'{}'.format(pattern), re.I|re.DOTALL)

    patterns = [
        make_pattern('Infobox Person'),
        make_pattern('Infobox Scientist'),

        # Religious person
        # make_pattern('Infobox Buddha'),
        make_pattern('Infobox Dalai lama'),
        make_pattern('Infobox Christian leader'),
        make_pattern('Infobox Hindu leader'),
        make_pattern('Infobox Jewish leader'),
        make_pattern('Infobox Muslim leader'),
        make_pattern('Infobox Latter Day Saint biography'),
        make_pattern('Infobox rebbe'),
        make_pattern('Infobox religious biography'),
        make_pattern('Infobox saint'),

        # American football person
        make_pattern('Infobox college football player'),
        make_pattern('Infobox CFL biography'),
        make_pattern('Infobox NFL biography'),

        # Baseball person
        make_pattern('Infobox baseball biography'),
        make_pattern('Infobox MLB umpire'),

        # Basketball person
        make_pattern('Infobox basketball biography'),
        make_pattern('Infobox basketball official'),

        # Motorsports person
        make_pattern('Infobox Champ Car driver'),
        make_pattern('Infobox F1 driver'),
        make_pattern('Infobox Le Mans driver'),
        make_pattern('Infobox Motocross rider'),
        make_pattern('Infobox motorcycle rider'),
        make_pattern('Infobox NASCAR driver'),
        make_pattern('Infobox racing driver'),
        make_pattern('Infobox racing driver series section'),
        make_pattern('Infobox speedway rider'),
        make_pattern('Infobox WRC driver'),

        # Other sportsperson
        make_pattern('Infobox sportsperson'),
        make_pattern('Infobox biathlete'),
        make_pattern('Infobox boxer (amateur)'),
        make_pattern('Infobox speed skater'),
        make_pattern('Infobox sailor'),
        make_pattern('Infobox sport wrestler'),
        make_pattern('Infobox swimmer'),
        make_pattern('Infobox AFL biography'),
        make_pattern('Infobox alpine ski racer'),
        make_pattern('Infobox amateur wrestler'),
        make_pattern('Infobox badminton player'),
        make_pattern('Infobox bandy biography'),
        make_pattern('Infobox bodybuilder'),
        make_pattern('Infobox boxer'),
        make_pattern('Infobox climber'),
        make_pattern('Infobox cricketer'),
        make_pattern('Infobox curler'),
        make_pattern('Infobox cyclist'),
        make_pattern('Infobox equestrian'),
        make_pattern('Infobox fencer'),
        make_pattern('Infobox field hockey player'),
        make_pattern('Infobox figure skater'),
        make_pattern('Infobox football biography'),
        make_pattern('Infobox football official'),
        make_pattern('Infobox GAA player'),
        make_pattern('Infobox golfer'),
        make_pattern('Infobox gymnast'),
        make_pattern('Infobox handball biography'),
        make_pattern('Infobox horseracing personality'),
        make_pattern('Infobox ice hockey player'),
        make_pattern('Infobox lacrosse player'),
        make_pattern('Infobox martial artist'),
        make_pattern('Infobox mountaineer'),
        make_pattern('Infobox NCAA athlete'),
        make_pattern('Infobox netball biography'),
        make_pattern('Infobox NHL coach'),
        make_pattern('Infobox pelotari'),
        make_pattern('Infobox professional bowler'),
        make_pattern('Infobox professional wrestler'),
        make_pattern('Infobox rugby biography'),
        make_pattern('Infobox rugby league biography'),
        make_pattern('Infobox skier'),
        # make_pattern('Infobox sports announcer details'),
        make_pattern('Infobox squash player'),
        make_pattern('Infobox sumo wrestler'),
        make_pattern('Infobox surfer'),
        make_pattern('Infobox table tennis player'),
        make_pattern('Infobox tennis biography'),
        make_pattern('Infobox volleyball biography'),

        # Other person
        make_pattern('Infobox academic'),
        make_pattern('Infobox adult biography'),
        make_pattern('Infobox architect'),
        make_pattern('Infobox clergy'),
        make_pattern('Infobox dancer'),
        make_pattern('Infobox fashion designer'),
        # make_pattern('Infobox medical details'),
        make_pattern('Infobox medical person'),
        make_pattern('Infobox Native American leader'),
        make_pattern('Infobox sports announcer'),
        make_pattern('Infobox theologian'),
        # make_pattern('Infobox theological work'),
        make_pattern('Infobox artist'),
        make_pattern('Infobox astronaut'),
        make_pattern('Infobox aviator'),
        make_pattern('Infobox chef'),
        make_pattern('Infobox chess biography'),
        make_pattern('Infobox Chinese historical biography'),
        make_pattern('Infobox Chinese-language singer and actor'),
        make_pattern('Infobox classical composer'),
        make_pattern('Infobox college coach'),
        make_pattern('Infobox comedian'),
        make_pattern('Infobox comics creator'),
        make_pattern('Infobox criminal'),
        make_pattern('Infobox darts player'),
        make_pattern('Infobox economist'),
        make_pattern('Infobox engineer'),
        make_pattern('Infobox FBI Ten Most Wanted'),
        make_pattern('Infobox go player'),
        make_pattern('Infobox gunpowder plotter'),
        make_pattern('Infobox Magic: The Gathering player'),
        make_pattern('Infobox member of the Knesset'),
        make_pattern('Infobox military person'),
        make_pattern('Infobox model'),
        make_pattern('Infobox musical artist'),
        make_pattern('Infobox Nahua officeholder'),
        make_pattern('Infobox officeholder'),
        make_pattern('Infobox pageant titleholder'),
        make_pattern('Infobox philosopher'),
        make_pattern('Infobox pirate'),
        make_pattern('Infobox Playboy Playmate'),
        make_pattern('Infobox playwright'),
        make_pattern('Infobox poker player'),
        make_pattern('Infobox police officer'),
        make_pattern('Infobox presenter'),
        make_pattern('Infobox eSports player'),
        make_pattern('Infobox Pro Gaming player'),
        make_pattern('Infobox snooker player'),
        make_pattern('Infobox spy'),
        make_pattern('Infobox War on Terror detainee'),
        make_pattern('Infobox writer'),
        make_pattern('Infobox YouTube personality'),
    ]
    for p in patterns:
        if p.search(text):
            return True
    return False


def get_birth_death_date(text):
    def filter_date(string):
        """
        # {{birth based on age as of date|mos=1|25|2009|02|03}}
        # from: https://zh.wikipedia.org/wiki/%E5%86%B0%E8%9B%99
        >>> filter_date("|mos=1|25|2009|02|03")
        ['25', '2009', '02', '03']
        """
        result = []
        for i in string.strip('|').split('|'):
            i = i.strip()
            if not i:
                continue
            if '=' in i:
                continue
            result.append(i)
        return result
    # def get_date_from_text(pattern, text, callback):
    #     match = re.search(pattern, text, flags=re.I)
    #     if not match:
    #         return None
        # return callback()

    birth_date, death_date = None, None

    # birth date and age
    match = re.search(r'{{\s*birth\s*date and age\s*\|[^\d]*(\d+\|\d+\|\d+)', text, flags=re.I)
    if match:
        # living
        return parse_date(match.group(1).replace('|', '-')), None

    # birth date
    match = re.search(r'{{\s*birth\s*date\s*\|[^\d]*(\d+\|\d+\|\d+)', text, flags=re.I)
    if match:
        birth_date = parse_date(match.group(1).replace('|', '-'))

    # birth year and age
    # see: https://zh.wikipedia.org/wiki/Template:Birth_year_and_age
    if not birth_date:
        match = re.search(r'{{\s*birth\s*year and age\s*\|[^\d]*(\d+)', text, flags=re.I)
        if match:
            birth_date = datetime.date(int(match.group(1)), 1, 1)

    # birth based on age as of date
    # see: https://zh.wikipedia.org/wiki/Template:Birth_based_on_age_as_of_date
    if not birth_date:
        match = re.search(r'{{\s*birth based on age as of date\s*\|(.*?)}}', text, flags=re.I)
        if match:
            splitted = filter_date(match.group(1))
            if splitted:
                birth_date = datetime.date(int(splitted[1]) - int(splitted[0]), 1, 1)

    # birth_date  = 1957年6月27日
    # example: https://zh.wikipedia.org/wiki/%E7%9B%96%E5%B0%94%C2%B7%E4%BC%8A%E7%93%A6%E5%B0%94%E7%BB%A5
    if not birth_date:
        match = re.search(r'birth_date\s*=\s*(\d+)年(\d+)月(\d+)日', text, flags=re.I)
        if match:
            birth_date = datetime.date(int(match.group(1)), int(match.group(2)), int(match.group(3)))

    # death date and age
    match = re.search(r'{{\s*death\s*date and age\s*\|[^\d]*(\d+\|\d+\|\d+).*?}}', text, flags=re.I)
    if match:
        death_date = parse_date(match.group(1).replace('|', '-'))

    # death date
    # see: https://en.wikipedia.org/wiki/Template:Death_date
    if not death_date:
        match = re.search(r'{{\s*death date\s*\|[^\d]*(\d+)\|(\d+)\|(\d+)', text, flags=re.I)
        if match:
            death_date = datetime.date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    if not death_date:
        match = re.search(r'{{\s*death date\s*\|[^\d]*(\d+)\|(\d+)', text, flags=re.I)
        if match:
            death_date = datetime.date(int(match.group(1)), int(match.group(2)), 1)
    if not death_date:
        match = re.search(r'{{\s*death date\s*\|[^\d]*(\d+)', text, flags=re.I)
        if match:
            death_date = datetime.date(int(match.group(1)), 1, 1)

    # death year and age
    # see: https://zh.wikipedia.org/wiki/Template:Death_year_and_age
    if not death_date:
        match = re.search(r'{{\s*death\s*year and age\s*\|[^\d]*(\d+)\|\d+\|(\d+)', text, flags=re.I)
        if match:
            death_date = datetime.date(int(match.group(1)), int(match.group(2)), 1)
        else:
            match = re.search(r'{{\s*death\s*year and age\s*\|[^\d]*(\d+)', text, flags=re.I)
            if match:
                death_date = datetime.date(int(match.group(1)), 1, 1)

    if not death_date:
        match = re.search(r'death_date\s*=\s*(\d+)年(\d+)月(\d+)日', text, flags=re.I)
        if match:
            death_date = datetime.date(int(match.group(1)), int(match.group(2)), int(match.group(3)))

    return birth_date, death_date


def get_wiki_abstract(text):
    pass
