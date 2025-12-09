import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT', '3306'))  # Преобразуем в число

    @classmethod
    def validate_config(cls):
        print("🔍 ПРОВЕРКА КОНФИГУРАЦИИ...")

        required_vars = ['DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST']
        missing_vars = []

        for var in required_vars:
            value = getattr(cls, var)
            if not value:
                missing_vars.append(var)
                print(f"   ❌ {var}: НЕ УСТАНОВЛЕН")
            else:
                print(f"   ✅ {var}: установлен")

        if missing_vars:
            error_msg = f"Отсутствуют переменные в .env: {', '.join(missing_vars)}"
            raise Exception(error_msg)

        print("✅ Конфигурация загружена успешно")
        return True