import helpers as h
from timerange import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Friend:
    all_busy_minutes_ranges: ClassVar[list] = []
    name: str
    busy_time_ranges: list[TimeRange] = field(default_factory=list, repr=False)
    
    def add_busy_time_range(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)
        Friend.all_busy_minutes_ranges.append(obj.minutes_range)


