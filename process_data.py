import csv

input_files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

output_file = 'output.csv'

with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write header
    writer.writerow(['Sales', 'Date', 'Region'])

    # Process each input file
    for file in input_files:
        with open(file, 'r') as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                # Keep only Pink Morsel rows
                if row['product'].lower() == 'pink morsel':

                    # Remove $ sign and convert to number
                    price = float(row['price'].replace('$', ''))

                    # Convert quantity to integer
                    quantity = int(row['quantity'])

                    # Calculate sales
                    sales = price * quantity

                    # Write required fields
                    writer.writerow([
                        sales,
                        row['date'],
                        row['region']
                    ])

print('Processing complete!')