from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Shader:
    color: Tuple[int, int, int]


Shader.white = Shader((255, 255, 255))
