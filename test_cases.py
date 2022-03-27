#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import revolve_task


obj = revolve_task.Revolve_Task()


def test_total_days():
    result = obj.total_days("flights.csv")
    assert result == 365


def test_departure_cities_list():
    result = obj.departure_cities_list("flights.csv", "airports.csv")
    assert result == ["New York", "Newark"]


def test_relation():
    result = obj.relation("flights.csv", "Planes.csv")
    assert result == {"tailnum", "year"}


def test_delay_manufacturer():
    result = obj.delay_manufacturer("flights.csv", "planes.csv")
    assert result == "EMBRAER"


def test_connected_cities():
    result = obj.connected_cities("flights.csv", "airports.csv")
    assert result == ["New York", "Los Angeles"]

# (base) C:\Users\91703\python_task_revolve_soln>pytest
# ============================================================================================== test session starts ===============================================================================================
# platform win32 -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
# rootdir: C:\Users\91703\python_task_revolve_soln
# plugins: anyio-2.2.0
# collected 5 items

# test_cases.py .....                                                                                                                                              [100%]                                           [100%]

# ========================================================================================= 5 passed in 4.68s ==========================================================================================
