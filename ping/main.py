import _thread
import os

givenIp = input('IP to spam : ')

_thread.start_new_thread(os.system('ping '+givenIp))