import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("enter mobile number with country code:")
mobileNo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNo,"en"))


print("valid mobile number :",phonenumbers.is_valid_number(mobileNo))

print("Checking possibility of number :", phonenumbers.is_possible_number(mobileNo))