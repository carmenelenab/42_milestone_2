#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing

class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        if data is not [int, float, list[int], list[float], list[int, float]]:
            return False
        return True


    @abstractmethod
    def ingest(self, data: Any) -> None:
            pass

    def output(self) -> tuple[int, str]:
        input = None
        try:
            if validate(input) is False:
                raise Exception("Sa vedem ce o sa iasa!") 
            return input
        except:


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


def main() -> None:
    input = None
    


if __name__ == "__main__":
    main()