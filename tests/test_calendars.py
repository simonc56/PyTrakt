"""trakt.calendar functional tests"""
from trakt.calendar import (PremiereCalendar, MyPremiereCalendar, ShowCalendar,
                            MyShowCalendar, SeasonCalendar, MySeasonCalendar,
                            MovieCalendar, MyMovieCalendar)

__author__ = 'Jon Nappi'


def test_my_shows():
    """functional tests for the :class:`MyShowCalendar` class"""
    date, days = '2014-09-01', 7
    cal = MyShowCalendar(date=date, days=days)
    assert isinstance(cal, MyShowCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 4


def test_my_premiere_calendar():
    """functional tests for the :class:`MyPremiereCalendar` class"""
    date, days = '2014-09-01', 7
    cal = MyPremiereCalendar(date=date, days=days)
    assert isinstance(cal, MyPremiereCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 1


def test_my_season_calendar():
    """functional tests for the :class:`MySeasonCalendar` class"""
    date, days = '2014-09-01', 7
    cal = MySeasonCalendar(date=date, days=days)
    assert isinstance(cal, MySeasonCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 2


def test_my_movie_calendar():
    """functional tests for the :class:`MyMovieCalendar` class"""
    date, days = '2014-09-01', 7
    cal = MyMovieCalendar(date=date, days=days)
    assert isinstance(cal, MyMovieCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 3


def test_show_calendar():
    """functional tests for the :class:`ShowCalendar` class"""
    date, days = '2014-09-01', 7
    cal = ShowCalendar(date=date, days=days)
    assert isinstance(cal, ShowCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 4


def test_premiere_calendar():
    """functional tests for the :class:`PremiereCalendar` class"""
    date, days = '2014-09-01', 7
    cal = PremiereCalendar(date=date, days=days)
    assert isinstance(cal, PremiereCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 1


def test_season_calendar():
    """functional tests for the :class:`SeasonCalendar` class"""
    date, days = '2014-09-01', 7
    cal = SeasonCalendar(date=date, days=days)
    assert isinstance(cal, SeasonCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 2


def test_movie_calendar():
    """functional tests for the :class:`MovieCalendar` class"""
    date, days = '2014-09-01', 7
    cal = MovieCalendar(date=date, days=days)
    assert isinstance(cal, MovieCalendar)
    assert cal.days == days
    assert cal.date == date
    assert len(cal) == 3
