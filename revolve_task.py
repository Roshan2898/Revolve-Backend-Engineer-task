#!/usr/bin/env python
# coding: utf-8

# In[48]:


import csv


class Revolve_Task:

    # 1. How many total number of days does the flights table cover?
    def total_days(self, flights):

        """
        Parameters:
        flights(file): flights CSV file

        Returns:
        int: number of days

        """
        unique_days = []
        with open(flights, mode='r') as file:
            csvFile = csv.DictReader(file)
            for line in csvFile:
                date = (line["year"], line["month"], line["day"])
                unique_days.append(date)
        return len(set(unique_days))
    # returns 365 days

    # 2. how many departure cities (not airports)
    # does the flights database cover?
    def departure_cities_list(self, flights, airports):

        """
        Parameters:
        flights(file): flights CSV file
        airports(file): airports CSV file

        Returns:
        list: list of departure cities
        """
        dep_airports = []
        result_cities = []
        with open(flights) as flights_file, open(airports) as airports_file:
            flightsFile = csv.DictReader(flights_file)
            dep_airports = [lines["origin"] for lines in flightsFile
                            if lines["origin"] not in dep_airports]
            airportsFile = csv.DictReader(airports_file)
            result_cities = [line["CITY"] for line in airportsFile
                             for airport in dep_airports
                             if line["IATA_CODE"] == airport]

        return sorted(set(result_cities))
    # returns ['New York', 'Newark']

    # 3. what is the relationship between flights and planes tables?
    def relation(self, flights, planes):

        """
        Parameters:
        flights(file): flights CSV file
        planes(file): planes CSV file

        Returns:
        list: relation between flights and planes table
        """
        with open(flights) as flights_file:
            flightsFile = csv.reader(flights_file)
            lines_flight = next(flightsFile)
            with open(planes) as planes_file:
                planesFile = csv.reader(planes_file)
                lines_plane = next(planesFile)
                relationship = [
                    r for r in lines_flight if r in lines_plane
                ]
        if relationship:
            return set(relationship)
        else:
            return 'no relation'

    # 4. which airplane manufacturer incurred the
    #  most delays in the analysis period?
    def delay_manufacturer(self, flights_file, planes_file):

        """
        Parameters:
        flights(file): flights CSV file
        planes(file): planes CSV file

        Returns:
        str: returns name of the manufacturer with most delays
        """
        delay_count = dict()
        result = ""
        with open(flights_file) as flights:
            flights_reader = csv.DictReader(flights)
            for line in flights_reader:
                tailnum = line["tailnum"]
                arr_delay = "".join(x for x in line["arr_delay"]
                                    if x.isdigit())
                dep_delay = "".join(x for x in line["dep_delay"]
                                    if x.isdigit())
                if line["tailnum"] not in delay_count:
                    if arr_delay != "" and dep_delay != "":
                        if int(dep_delay) > 0 and int(arr_delay) > 0:
                            delay_count[tailnum] = int(arr_delay) + int(
                                dep_delay
                            )
                    elif dep_delay != "":
                        if int(dep_delay) > 0:
                            delay_count[tailnum] = int(dep_delay)
                    elif arr_delay != "":
                        if int(arr_delay) > 0:
                            delay_count[tailnum] = int(arr_delay)
                    else:
                        line["tailnum"] = 0
                else:
                    if arr_delay != "" and dep_delay != "":
                        if int(dep_delay) > 0 and int(arr_delay) > 0:
                            delay_count[tailnum] += int(arr_delay) + int(
                                dep_delay
                            )
                    elif dep_delay != "":
                        if int(dep_delay) > 0:
                            delay_count[tailnum] += int(dep_delay)
                    elif arr_delay != "":
                        if int(arr_delay) > 0:
                            delay_count[tailnum] += int(arr_delay)
        sorted_delayed_tailnums = sorted(
            delay_count.items(), key=lambda item: item[1]
        )
        i = 1
        while i < len(sorted_delayed_tailnums):
            with open(planes_file) as planes:
                planes_reader = csv.DictReader(planes)
                for line in planes_reader:
                    if line["tailnum"] == sorted_delayed_tailnums[-i][0]:
                        result = line["manufacturer"]
                        i = len(sorted_delayed_tailnums)
            i += 1
        return result
    # returns EMBRAER

    # 5 which are the two most connected cities?
    def connected_cities(self, flights_file, airports_file):

        """
        Parameters:
        flights(file): flights CSV file
        airports(file): airports CSV file

        Returns:
        list: returns list of 2 most connected cities
        """
        with open(flights_file) as flights:
            connected_airports_dict = dict()
            flights_reader = csv.DictReader(flights)
            for line in flights_reader:
                if ((line["origin"], line["dest"]) not in
                        connected_airports_dict):
                    connected_airports_dict[(line["origin"], line["dest"])] = 1
                connected_airports_dict[(line["origin"], line["dest"])] += 1
            most_connected_airports = sorted(
                connected_airports_dict.items(), key=lambda item: item[1]
            )[-1]
        cities = []
        with open(airports_file) as airports:
            airports_reader = csv.DictReader(airports)
            cities = [line["CITY"] for line in airports_reader
                      for airport in most_connected_airports[0]
                      if airport == line["IATA_CODE"]]
        return cities
    # returns ['New York', 'Los Angeles']


if __name__ == "__main__":
    obj = Revolve_Task()

    print(obj.total_days("flights.csv"))
    print(
        obj.departure_cities_list("flights.csv", "airports.csv")
    )

    print(obj.relation("flights.csv", "planes.csv"))
    print(
        obj.delay_manufacturer("flights.csv", "planes.csv")
    )
    print(
        obj.connected_cities("flights.csv", "airports.csv")
    )
