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

# Plot Total Reviewers Distribution 
plt.subplot(1, 3, 2)
plt.hist(reviewers, bins=20, color='coral', edgecolor='black')
plt.title("Total Reviewers Distribution")
plt.xlabel("Number of Reviewers")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
