#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.my_strings: list[tuple[int, str]] = []
        self.rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.my_strings.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        items = data if isinstance(data, list) else [data]
        return all(isinstance(elem, (int, float)) for elem in items)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data!")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.my_strings.append((self.rank_counter, str(item)))
            self.rank_counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        items = data if isinstance(data, list) else [data]
        return all(isinstance(elem, str) for elem in items)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data!")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.my_strings.append((self.rank_counter, str(item)))
            self.rank_counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        items = data if isinstance(data, list) else [data]
        return all(
            isinstance(elem, dict)
            and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in elem.items()
            )
            for elem in items
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data!")
        items = data if isinstance(data, list) else [data]
        for item in items:
            formatted_text = ": ".join(item.values())
            self.my_strings.append((self.rank_counter, formatted_text))
            self.rank_counter += 1


def test_processor(
    processor: DataProcessor,
    name: str,
    label: str,
    to_validate: list[Any],
    invalid_ingest: list[Any],
    valid_data: list[Any],
    extract: int,
) -> None:
    print(f"Testing {name} Processor")

    for elem in to_validate:
        print(
            f" Trying to validate input '{elem}': {processor.validate(elem)}"
        )
    for elem in invalid_ingest:
        print(
            f" Test invalid ingestion of {type(elem).__name__} "
            f"'{elem}' without prior validation:"
        )
        try:
            processor.ingest(elem)
        except Exception as e:
            print(f" Got exception: {e}")
    processor.ingest(valid_data)
    print(f" Processing data: {valid_data}")
    plural = "value" if extract == 1 else "values"
    print(f" Extracting {extract} {plural}...")
    for _ in range(extract):
        rank, value = processor.output()
        print(f" {label}: {rank}: {value}")
    print()


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    common = [42, "Hello", "foo", 32.44]
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    test_processor(
        NumericProcessor(),
        "Numeric",
        "Numeric value",
        common,
        ["foo"],
        [1, 2, 3, 4, 5],
        3,
    )
    test_processor(
        TextProcessor(),
        "Text",
        "Text value",
        common,
        [42],
        ["Hello", "Nexus", "World"],
        1,
    )
    test_processor(
        LogProcessor(), "Log", "Log entry", common, [42, {"a": 1}], logs, 2
    )


if __name__ == "__main__":
    main()
