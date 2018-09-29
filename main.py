#!/usr/bin/env python3

import time
from changed import changed

minutes = 30
waiting_time = 60*minutes

time.sleep(120)
while True:
    changed()
    time.sleep(waiting_time)
