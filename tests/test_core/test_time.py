import pytest
from datetime import datetime, timedelta
from src.core.time import SimulationClock, datetime_to_julian, julian_to_datetime

def test_datetime_julian_conversion():
    dt = datetime(2025, 7, 7, 12, 0, 0)
    jd = datetime_to_julian(dt)
    dt_back = julian_to_datetime(jd)
    assert abs((dt - dt_back).total_seconds()) < 1e-6

def test_simulation_clock_to_utc_and_back():
    start = datetime(2025, 7, 7, 12, 0, 0)
    clock = SimulationClock(start)

    t_rel = 3600
    utc = clock.to_utc(t_rel)
    rel = clock.to_relative(utc)

    assert utc == start + timedelta(seconds=t_rel)
    assert abs(rel - t_rel) < 1e-9

def test_simulation_clock_to_julian():
    start = datetime(2025, 7, 7, 12, 0, 0)
    clock = SimulationClock(start)
    t_rel = 3600

    jd_rel = clock.to_julian(t_rel)
    expected_jd = datetime_to_julian(start) + t_rel / 86400

    assert abs(jd_rel - expected_jd) < 1e-9

def test_simulation_clock_advance_and_properties():
    start_time = datetime(2022, 6, 1, 0, 0, 0)
    clock = SimulationClock(start_time)

    assert clock.t_rel == 0.0
    assert clock.t_utc == start_time
    assert abs(clock.t_jd - datetime_to_julian(start_time)) < 1e-6

    clock.advance(9000)

    assert clock.t_rel == 9000
    assert clock.t_utc == start_time + timedelta(seconds=9000)
    assert abs(clock.t_jd - datetime_to_julian(start_time + timedelta(seconds=9000))) < 1e-6