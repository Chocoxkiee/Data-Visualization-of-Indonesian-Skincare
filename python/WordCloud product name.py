import matplotlib.pyplot as plt
from wordcloud import WordCloud
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

# WordCloud for Product Names 
plt.subplot(1, 3, 3)
combined_text = " ".join(name for name in names if isinstance(name, str))
wordcloud = WordCloud(width=600, height=400, background_color='white').generate(combined_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Common Words in Product Names")

plt.tight_layout()
plt.show()
