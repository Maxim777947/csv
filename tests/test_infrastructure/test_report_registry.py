import pytest

from src.domain.reports import PerformanceReport, Report
from src.infrastructure.report_registry import ReportRegistry


def test_report_registry_initialization():
    """Тест инициализации реестра с дефолтными отчетами."""
    registry = ReportRegistry()
    available = registry.get_available_reports()

    assert "performance" in available


def test_report_registry_get_performance_report():
    """Тест получения отчета performance из реестра."""
    registry = ReportRegistry()
    report = registry.get_report("performance")

    assert isinstance(report, PerformanceReport)
    assert isinstance(report, Report)
    assert report.get_name() == "performance"


def test_report_registry_unknown_report():
    """Тест ошибки при запросе неизвестного отчета."""
    registry = ReportRegistry()

    with pytest.raises(ValueError) as exc_info:
        registry.get_report("unknown_report")

    error_message = str(exc_info.value)
    assert "не найден" in error_message
    assert "unknown_report" in error_message
    assert "performance" in error_message


def test_report_registry_get_available_reports():
    """Тест получения списка доступных отчетов."""
    registry = ReportRegistry()
    available = registry.get_available_reports()

    assert isinstance(available, list)
    assert len(available) >= 1
    assert "performance" in available
