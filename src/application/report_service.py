from typing import List

from src.application.use_cases import GenerateReportUseCase
from src.infrastructure.console_printer import ConsolePrinter
from src.infrastructure.csv_reader import CSVReader
from src.infrastructure.report_registry import ReportRegistry


class ReportService:
    def __init__(
        self,
        csv_reader: CSVReader,
        report_registry: ReportRegistry,
        console_printer: ConsolePrinter,
        use_case: GenerateReportUseCase,
    ) -> None:
        self._csv_reader = csv_reader
        self._report_registry = report_registry
        self._console_printer = console_printer
        self._use_case = use_case

    def generate_and_print_report(
        self, file_paths: List[str], report_name: str
    ) -> None:
        employees = self._csv_reader.read_multiple_files(file_paths)
        report = self._report_registry.get_report(report_name)
        result = self._use_case.execute(employees, report)
        self._console_printer.print_report(result)
