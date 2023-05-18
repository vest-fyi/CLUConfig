import json


def main():
    with open('StockResearch-2023-05-18.json', 'r') as file:
        clu_config = json.load(file)
    with open('us-symbols-major-exchanges.json', 'r') as file:
        stocks = json.load(file)

    # Create a list to hold all the new utterance objects
    new_utterances = []

    dedupe_set = set()

    for item in stocks:
        code = item['Code']
        name = item['Name']

        # Skip if the code or name is already in the dedupe set
        if code in dedupe_set:
            continue
        dedupe_set.add(code)

        code_length = len(code)
        name_length = len(name)

        # Create new utterance objects for code and name
        code_utterance = {
            'text': f'get market cap for {code}',
            'language': 'en-us',
            'intent': 'GetFundamental',
            'entities': [
                {
                    'category': 'fundamentalType',
                    'offset': 4,
                    'length': 10
                },
                {
                    'category': 'Stock',
                    'offset': 19,
                    'length': code_length
                }
            ],
            'dataset': 'Train'
        }


        # prevent duplicate utterances
        if code == name:
            new_utterances.append(code_utterance)
            continue

        if name in dedupe_set:
            continue
        dedupe_set.add(name)

        name_utterance = {
            'text': f'get market cap for {name}',
            'language': 'en-us',
            'intent': 'GetFundamental',
            'entities': [
                {
                    'category': 'fundamentalType',
                    'offset': 4,
                    'length': 10
                },
                {
                    'category': 'Stock',
                    'offset': 19,
                    'length': name_length
                }
            ],
            'dataset': 'Train'
        }

        # Append the new utterance objects to the list
        new_utterances.extend([code_utterance, name_utterance])

    # Append the new utterance objects to the existing ones in file A
    clu_config['assets']['utterances'].extend(new_utterances)

    # Save the modified file A
    with open('StockResearch-major-exchanges.json', 'w') as file:
        json.dump(clu_config, file, indent=4)


if __name__ == "__main__":
    main()
