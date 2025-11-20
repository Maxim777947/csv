import argparse
import sys
from typing import List


class CLI:
    def __init__(self) -> None:
        self._parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description="Анализ эффективности работы разработчиков",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
                Примеры использования:
                python3 main.py --files employees1.csv --report performance
                python3 main.py --files employees1.csv employees2.csv --report performance
                            """,
        )

        parser.add_argument(
            "--files",
            nargs="+",
            required=True,
            metavar="FILE",
            help="Путь(и) к CSV файлам с данными о разработчиках",
        )

        parser.add_argument(
            "--report",
            required=True,
            metavar="REPORT_NAME",
            help="Название отчета для генерации (например: performance)",
        )

        return parser

    def parse_args(self, args: List[str] | None = None) -> argparse.Namespace:
        return self._parser.parse_args(args)

    def print_error(self, message: str) -> None:
        print(f"Ошибка: {message}", file=sys.stderr)
        sys.exit(1)
