#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any

class My_exceptions:
    pass


class DataProcessor(ABC):

    def __init__(self):
        self.my_list = []
        self.rank = self.my_list[0:]
        pass


    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass


    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        input = None
        try:
            # if data is not validated , raise exception
            if validate(input):
                input = (1, "Sa vedem!")
            input = (2, "Inca putin")
        except Exception as e:
            print(f"Invalid data: {e}")
        return


class NumericProcessor(DataProcessor):
    
    def validate(self, data):
        super().validate(data)
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) & all(isinstance(item, (int, float)) for item in data):
            return True
        return False
    

    def ingest(self, data):
        return super().ingest(data)


class TextProcessor(DataProcessor):

    def validate(self, data):
        super().validate(data)
        if isinstance(data, str):
            return True
        if isinstance(data, list) & all(isinstance(item, str) for item in data):
            return True
        return False


    def ingest(self, data):
        return super().ingest(data)
    

class LogProcessor(DataProcessor):

    def validate(self, data):
        super().validate(data)
        return isinstance(data, all(dict, list[dict]))


    def ingest(self, data):
        return super().ingest(data)


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    to_test = [42, "Hello"]
    for item in to_test:
        print()
    if len(sys.argv) < 2:
        input
    


if __name__ == "__main__":
    main()