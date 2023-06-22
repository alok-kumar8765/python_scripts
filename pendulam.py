# import library

import pendulum
dt = pendulum.datetime(2023, 1, 31)
print(dt)
 
#local() creates datetime instance with local timezone

local = pendulum.local(2023, 1, 31)
print("Local Time:", local)
print("Local Time Zone:", local.timezone.name)

# Printing UTC time

utc = pendulum.now('UTC')
print("Current UTC time:", utc)
 
# Converting UTC timezone into Europe/Paris time

europe = utc.in_timezone('Europe/Paris')
print("Current time in Paris:", europe)