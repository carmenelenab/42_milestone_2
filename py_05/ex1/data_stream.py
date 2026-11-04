#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.my_strings: list[tuple[int, str]] = []
        self.rank_counter: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.my_strings:
            raise IndexError("No data available in the processor")
        return self.my_strings.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
    def validate(self, data: typing.Any) -> bool:
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
    def validate(self, data: typing.Any) -> bool:
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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[typing.Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for elem in stream:
            for proc in self.processors:
                if proc.validate(elem):
                    proc.ingest(elem)
                    break
            else:
                print(
                    "-->DataStream error - "
                    f"Can't process element in stream {elem}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        proc_name = {
            "NumericProcessor": "Numeric Processor",
            "TextProcessor": "Text Processor",
            "LogProcessor": "Log Processor",
        }
        for proc in self.processors:
            raw_name = proc.__class__.__name__
            print_name = proc_name.get(raw_name, raw_name)
            print(
                f"{print_name}: total {proc.rank_counter} items processed, "
                f"remaining {len(proc.my_strings)} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    stream = DataStream()
    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
        ],
        42,
        ["Hi", "Five"],
        None,
    ]
    stream.print_processors_stats()
    print()

    print("Registering Numeric Processor")
    print(f"Send first batch of data to stream: {data}")
    stream.register_processor(NumericProcessor())
    stream.process_stream(data)
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    stream.process_stream(data)
    stream.print_processors_stats()
    print()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    try:
        for count, proc in zip([3, 2, 1], stream.processors):
            for _ in range(count):
                proc.output()
        stream.print_processors_stats()
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()
