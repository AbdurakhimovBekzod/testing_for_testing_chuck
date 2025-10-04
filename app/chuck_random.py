import json
import requests
class Test_new_joke():
    """Creating new joke"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        print(url)

        result = requests.get(url)
        # print(f'STATUS CODE: {result.status_code}')
        # print(f'JSON BODY: {result.json()}')
        # print(f'HEADERS: {result.headers}')
        # print('-------------------------')
        assert result.status_code == 200

        if result.status_code == 200:
            print('Everything is ok 200')
        else:
            print('Error request!')
        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        print(json.dumps(check, indent=4, ensure_ascii=False) + '\n ---------------------------')
        #
        # check_info = check.get("value")
        # print(check_info)

        check_info_value = check.get("value")
        if "Chuck" in check_info_value:
            print('Chuck ismi mavjud responseda!')
        else:
            print('Chuck ismi response da mavjud emas!')


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()
