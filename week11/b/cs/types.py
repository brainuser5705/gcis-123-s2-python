from dataclassses import dataclass
from typing import Union, Any, Hashable, List, Callable

@dataclass
class Entry:
    key: Hashable
    value: Any

@dataclass
class Hashtable:
    table: List[Entry]
    size: int
    capacity: int
    hash_func: Callable[[Hashable], int]
