"""Тесты для доменных отчетов."""

import pytest

from src.domain.reports import PerformanceReport, ReportResult
from src.domain.entities import Employee


def test_performance_report_generate(sample_employees):
    """Тест генерации отчета по производительности."""
    report = PerformanceReport()
    result = report.generate(sample_employees)

    assert isinstance(result, ReportResult)
    assert result.headers == ["position", "performance"]
    assert len(result.rows) == 2

    assert result.rows[0][0] == "Backend Developer"
    assert result.rows[0][1] == 4.85

    assert result.rows[1][0] == "Frontend Developer"
    assert result.rows[1][1] == 4.7


def test_performance_report_empty_list():
    """Тест генерации отчета с пустым списком разработчиков."""
    report = PerformanceReport()
    result = report.generate([])

    assert isinstance(result, ReportResult)
    assert result.headers == ["position", "performance"]
    assert result.rows == []


def test_performance_report_single_employee():
    """Тест генерации отчета с одним разработчиком."""
    employee = Employee(
        name="Solo Dev",
        position="DevOps Engineer",
        completed_tasks=40,
        performance=4.5,
        skills="Docker, Kubernetes",
        team="Infrastructure",
        experience_years=3,
    )

    report = PerformanceReport()
    result = report.generate([employee])

    assert len(result.rows) == 1
    assert result.rows[0][0] == "DevOps Engineer"
    assert result.rows[0][1] == 4.5


def test_performance_report_sorting():
    """Тест сортировки отчета по производительности (по убыванию)."""
    employees = [
        Employee("Dev1", "QA Engineer", 30, 4.3, "Testing", "QA", 2),
        Employee("Dev2", "Backend Developer", 50, 4.9, "Python", "Backend", 5),
        Employee("Dev3", "Frontend Developer", 40, 4.6, "React", "Frontend", 3),
    ]

    report = PerformanceReport()
    result = report.generate(employees)

    assert result.rows[0][1] == 4.9
    assert result.rows[1][1] == 4.6
    assert result.rows[2][1] == 4.3
