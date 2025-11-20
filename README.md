Скрипт для обработки csv файлов.

## Описание слоев:

- **Domain Layer** - содержит бизнес-логику и сущности
- **Application Layer** - координирует работу компонентов
- **Infrastructure Layer** - работа с файлами, БД, внешними API
- **Presentation Layer** - интерфейс пользователя (CLI)


Запуск:

poetry install --no-root
poetry env activate


python3 main.py --help
