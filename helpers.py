def timerange_to_minutes(t_str):
    """
    Convert a string of the form "HH:MM" to minutes since midnight.
    """
    h = t_str.split(':')[0]
    m = t_str.split(':')[1]
    
    return int(h) * 60 + int(m)

def minutes_to_timerange(m):
    """
    Convert minutes since midnight to a string of the form "HH:MM".
    """
    hour = m // 60
    minute = m % 60
    
    return f'{hour:02d}:{minute:02d}'

def converting_avaiable_minutes(l : list):
    grouped_list = []
    list_resettable = []
    for elem in l:
        if list_resettable == []:
            list_resettable.append(elem)
            continue
        
        if list_resettable[-1] + 1 == elem:
            list_resettable.append(elem)
        else:
            grouped_list.append(list_resettable[:])
            list_resettable.clear()
            list_resettable.append(elem)
            
    grouped_list.append(list_resettable)   
    
    time_ranges = []   
    for group in grouped_list:
        start_time = minutes_to_timerange(m=group[0])
        end_time = minutes_to_timerange(m=group[-1])
        time_range_str = f'{start_time}-{end_time}'
        time_ranges.append(time_range_str)
        
    return time_ranges

    

            
    

    