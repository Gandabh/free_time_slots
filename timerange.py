import helpers as h
from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time : str
    end_time : str
    
    start_minutes : int = field(init=False, repr=False)
    end_minutes : int = field(init=False, repr=False)
    
    minutes_range : range = field(init=False, repr=False)
    
    
    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)
        self.minutes_range=range(self.start_minutes, self.end_minutes, 1)