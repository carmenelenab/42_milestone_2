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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            batch = []
            for _ in range(nb):
                if proc.my_strings:
                    batch.append(proc.output())
            plugin.process_output(batch)


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(item[1] for item in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{rank}": "{text}"' for rank, text in data]
        json_str = "{" + ", ".join(items) + "}"
        print(json_str)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()
    stream = DataStream()
    stream.print_processors_stats()
    print()
    print("Registering Processors")
    print()
    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {first_batch}")

    print()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    print()
    stream.print_processors_stats()

    print()
    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {second_batch}")
    print()
    stream.process_stream(second_batch)
    stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plug")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
