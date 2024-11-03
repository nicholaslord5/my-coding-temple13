# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the 
# flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

# Example Code:

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_routes = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", shared_routes)

unique_to_us = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_us)

neither_shared_routes = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", neither_shared_routes)
