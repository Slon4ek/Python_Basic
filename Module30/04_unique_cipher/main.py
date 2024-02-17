def count_unique_characters(string: str) -> int:
    string = string.lower()
    result = list(filter(lambda x: string.count(x) == 1, string))
    print(result)
    return len(result)


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
