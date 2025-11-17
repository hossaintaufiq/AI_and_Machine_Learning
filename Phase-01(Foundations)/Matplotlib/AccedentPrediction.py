import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # modern clean look
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

df = pd.read_csv(
    r"D:\AI & Machine learning\Phase-01(Foundations)\Matplotlib\AccidentPredictionIndianData.csv"
)

# Convert time to hour
df['Hour'] = pd.to_datetime(df['Time of Day'], errors='coerce').dt.hour


# ==========================
# 1️⃣ Yearly Accident Count
# ==========================
plt.figure(figsize=(12, 6))
year_counts = df['Year'].value_counts().sort_index()
bars = plt.bar(year_counts.index, year_counts.values, width=0.6)

plt.title("📅 Accidents Per Year (Trend Overview)", fontsize=16, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Number of Accidents")

# Annotate values
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=11)

plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# =====================================
# 2️⃣ Accident Severity Distribution
# =====================================
# import matplotlib.pyplot as plt

severity_counts = df['Accident Severity'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(
    severity_counts.values,
    labels=severity_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.title("Accident Severity Distribution (Pie Chart)", fontsize=16, fontweight='bold')
plt.show()



# ==============================
# 3️⃣ Time of Day (Histogram)
# ==============================
plt.figure(figsize=(12, 6))
plt.hist(df['Hour'].dropna(), bins=24, edgecolor='black')

plt.title("⏰ Accident Frequency by Hour of the Day", fontsize=16, fontweight='bold')
plt.xlabel("Hour (0–23)")
plt.ylabel("Number of Accidents")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# ======================================
# 4️⃣ Accidents by Vehicle Type
# ======================================
vehicle_counts = df['Vehicle Type Involved'].value_counts()

plt.figure(figsize=(9,9))
plt.pie(
    vehicle_counts.values,
    labels=vehicle_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops={'edgecolor': 'black'}
)

# Donut style effect
centre_circle = plt.Circle((0,0),0.50,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Vehicle Type Distribution (Donut Chart)", fontsize=16, fontweight='bold')
plt.show()



# ==================================
# 5️⃣ Accidents by Road Type
# ==================================
plt.figure(figsize=(14, 6))
road_counts = df['Road Type'].value_counts()
bars = plt.bar(road_counts.index, road_counts.values)

plt.title("🛣️ Accidents by Road Type", fontsize=16, fontweight='bold')
plt.xlabel("Road Type")
plt.ylabel("Accident Count")
plt.xticks(rotation=45)

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{int(bar.get_height())}', ha='center', va='bottom')

plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
