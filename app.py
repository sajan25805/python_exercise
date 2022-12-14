import csv

# Where final data will be stored.
final_data = []

def parse_csv(file):
    # Parses CSV file
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
parsed_data = parse_csv("sample.csv")


for item in parsed_data:
    if float(item["Math"]) < 50 and float(item["Science"]) < 50:
        final_data.append(item)

# Write the final_data into demofile3.csv
f = open("finalfile.csv", "w")
f.write("List of Failed Students in Both Subject \n")
f.write(str(final_data))


#open and read the file after the appending:
f = open("finalfile.csv", "r")
print("The List of Failed Students in both Science and Math \n ",f.read())


        
    

    
