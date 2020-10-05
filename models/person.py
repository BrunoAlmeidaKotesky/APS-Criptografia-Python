from dataclasses import dataclass
from typing import Optional

@dataclass
class Person():
   id: Optional[int] = -1
   nome: Optional[str] = ''
   sobrenome: Optional[str] = ''
   tipo: Optional[str] = ''
   ususername: Optional[str] = ''
   email: Optional[str] = ''
   senha: Optional[str] = ''