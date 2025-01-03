from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Entry:
    sale: str
    title: str
    price: float
    date: datetime = field(init=False)

    def __post_init__(self):
        self.date = datetime.now()
