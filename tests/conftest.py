import pytest
from typing import List
from pathlib import Path
import tempfile
import csv

from src.domain.entities import Employee


@pytest.fixture
def sample_employees() -> List[Employee]:
    return [
        Employee(
            name="Alex Ivanov",
            position="Backend Developer",
            completed_tasks=45,
            performance=4.8,
            skills="Python, Django, PostgreSQL",
            team="API Team",
            experience_years=5,
        ),
        Employee(
            name="Maria Petrova",
            position="Frontend Developer",
            completed_tasks=38,
            performance=4.7,
            skills="React, TypeScript, Redux",
            team="Web Team",
            experience_years=4,
        ),
        Employee(
            name="John Smith",
            position="Backend Developer",
            completed_tasks=50,
            performance=4.9,
            skills="Go, Microservices",
            team="API Team",
            experience_years=6,
        ),
    ]


@pytest.fixture
def temp_csv_file() -> Path:
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "name",
                "position",
                "completed_tasks",
                "performance",
                "skills",
                "team",
                "experience_years",
            ]
        )
        writer.writerow(
            [
                "Test User",
                "Backend Developer",
                "40",
                "4.5",
                "Python, Django",
                "Test Team",
                "3",
            ]
        )
        temp_path = Path(f.name)

    yield temp_path
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def temp_csv_files() -> List[Path]:
    files = []

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "name",
                "position",
                "completed_tasks",
                "performance",
                "skills",
                "team",
                "experience_years",
            ]
        )
        writer.writerow(
            ["User 1", "Backend Developer", "40", "4.5", "Python", "Team A", "3"]
        )
        files.append(Path(f.name))

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "name",
                "position",
                "completed_tasks",
                "performance",
                "skills",
                "team",
                "experience_years",
            ]
        )
        writer.writerow(
            ["User 2", "Frontend Developer", "35", "4.6", "React", "Team B", "2"]
        )
        files.append(Path(f.name))

    yield files

    for file_path in files:
        if file_path.exists():
            file_path.unlink()
