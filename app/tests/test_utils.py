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
                birth_date = {{birth date and age|2017|6|27}}
                }}""", True),
        ]
        for input, expected in cases:
            self.assertEqual(expected, utils.is_wiki_about_person(input))

    def test_get_birth_death_date(self):
        cases = [
            ("test", (None, None)),

            # birth date and age
            ("""{{Infobox Person
                name = test
                birth_date = {{birth date and age|2017|6|27}}
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
                birth_date = {{birth date|1500|2|3}}
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
                birth_date = {{birth year and age|2017}}
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

            # death date and age
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
                death_date = {{Death date|1600|2|2}}
                }}""", (None, date(1600, 2, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date |1600|2|2}}
                }}""", (None, date(1600, 2, 2))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|1600|2}}
                }}""", (None, date(1600, 2, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date |1600|2}}
                }}""", (None, date(1600, 2, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{Death date|1600}}
                }}""", (None, date(1600, 1, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ Death date |1600}}
                }}""", (None, date(1600, 1, 1))),

            # death year and age
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|1900|1800|12}}
                }}""", (None, date(1900, 12, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{ death year and age |1900|1800|12}}
                }}""", (None, date(1900, 12, 1))),
            ("""{{Infobox Person
                name = test
                death_date = {{death year and age|1900|1800}}
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
        ]
        for input, expected in cases:
            self.assertEqual(expected, utils.get_birth_death_date(input))
