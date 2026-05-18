from typing import List,Dict,Union,TypedDict

class MusicData(TypedDict):
    music_name: str
    features: List[float]
    my_eq: List[float]

