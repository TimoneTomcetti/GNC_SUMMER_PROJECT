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
    Manages absolute (UTC, Julian Date) and relative (simulation) time conversions.

    This utility helps maintain consistency between wall-clock time (e.g., from TLEs or logs)
    and relative simulation time (e.g., t = 0 at simulation start).

    Attributes
    ----------
    start_time : datetime
        UTC datetime at which the simulation starts.
    start_jd : float
        Julian Date corresponding to `start_time`.
    """

    def __init__(self, start_time: datetime):
        """
        Initializes the clock with a given simulation start time.

        Parameters
        ----------
        start_time : datetime
            UTC time corresponding to t = 0 in the simulation.
        """
        self.start_time = start_time
        self.start_jd = datetime_to_julian(start_time)

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

    def __call__(self, t_rel: float) -> datetime:
        """
        Enables the object to be called like a function to return UTC time.

        Equivalent to calling `to_utc()`.

        Parameters
        ----------
        t_rel : float
            Relative simulation time in seconds.

        Returns
        -------
        datetime
            Corresponding UTC time.
        """
        return self.to_utc(t_rel)
