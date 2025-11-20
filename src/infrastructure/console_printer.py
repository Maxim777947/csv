from tabulate import tabulate

from src.domain.reports import ReportResult


class ConsolePrinter:
    @staticmethod
    def print_report(report_result: ReportResult) -> None:
        table = tabulate(
            report_result.rows, headers=report_result.headers, tablefmt="simple"
        )
        print(table)
