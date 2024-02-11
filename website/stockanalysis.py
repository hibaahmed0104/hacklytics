import csv

csv_filename = '/Users/meghanamukkoti/Desktop/hacklytics/Stoquette/website/stock_data.csv'
output_csv_filename = '/Users/meghanamukkoti/Desktop/hacklytics/Stoquette/website/output_stock_data.csv'
listName = ["AMZN", "ANTM", "BAC", "C", "CMS", "CVS", "DUK", "FIS", "GM", "PGR", "HSY", "VRTX"]

try:
    with open(csv_filename, mode='r') as csvfile, open(output_csv_filename, mode='w', newline='') as output_csv:
        reader = csv.reader(csvfile)
        writer = csv.writer(output_csv)

        for row in reader:
            # Check if the first element is in the listName
            if row[0] in listName:
                value = row[4]
                writer.writerow([value])

except FileNotFoundError:
    print(f"File '{csv_filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")