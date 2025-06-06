import csv

filename = "people.csv"

fields = ['Slno', 'Name', 'Gender', 'Qualification', 'Email ID', 'Mobile Number']

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
  
    writer.writerow(fields)

    n = int(input("Enter the number of people to record: "))

    for i in range(n):
        print(f"\nEnter details for person {i+1}:")
        slno = input("Slno: ")
        name = input("Name: ")
        gender = input("Gender: ")
        qualification = input("Qualification: ")
        email = input("Email ID: ")
        mobile = input("Mobile Number: ")
      
        writer.writerow([slno, name, gender, qualification, email, mobile])

print("\nData has been written to 'people.csv'.")
