from abc import ABC, abstractmethod
from pydantic import BaseModel

class ILoco(ABC):
    @abstractmethod
    def testando(u: str) -> None:
        pass
    
if __name__ == "__main__":
    class ola(ILoco):
        def testando(u: int) -> None:
            print("o loco")
        
    como = ola()
    como.testando(5)