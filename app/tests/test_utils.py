# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.test import TestCase

from .. import utils


class UtilsTest(TestCase):
    def test_parse_date(self):
        func = utils.parse_date
        self.assertEqual(date(2017, 6, 27), func('2017-6-27'))
        self.assertEqual(date(1956, 1, 31), func('1956年1月31日'))
        self.assertEqual(date(2017, 6, 27), func('2017年06月27日'))

    def test_is_wiki_about_person(self):
        cases = [
            ("test", False),
            ("""{{Infobox Person
                name = test
                }}""", True),
            ("""{{Infobox_Person
                name = test
                }}""", True),
            ("""{{Infobox Scientist
                }}""", True),
            ("""{{Infobox_Scientist
                name = test
                }}""", True),
            ("""{{Infobox Dalai Lama
                name = test
                }}""", True),
            ("""{{InfoboxDalaiLama
                name = test
                }}""", True),
            ("""{{Infobox Christian leader
                }}""", True),
            ("""{{Infobox_Christianleader
                }}""", True),
            ("""{{Infobox Hindu leader
                }}""", True),
            ("""{{Infobox_Hindu_leader
                }}""", True),
            ("""{{Infobox Jewish leader
                }}""", True),
            ("""{{Infobox_Jewish_leader
                }}""", True),
            ("""{{Infobox Muslim leader
                }}""", True),
            ("""{{Infobox_Muslim_leader
                }}""", True),
            ("""{{Infobox Latter Day Saint biography
                }}""", True),
            ("""{{Infobox_Latter_DaySaint  biography
                }}""", True),
            ("""{{Infobox rebbe
                }}""", True),
            ("""{{Infobox_rebbe
                }}""", True),
            ("""{{Infobox religious biography
                }}""", True),
            ("""{{Infobox_religious_biography
                }}""", True),
            ("""{{Infobox saint
                }}""", True),
            ("""{{Infobox_saint
                }}""", True),
            ("""{{Infobox college football player
                }}""", True),            
            ("""{{Infobox CFL biography
                }}""", True),
            ("""{{Infobox NFL biography
                }}""", True),
            ("""{{Infobox baseball biography
                }}""", True),
            ("""{{Infobox MLB umpire
                }}""", True),
            ("""{{Infobox basketball biography
                }}""", True),
            ("""{{Infobox basketball official
                }}""", True),
            ("""{{Infobox Champ Car driver
                }}""", True),
            ("""{{Infobox F1 driver
                }}""", True),
            ("""{{Infobox Le Mans driver
                }}""", True),
            ("""{{Infobox Motocross rider
                }}""", True),
            ("""{{Infobox motorcycle rider
                }}""", True),
            ("""{{Infobox NASCAR driver
                }}""", True),
            ("""{{Infobox racing driver
                }}""", True),
            ("""{{Infobox racing driver series section
                }}""", True),
            ("""{{Infobox speedway rider
                }}""", True),
            ("""{{Infobox WRC driver
                }}""", True),
            ("{{Infobox sportsperson}}", True),
            ("{{Infobox biathlete}}", True),
            ("{{Infobox boxer (amateur)}}", True),
            ("{{Infobox speed skater}}", True),
            ("{{Infobox sailor}}", True),
            ("{{Infobox sport wrestler}}", True),
            ("{{Infobox swimmer}}", True),
            ("{{Infobox AFL biography}}", True),
            ("{{Infobox alpine ski racer}}", True),
            ("{{Infobox amateur wrestler}}", True),
            ("{{Infobox badminton player}}", True),
            ("{{Infobox bandy biography}}", True),
            ("{{Infobox bodybuilder}}", True),
            ("{{Infobox boxer}}", True),
            ("{{Infobox climber}}", True),
            ("{{Infobox cricketer}}", True),
            ("{{Infobox curler}}", True),
            ("{{Infobox cyclist}}", True),
            ("{{Infobox equestrian}}", True),
            ("{{Infobox fencer}}", True),
            ("{{Infobox field hockey player}}", True),
            ("{{Infobox figure skater}}", True),
            ("{{Infobox football biography}}", True),
            ("{{Infobox football official}}", True),
            ("{{Infobox GAA player}}", True),
            ("{{Infobox golfer}}", True),
            ("{{Infobox gymnast}}", True),
            ("{{Infobox handball biography}}", True),
            ("{{Infobox horseracing personality}}", True),
            ("{{Infobox ice hockey player}}", True),
            ("{{Infobox lacrosse player}}", True),
            ("{{Infobox martial artist}}", True),
            ("{{Infobox mountaineer}}", True),
            ("{{Infobox NCAA athlete}}", True),
            ("{{Infobox netball biography}}", True),
            ("{{Infobox NHL coach}}", True),
            ("{{Infobox pelotari}}", True),
            ("{{Infobox professional bowler}}", True),
            ("{{Infobox professional wrestler}}", True),
            ("{{Infobox rugby biography}}", True),
            ("{{Infobox rugby league biography}}", True),
            ("{{Infobox skier}}", True),
            # ("{{Infobox sports announcer details}}", True),
            ("{{Infobox squash player}}", True),
            ("{{Infobox sumo wrestler}}", True),
            ("{{Infobox surfer}}", True),
            ("{{Infobox table tennis player}}", True),
            ("{{Infobox tennis biography}}", True),
            ("{{Infobox volleyball biography}}", True),
            ("{{Infobox academic}}", True),
            ("{{Infobox adult biography}}", True),
            ("{{Infobox architect}}", True),
            ("{{Infobox clergy}}", True),
            ("{{Infobox dancer}}", True),
            ("{{Infobox fashion designer}}", True),
            ("{{Infobox medical person}}", True),
            ("{{Infobox Native American leader}}", True),
            ("{{Infobox sports announcer}}", True),
            ("{{Infobox theologian}}", True),
            ("{{Infobox artist}}", True),
            ("{{Infobox astronaut}}", True),
            ("{{Infobox aviator}}", True),
            ("{{Infobox chef}}", True),
            ("{{Infobox chess biography}}", True),
            ("{{Infobox Chinese historical biography}}", True),
            ("{{Infobox Chinese-language singer and actor}}", True),
            ("{{Infobox classical composer}}", True),
            ("{{Infobox college coach}}", True),
            ("{{Infobox comedian}}", True),
            ("{{Infobox comics creator}}", True),
            ("{{Infobox criminal}}", True),
            ("{{Infobox darts player}}", True),
            ("{{Infobox economist}}", True),
            ("{{Infobox engineer}}", True),
            ("{{Infobox FBI Ten Most Wanted}}", True),
            ("{{Infobox go player}}", True),
            ("{{Infobox gunpowder plotter}}", True),
            ("{{Infobox Magic: The Gathering player}}", True),
            ("{{Infobox member of the Knesset}}", True),
            ("{{Infobox military person}}", True),
            ("{{Infobox model}}", True),
            ("{{Infobox musical artist}}", True),
            ("{{Infobox Nahua officeholder}}", True),
            ("{{Infobox officeholder}}", True),
            ("{{Infobox pageant titleholder}}", True),
            ("{{Infobox philosopher}}", True),
            ("{{Infobox pirate}}", True),
            ("{{Infobox Playboy Playmate}}", True),
            ("{{Infobox playwright}}", True),
            ("{{Infobox poker player}}", True),
            ("{{Infobox police officer}}", True),
            ("{{Infobox presenter}}", True),
            ("{{Infobox eSports player}}", True),
            ("{{Infobox Pro Gaming player}}", True),
            ("{{Infobox snooker player}}", True),
            ("{{Infobox spy}}", True),
            ("{{Infobox War on Terror detainee}}", True),
            ("{{Infobox writer}}", True),
            ("{{Infobox YouTube personality}}", True),
        ]
        for input, expected in cases:
            self.assertEqual(expected, utils.is_wiki_about_person(input))

    def test_get_birth_death_date(self):
        cases = [
            ("test", (None, None)),

            # birth date and age
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date and age|}}
                test = 2017|7|3
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date and age|2017|6|27}}
                }}""", (date(2017, 6, 27), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth_date and age|2017|6|27}}
                }}""", (date(2017, 6, 27), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{ birth date and age |2017|6|27}}
                }}""", (date(2017, 6, 27), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birthdate and age|2017|6|27}}
                }}""", (date(2017, 6, 27), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date and age|2017|6|27|mf=y}}
                }}""", (date(2017, 6, 27), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date and age|mf=yes|2017|6|27}}
                }}""", (date(2017, 6, 27), None)),

            # birth date
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date|}}
                test = 2017|7|3
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date|1500|2|3}}
                }}""", (date(1500, 2, 3), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth_date|1500|2|3}}
                }}""", (date(1500, 2, 3), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{ birth date |1500|2|3}}
                }}""", (date(1500, 2, 3), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date|mf=yes|1500|2|3}}
                }}""", (date(1500, 2, 3), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date|1500|2|3|mf=y}}
                }}""", (date(1500, 2, 3), None)),

            # birth year and age
            ("""{{Infobox Person
                name = test
                birth_date = {{birth year and age|}}
                test = 2017|7|3
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth year and age|2017}}
                }}""", (date(2017, 1, 1), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth_year and age|2017}}
                }}""", (date(2017, 1, 1), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{ birth year and age |2017}}
                }}""", (date(2017, 1, 1), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth year and age|mf=yes|2017}}
                }}""", (date(2017, 1, 1), None)),
            ("""{{Infobox Person
                name = test
                birth_date = {{birth year and age|2017|ms=y}}
                }}""", (date(2017, 1, 1), None)),

            # birth based on age as of date
            ("""{{Infobox Person
                birth_date = {{Birth based on age as of date|50|2000|3|3}}
                }}""", (date(1950, 1, 1), None)),
            ("""{{Infobox Person
                birth_date = {{ Birth based on age as of date |50|2000|3|3}}
                }}""", (date(1950, 1, 1), None)),
            ("""{{Infobox Person
                birth_date = {{birth based on age as of date|mos=1|25|2009|02|03}}
                }}""", (date(1984, 1, 1), None)),

            ("""{{Infobox Person
                birth_date = 1957年6月27日
                }}""", (date(1957, 6, 27), None)),
            ("""{{Infobox Person
                birth_date = 1957年6月
                }}""", (date(1957, 6, 1), None)),
            ("""{{Infobox Person
                birth_date = 1957年
                }}""", (date(1957, 1, 1), None)),

            ("""{{Infobox Person
                born = 1957年6月27日
                }}""", (date(1957, 6, 27), None)),
            ("""{{Infobox Person
                born = 1957年6月
                }}""", (date(1957, 6, 1), None)),
            ("""{{Infobox Person
                born = 1957年
                }}""", (date(1957, 1, 1), None)),

            ("""{{Infobox Person
                birth_date = 3 Jul, 2017
                }}""", (date(2017, 7, 3), None)),
            ("""{{Infobox Person
                birth_date = 28 August 1919
                }}""", (date(1919, 8, 28), None)),

            # death date and age
            ("""{{Infobox Person
                name = test
                death_date = {{Death date and age|}}\ntest = 1000|2|3}}
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date and age|1600|1|2|1500|2|3}}
                }}""", (None, date(1600, 1, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date and age |1600|1|2|1500|2|3}}
                }}""", (None, date(1600, 1, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date and age|mf=yes|1600|1|2|1500|2|3}}
                }}""", (None, date(1600, 1, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date and age|1600|1|2|1500|2|3|mf=y}}
                }}""", (None, date(1600, 1, 2))),

            # death date
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|}}
                test = 1600|2|2
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|1600|2|2}}
                }}""", (None, date(1600, 2, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death_date|1600|2|2}}
                }}""", (None, date(1600, 2, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date |1600|2|2}}
                }}""", (None, date(1600, 2, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|}}
                test = 1600|2
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|1600|2}}
                }}""", (None, date(1600, 2, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death_date|1600|2}}
                }}""", (None, date(1600, 2, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date |1600|2}}
                }}""", (None, date(1600, 2, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|}}
                test = 1600
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|1600}}
                }}""", (None, date(1600, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death_date|1600}}
                }}""", (None, date(1600, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date |1600}}
                }}""", (None, date(1600, 1, 1))),

            # death year and age
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|}}
                test = 1900|1800|12
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|1900|1800|12}}
                }}""", (None, date(1900, 12, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{death_year and age|1900|1800|12}}
                }}""", (None, date(1900, 12, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ death year and age |1900|1800|12}}
                }}""", (None, date(1900, 12, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|}}
                test = 1900|1800
                }}""", (None, None)),
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|1900|1800}}
                }}""", (None, date(1900, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{death_year and age|1900|1800}}
                }}""", (None, date(1900, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ death year and age |1900|1800}}
                }}""", (None, date(1900, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|mf=yes|2017}}
                }}""", (None, date(2017, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ death year and age |mf=yes|2017}}
                }}""", (None, date(2017, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|2017|ms=y}}
                }}""", (None, date(2017, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ death year and age |2017|ms=y}}
                }}""", (None, date(2017, 1, 1))),

            ("""{{Infobox Person
                death_date = 1900年2月2日
                }}""", (None, date(1900, 2, 2))),
            ("""{{Infobox Person
                death_date = 1900年2月
                }}""", (None, date(1900, 2, 1))),
            ("""{{Infobox Person
                death_date = 1900年
                }}""", (None, date(1900, 1, 1))),

            ("""{{Infobox Person
                death_date = 2 Feb, 1900
                }}""", (None, date(1900, 2, 2))),
            ("""{{Infobox Person
                death_date = 28 August 1919
                }}""", (None, date(1919, 8, 28))),

            ("""{{Infobox_Scientist 
                |name = -{zh-hans:克劳德·艾尔伍德·香农; zh-hant:克勞德·夏農}-
                |image = ClaudeShannon MFO3807.jpg
                |birth_date = {{BirthDeathAge|B|1916|4|30|}}
                |birth_place = [[密西根州]][[佩托斯基]] 
                |death_place = [[麻省]][[梅得福鎮]]
                |nationality = {{USA}}
                """, (date(1916, 4, 30), None)),

            ("""{{Infobox_Scientist 
                |name = -{zh-hans:克劳德·艾尔伍德·香农; zh-hant:克勞德·夏農}-
                |image = ClaudeShannon MFO3807.jpg
                |birth_date = {{BirthDeathAge|B|1916|4|30|2001|2|24|}}
                |birth_place = [[密西根州]][[佩托斯基]] 
                |death_date = {{BirthDeathAge||1916|4|30|2001|2|24|}}
                |death_place = [[麻省]][[梅得福鎮]]
                |nationality = {{USA}}
                """, (date(1916, 4, 30), date(2001, 2, 24))),
        ]
        for input, expected in cases:
            self.assertEqual(expected, utils.get_birth_death_date(input))
