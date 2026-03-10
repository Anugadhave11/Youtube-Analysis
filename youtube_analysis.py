# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/youtube_data.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(data.head())

# Check dataset information
print("\nDataset Info:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Top 10 videos by views
top_videos = data.sort_values(by="views", ascending=False).head(10)
print("\nTop 10 Videos by Views:")
print(top_videos[['title','views']])

# Top channels by total views
channel_views = data.groupby("channel_title")["views"].sum().sort_values(ascending=False).head(10)

print("\nTop Channels by Views:")
print(channel_views)

# Visualization - Top channels
plt.figure(figsize=(10,5))
sns.barplot(x=channel_views.values, y=channel_views.index)
plt.title("Top Channels by Views")
plt.xlabel("Views")
plt.ylabel("Channel")
plt.show()

# Visualization - Likes vs Views
plt.figure(figsize=(8,5))
sns.scatterplot(x=data["views"], y=data["likes"])
plt.title("Views vs Likes Relationship")
plt.show()