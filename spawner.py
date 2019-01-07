#!/usr/bin/env python3
import sys

InstaUsr =sys.argv[1]
InstaID  =sys.argv[2]
InstaLink=sys.argv[3]
#
# TBD - Write to a specific LOG file, based on month/day
print("Spawner(",InstaUsr,",",InstaID,",",InstaLink,")")

# TBD - Adjust Polling script to build a list of ALL links ? See below..
#session.interact_by_URL(urls=["Fv0J4AJ3Y7r/?taken-at=628416252", "Vb0D4bJgY7r" "Dj0J4VJgY7r"], randomize=True, interact=True)

# TBD - Setup MySQL database with USER table. 
# TBD - Query Database, for every OTHER user in 'pool'
# TBD - Loop For EACH user
#     - TBD - Get User/Pass/Proxy IP
#     - TBD - Pass User Info + Instagram Post URL(Link) to Instapy Script
#     - TBD - Update #'s? Keep track of Number of accumulated likes?
