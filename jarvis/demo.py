#!/usr/bin/env python3
"""
Демонстрация Jarvis AI Assistant
Автор: Jarvis AI Assistant
Версия: 1.0.0
"""

import requests
import json
import time

def test_api():
    """Тестирование API"""
    base_url = "http://localhost:8000"
    
    print("🤖 Jarvis AI Assistant - Демонстрация")
    print("=" * 50)
    
    # Проверка здоровья
    print("1. Проверка здоровья сервиса...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Сервис здоров: {data['service']} v{data['version']}")
        else:
            print(f"❌ Ошибка: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return
    
    # Проверка статуса
    print("\n2. Получение статуса...")
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Статус: {data['status']}")
            print(f"   Активных соединений: {data['active_connections']}")
            print(f"   Всего сообщений: {data['total_messages']}")
        else:
            print(f"❌ Ошибка: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    # Тестирование сообщений
    print("\n3. Тестирование сообщений...")
    test_messages = [
        "Привет, Jarvis!",
        "Как дела?",
        "Который час?",
        "Что ты умеешь?",
        "Спасибо за помощь!"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n   Тест {i}: {message}")
        try:
            response = requests.post(
                f"{base_url}/message",
                json={"text": message, "user_id": "demo_user"}
            )
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Ответ: {data['data']['response']}")
            else:
                print(f"   ❌ Ошибка: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
        
        time.sleep(1)  # Пауза между сообщениями
    
    # Получение всех сообщений
    print("\n4. Получение истории сообщений...")
    try:
        response = requests.get(f"{base_url}/messages")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Получено {len(data['messages'])} сообщений")
            for msg in data['messages'][-3:]:  # Последние 3 сообщения
                print(f"   - {msg['text']} (от {msg['user_id']})")
        else:
            print(f"❌ Ошибка: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Демонстрация завершена!")
    print("🌐 Веб-интерфейс доступен по адресу: http://localhost:8000")
    print("📚 API документация: http://localhost:8000/docs")

if __name__ == "__main__":
    test_api()