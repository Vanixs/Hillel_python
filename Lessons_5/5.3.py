import string

while True:
    user_input = input("Введіть рядок для хештегу: ")

    words = user_input.split()
    hashtag = "#"

    for word in words:
        clean_word = ""
        for char in word:
            if char not in string.punctuation:
                clean_word += char

        if clean_word:
            hashtag += clean_word.capitalize()

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    print(hashtag)

    user_choice = input("Бажаєте створити ще один хештег? (y/yes): ").lower()
    if user_choice != 'y' and user_choice != 'yes':
        print("Програма завершена.")
        break