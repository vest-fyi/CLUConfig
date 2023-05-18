import json


def main():
    # Open the JSON file
    with open('us-symbols.json') as file:
        data = json.load(file)

    # Filter the entries to remove
    filtered_data = [entry for entry in data
                     if entry['Exchange'] == 'US'
                     or entry['Exchange'] == 'NYSE'
                     or entry['Exchange'] == 'NASDAQ'
                     or entry['Exchange'] == 'NYSE MKT'
                     ]

    # Write the filtered data back to the file
    with open('us-symbols-major-exchanges.json', 'w') as file:
        json.dump(filtered_data, file, indent=4)


if __name__ == "__main__":
    main()
