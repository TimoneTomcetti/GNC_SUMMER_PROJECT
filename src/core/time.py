"""
Module for time conversions and simulation clock management.

Includes functions to convert between datetime and Julian date,
and a SimulationClock class for handling simulation-relative and UTC times.
"""

from datetime import datetime, timedelta

def datetime_to_julian(dt: datetime) -> float:
    """
    Converts a datetime object to Julian Date.

    Parameters
    ----------
    dt : datetime
        The datetime to convert.

    Returns
    -------
    float
        Julian Date corresponding to the input datetime.
    """
    unix_epoch = datetime(1970,1,1)
    delta = dt - unix_epoch
    return 2440587.5 + delta.total_seconds() / 86400

def julian_to_datetime(jd: float) -> datetime:
    """
    Converts a Julian Date to a datetime object.

    Parameters
    ----------
    jd : float
        Julian Date to convert.

    Returns
    -------
    datetime
        Corresponding datetime in UTC.
    """
    unix_epoch = datetime(1970,1,1)
    seconds = (jd - 2440587.5) * 86400
    return unix_epoch + timedelta(seconds=seconds)

class SimulationClock:
    """
    Manages simulation time by tracking both relative time and its
    corresponding absolute representations (UTC, Julian Date).

    This utility allows consistent progression of time during a simulation,
    and conversion between different time formats.

    Attributes
    ----------
    start_time : datetime
        UTC datetime at which the simulation starts (t = 0).
    start_jd : float
        Julian Date corresponding to `start_time`.
    current_time_rel : float
        Current simulation time in seconds since start.
    """

    def __init__(self, start_time_utc: datetime):
        """
        Initializes the simulation clock.

        Parameters
        ----------
        start_time_utc : datetime
            UTC time corresponding to the simulation start (t = 0).
        """
        self.start_time = start_time_utc
        self.start_jd = datetime_to_julian(start_time_utc)
        self.current_time_rel = 0.0

    def advance(self, dt: float):
        """
        Advances the simulation clock by a given time step.

        Parameters
        ----------
        dt : float
            Time step in seconds to advance the simulation time.
        """
        self.current_time_rel += dt

    def to_utc(self, t_rel: float) -> datetime:
        """
        Converts relative simulation time to UTC.

        Parameters
        ----------
        t_rel : float
            Simulation time in seconds since start.

        Returns
        -------
        datetime
            UTC time corresponding to t_rel.
        """
        return self.start_time + timedelta(seconds=t_rel)

    def to_julian(self, t_rel: float) -> float:
        """
        Converts relative simulation time to Julian Date.

        Parameters
        ----------
        t_rel : float
            Simulation time in seconds since start.

        Returns
        -------
        float
            Julian Date corresponding to t_rel.
        """
        return self.start_jd + t_rel / 86400

    def to_relative(self, utc_time: datetime) -> float:
        """
        Converts UTC datetime to relative simulation time (seconds since start).

        Parameters
        ----------
        utc_time : datetime
            Absolute UTC time.

        Returns
        -------
        float
            Relative simulation time in seconds.
        """
        return (utc_time - self.start_time).total_seconds()

    @property
    def t_rel(self):
        """
        Returns the current simulation time (seconds since start).

        Returns
        -------
        float
            Current simulation time in seconds.
        """
        return self.current_time_rel

    @property
    def t_utc(self):
        """
        Returns the current UTC time based on the simulation clock.

        Returns
        -------
        datetime
            Current UTC time.
        """
        return self.to_utc(self.current_time_rel)

    @property
    def t_jd(self):
        """
        Returns the current Julian Date based on the simulation clock.

        Returns
        -------
        float
            Current Julian Date.
        """
        return self.to_julian(self.current_time_rel)
