# test_connection.py
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.db import connections

print("Тестирование подключения к базам данных...")

for db_name in ['default', 'utility']:
    print(f"\n--- Проверка БД: {db_name} ---")
    try:
        if db_name in connections.databases:
            connection = connections[db_name]
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Подключение успешно! Результат теста: {result}")
            cursor.close()
        else:
            print(f"⚠️  БД '{db_name}' не настроена в DATABASES")
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")