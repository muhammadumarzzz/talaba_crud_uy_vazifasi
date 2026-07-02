#!/usr/bin/env python
"""Django boshqaruv buyruqlari uchun fayl. Buni o'zgartirish shart emas."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'talaba_crud.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django o'rnatilmagan ko'rinadi. venv faollashtirilganini va "
            "'pip install -r requirements.txt' bajarilganini tekshiring."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
