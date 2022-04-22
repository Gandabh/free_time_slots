import helpers as h
from timerange import TimeRange
from friend import Friend
from custom_list import CustomList


def main():
    avaiable_minutes = CustomList(range(1440))
    f1 = Friend('Bob')
    f1.add_busy_time_range(TimeRange('00:00', '10:00'))
    f2 = Friend('Alice')
    f2.add_busy_time_range(TimeRange('11:00', '13:50'))
    f2.add_busy_time_range(TimeRange('22:00', '23:00'))
    f3 = Friend('Carol')
    f3.add_busy_time_range(TimeRange('10:00', '10:20'))
    
    for m in avaiable_minutes[:]:
        for r in Friend.all_busy_minutes_ranges:
            if m in r:
                avaiable_minutes.remove_if_exist(m)
    
    for tr in h.converting_avaiable_minutes(avaiable_minutes):
        print(f'You can meet in {tr}')
    
    
if __name__ == '__main__':
    main()