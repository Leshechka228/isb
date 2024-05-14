import json

def frequency_analysis(path, probabilities):
    frequencies = {}
    text_length = 0

    with open(path, 'r', encoding="utf-8") as file:
        text = file.read().replace('\n', '')
        text_length = len(text)

        for symbol in text:
            if symbol != '\n':
                if symbol in frequencies:
                    frequencies[symbol] += 1
                else:
                    frequencies[symbol] = 1

    probabilitie = {symbol: frequency / text_length for symbol, frequency in frequencies.items()}
    sorted_probabilities = {k: v for k, v in sorted(probabilitie.items(), key=lambda item: item[1], reverse=True)}  

    with open(probabilities, 'w', encoding="utf-8") as file:
        json.dump(sorted_probabilities, file, ensure_ascii=False, indent=4)