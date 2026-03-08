import matplotlib.pyplot as plt
import openpyxl

# Load the Excel file and access the first sheet
wb = openpyxl.load_workbook("Indonesian Skincare Dataset.xlsx")
sheet = wb['Sheet1']

# Extract 'Rating' and 'Total Reviewers' columns
ratings = []
reviewers = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    rating = row[4]
    reviewer = row[5]
    if isinstance(rating, (int, float)) and isinstance(reviewer, (int, float)):
        ratings.append(rating)
        reviewers.append(reviewer)

# Plotting the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(ratings, reviewers, alpha=0.6, color='tomato', edgecolor='black')
plt.title("Rating vs Total Reviewers")
plt.xlabel("Rating")
plt.ylabel("Total Reviewers")
plt.grid(True)
plt.tight_layout()
plt.show()
