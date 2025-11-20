from src.domain.reports import PerformanceReport, Report


class ReportRegistry:
    def __init__(self):
        self._reports = {}
        self._register_default_reports()

    def _register_default_reports(self):
        self.register(PerformanceReport)

    def register(self, report_class):
        instance = report_class()
        name = instance.get_name()
        self._reports[name] = report_class

    def get_report(self, report_name: str) -> Report:
        if report_name not in self._reports:
            available = ", ".join(self._reports.keys())
            raise ValueError(
                f"Отчет '{report_name}' не найден. Доступные отчеты: {available}"
            )

        report_class = self._reports[report_name]
        return report_class()

    def get_available_reports(self) -> list[str]:
        return list(self._reports.keys())
