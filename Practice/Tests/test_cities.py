import pytest

from city_functions import location

def test_city_country():
    place = location("Toronto","Canadá")
    assert place == "Toronto, Canadá"

def test_city_country_population():
    place = location("Toronto","Canadá", 50000)
    assert place == "Toronto, Canadá - population 50000" 