from Backend.mystery import Routine

with Routine() as Bot:
    Bot.land_first_page()
    Bot.get_info('CSE221','CSE320','CSE321','CSE422')