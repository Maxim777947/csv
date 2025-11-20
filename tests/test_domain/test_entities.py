"""Тесты для доменных сущностей."""

import pytest

from src.domain.entities import Employee


def test_employee_creation():
    employee = Employee(
        name="John Doe",
        position="Backend Developer",
        completed_tasks=50,
        performance=4.8,
        skills="Python, Django",
        team="API Team",
        experience_years=5,
    )

    assert employee.name == "John Doe"
    assert employee.position == "Backend Developer"
    assert employee.completed_tasks == 50
    assert employee.performance == 4.8
    assert employee.skills == "Python, Django"
    assert employee.team == "API Team"
    assert employee.experience_years == 5


def test_employee_immutability():
    employee = Employee(
        name="John Doe",
        position="Backend Developer",
        completed_tasks=50,
        performance=4.8,
        skills="Python, Django",
        team="API Team",
        experience_years=5,
    )

    with pytest.raises(Exception):
        employee.name = "Jane Doe"
