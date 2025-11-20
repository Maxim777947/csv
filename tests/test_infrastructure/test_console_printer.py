import pytest

from src.infrastructure.console_printer import ConsolePrinter
from src.domain.reports import ReportResult


def test_console_printer_output(capsys):
    """Тест вывода отчета в консоль."""
    result = ReportResult(
        headers=["position", "performance"],
        rows=[["Backend Developer", 4.8], ["Frontend Developer", 4.7]],
    )

    ConsolePrinter.print_report(result)

    captured = capsys.readouterr()
    output = captured.out
    assert "position" in output
    assert "performance" in output
    assert "Backend Developer" in output
    assert "4.8" in output
    assert "Frontend Developer" in output
    assert "4.7" in output


def test_console_printer_empty_report(capsys):
    """Тест вывода пустого отчета."""
    result = ReportResult(headers=["position", "performance"], rows=[])

    ConsolePrinter.print_report(result)

    captured = capsys.readouterr()
    output = captured.out

    assert "position" in output
    assert "performance" in output
