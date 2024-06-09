import csv

# Define the filename
input_file = 'sample.csv'
output_file = 'output.csv'

# Open the CSV file
file = open(input_file, mode='r', newline='')
# Create a DictReader object
csv_reader = csv.DictReader(file)
# Create a list to hold the dictionaries
data = []

for row in csv_reader:
    data.append(row)

# Check for Duplicate Names
def duplicate_check(check):
    name = check["first_name"]
    for j in range(i+1, len(data)):
        checking = data[j]
        if name == checking["first_name"]:
            return False
    return True

# Check for Empty Numbers
def number_check(check):
    number = check["phone"]
    if number == "":
        return False
    return True

# Input for Blank Email Entries
def email_enter(check):
    name = check["first_name"]
    print(f"{name} have no email ID.")
    email = input("Enter Email:")
    return email

headers = data[0].keys()
# Open the CSV file for writing
out_file = open(output_file, mode='w', newline='')
# Create a DictWriter object
writer = csv.DictWriter(out_file, fieldnames=headers)

# Write the header
writer.writeheader()
for i in range(len(data)):
    to_check = data[i]
    if to_check["email"] == "":
        to_check["email"] = email_enter(to_check)
    if  duplicate_check(to_check) and number_check(to_check):
        writer.writerow(data[i])

print("Completed!")
