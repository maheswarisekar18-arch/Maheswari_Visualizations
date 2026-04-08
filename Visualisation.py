import pandas as pd
import matplotlib.pyplot as plt
import os

# Task 1 — Setup
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create folder not exist
os.makedirs("outputs", exist_ok=True)

# chart 1
top10 = df.nlargest(10, "score").copy()
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(8,6))
plt.barh(top10["short_title"], top10["score"], color="skyblue")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# chart 2
category_counts = df["category"].value_counts()

plt.figure(figsize=(8,6))
category_counts.plot(kind="bar", color=plt.cm.tab20.colors)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Task 4 — Chart 3: Score vs Comments
plt.figure(figsize=(8,6))
colors = df["is_popular"].map({True:"green", False:"red"})
plt.scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend(handles=[
    plt.Line2D([0],[0], marker="o", color="w", label="Popular", markerfacecolor="green", markersize=8),
    plt.Line2D([0],[0], marker="o", color="w", label="Not Popular", markerfacecolor="red", markersize=8)
])
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

#Dashboard
fig, axes = plt.subplots(1, 3, figsize=(18,6))

# Chart 1 in dashboard
axes[0].barh(top10["short_title"], top10["score"], color="skyblue")
axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values, color=plt.cm.tab20.colors)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

# Chart 3 in dashboard
colors = df["is_popular"].map({True:"green", False:"red"})
axes[2].scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")

fig.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()
