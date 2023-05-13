from googletrans import Translator

prime_lang = input("Enter the language you want to translate from: ")
lang = input("Enter the language you want to translate to: ")

while True:
    word = input("Enter the word or sentence you want to translate: ")
    translator = Translator()
    result = translator.translate(word, src=prime_lang, dest=lang, raise_on_failure=True)
    if result:
        print(result.text)
    else:
        print("The word could not be translated.")

    answer = input("Do you want to translate another word or change language? y/n/c: ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        lang = input("Enter the language you want to translate to: ")
        continue

print("Thank you for using our services!")