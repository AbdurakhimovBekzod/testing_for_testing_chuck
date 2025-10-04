import requests
import json

class TestChuckNorrisAPI:
    """Тесты API шуток про Чака Норриса"""

    BASE_URL = "https://api.chucknorris.io/jokes/random"

    def test_create_random_joke_category(self):
        """Проверка получения шутки по категории"""

        category = "animal"
        url = f"{self.BASE_URL}?category={category}"
        print(f"Отправляю запрос: {url}")

        response = requests.get(url)
        assert response.status_code == 200, "❌ Ошибка: статус-код не 200"
        print("✅ Статус-код корректен (200)")

        data = response.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))

        # Проверяем категорию
        joke_category = data.get("categories", [])
        assert category in joke_category, f"❌ Ошибка: категория {category} не совпадает"
        print("✅ Категория корректна")

        # Проверяем наличие слова Chuck в тексте шутки
        joke_text = data.get("value", "")
        assert "Chuck" in joke_text, "❌ Ошибка: слово 'Chuck' не найдено в шутке"
        print("✅ Проверочное слово 'Chuck' найдено")

        print("🎉 Тест успешно пройден!")

