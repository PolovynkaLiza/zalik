def find_paragraphs_with_word(file_path, search_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            paragraphs = file.read().split('\n\n')
            found_paragraphs = []

            for paragraph in paragraphs:
                if search_word.lower() in paragraph.lower():
                    found_paragraphs.append(paragraph)

            if found_paragraphs:
                print(f"Знайдено {len(found_paragraphs)} абзаци, які містять слово '{search_word}':")
                for idx, found_paragraph in enumerate(found_paragraphs, 1):
                    print(f"\nАбзац {idx}:\n{found_paragraph}")
            else:
                print(f"Слово '{search_word}' не знайдено в жодному абзаці.")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")

file_path = input("Введіть шлях до текстового файлу: ")
search_word = input("Введіть слово для пошуку: ")

find_paragraphs_with_word(file_path, search_word)
