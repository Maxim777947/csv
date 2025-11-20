import pytest
from pathlib import Path

from src.infrastructure.csv_reader import CSVReader
from src.domain.entities import Employee


def test_read_employees_single_file(temp_csv_file):
    """Тест чтения одного CSV файла."""
    employees = CSVReader.read_employees(str(temp_csv_file))

    assert len(employees) == 1
    assert isinstance(employees[0], Employee)
    assert employees[0].name == "Test User"
    assert employees[0].position == "Backend Developer"
    assert employees[0].completed_tasks == 40
    assert employees[0].performance == 4.5
    assert employees[0].experience_years == 3


def test_read_employees_file_not_found():
    """Тест ошибки при отсутствии файла."""
    with pytest.raises(FileNotFoundError):
        CSVReader.read_employees("non_existent.csv")


def test_read_multiple_files(temp_csv_files):
    """Тест чтения нескольких CSV файлов."""
    file_paths = [str(f) for f in temp_csv_files]
    employees = CSVReader.read_multiple_files(file_paths)

    assert len(employees) == 2
    assert employees[0].name == "User 1"
    assert employees[1].name == "User 2"


def test_read_multiple_files_combines_data(temp_csv_files):
    """Тест объединения данных из нескольких файлов."""
    file_paths = [str(f) for f in temp_csv_files]
    employees = CSVReader.read_multiple_files(file_paths)
    assert isinstance(employees, list)
    assert all(isinstance(emp, Employee) for emp in employees)
    positions = [emp.position for emp in employees]
    assert "Backend Developer" in positions
    assert "Frontend Developer" in positions
