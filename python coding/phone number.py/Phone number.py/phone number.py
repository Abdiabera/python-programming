import phonenumbers
from test import number
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(numbers,"CH")
print(geocoder.description_for_number(ch_nmber, "en"))