Скрипт для обработки csv файлов.

src/
├── domain/              # Доменный слой (бизнес-логика)
├── application/         # Слой приложения (use cases, сервисы)
├── infrastructure/      # Инфраструктурный слой (внешние зависимости)
└── presentation/        # Слой представления (CLI)


Запуск:

poetry install --no-root
poetry env activate


python3 main.py --help
