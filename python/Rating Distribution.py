import matplotlib.pyplot as plt
import openpyxl

# Load Excel data
wb = openpyxl.load_workbook("Indonesian Skincare Dataset.xlsx")
sheet = wb['Sheet1']

# Extract columns into lists
ratings = []
reviewers = []
names = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    ratings.append(row[4])
    reviewers.append(row[5])
    names.append(row[1])

# Plot Rating Distribution 
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(ratings, bins=10, color='skyblue', edgecolor='black')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
