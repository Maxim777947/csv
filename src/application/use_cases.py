from typing import List
from src.domain.entities import Employee
from src.domain.reports import Report, ReportResult


class GenerateReportUseCase:
    def execute(self, employees: List[Employee], report: Report) -> ReportResult:
        return report.generate(employees)
