import sys

from src.presentation.cli import CLI
from src.application.report_service import ReportService
from src.application.use_cases import GenerateReportUseCase
from src.infrastructure.csv_reader import CSVReader
from src.infrastructure.report_registry import ReportRegistry
from src.infrastructure.console_printer import ConsolePrinter


def main() -> None:
    cli = CLI()

    try:
        args = cli.parse_args()
        csv_reader = CSVReader()
        report_registry = ReportRegistry()
        console_printer = ConsolePrinter()
        use_case = GenerateReportUseCase()

        service = ReportService(
            csv_reader=csv_reader,
            report_registry=report_registry,
            console_printer=console_printer,
            use_case=use_case,
        )
        service.generate_and_print_report(
            file_paths=args.files, report_name=args.report
        )

    except FileNotFoundError as e:
        cli.print_error(str(e))
    except ValueError as e:
        cli.print_error(str(e))
    except Exception as e:
        cli.print_error(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
