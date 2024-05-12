def print_seconds_per_day(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(seconds)


print_seconds_per_day(7)
print_seconds_per_day(0)
print_seconds_per_day(1237)
print_seconds_per_day(9)
print_seconds_per_day(7000000000)
print_seconds_per_day(11*365)