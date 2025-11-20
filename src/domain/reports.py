from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any
from collections import defaultdict

from src.domain.entities import Employee


@dataclass
class ReportResult:
    headers: List[str]
    rows: List[List[Any]]


class Report(ABC):
    @abstractmethod
    def generate(self, employees: List[Employee]) -> ReportResult:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class PerformanceReport(Report):
    def get_name(self) -> str:
        return "performance"

    def generate(self, employees) -> ReportResult:
        position_performance = defaultdict(list)

        for employee in employees:
            position_performance[employee.position].append(employee.performance)
            results = []
            for position, performances in position_performance.items():
                avg_performance = sum(performances) / len(performances)
                results.append([position, round(avg_performance, 2)])
            results.sort(key=lambda x: x[1], reverse=True)
        return ReportResult(headers=["position", "performance"], rows=results)
