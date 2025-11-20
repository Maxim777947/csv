import csv
from pathlib import Path
from typing import List

from src.domain.entities import Employee


class CSVReader:
    @staticmethod
    def read_employees(file_path: str) -> List[Employee]:
        path = Path(file_path)
        employees = []

        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print()

            for row in reader:
                employee = Employee(
                    name=row["name"],
                    position=row["position"],
                    completed_tasks=int(row["completed_tasks"]),
                    performance=float(row["performance"]),
                    skills=row["skills"],
                    team=row["team"],
                    experience_years=int(row["experience_years"]),
                )
                employees.append(employee)

        return employees

    @staticmethod
    def read_multiple_files(file_paths) -> List[Employee]:
        all_employees = []

        for file_path in file_paths:
            employees = CSVReader.read_employees(file_path)
            all_employees.extend(employees)
        return all_employees
