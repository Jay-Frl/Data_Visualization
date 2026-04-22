import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv(r"C:\Users\lab.AUKOL\Downloads\company_dataset (1) (1).csv")
print(df.head())

# ── Clean employees column ─────────────────────────────────
df['employees_clean'] = (
    df['employees']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+)')
    .astype(float)
)

# -------------------------------
# 0. TOP 10 COMPANIES - Visual Table
# -------------------------------
top10 = df.nlargest(10, 'employees_clean')[['name', 'employees', 'ratings', 'review_count', 'hq', 'years']]
top10 = top10.reset_index(drop=True)
top10.index += 1  # start rank from 1

fig_table = go.Figure(data=[go.Table(
    columnwidth=[40, 160, 100, 80, 100, 160, 80],
    header=dict(
        values=['<b>Rank</b>', '<b>Company</b>', '<b>Employees</b>',
                '<b>Rating</b>', '<b>Reviews</b>', '<b>HQ</b>', '<b>Year</b>'],
        fill_color='#4f46e5',
        font=dict(color='white', size=13),
        align='center',
        height=40,
        line_color='#3730a3',
    ),
    cells=dict(
        values=[
            list(top10.index),
            top10['name'].tolist(),
            top10['employees'].tolist(),
            top10['ratings'].tolist(),
            top10['review_count'].tolist(),
            top10['hq'].tolist(),
            top10['years'].tolist(),
        ],
        fill_color=[
            ['#1e1b4b' if i % 2 == 0 else '#2e2a5e' for i in range(10)],
        ],
        font=dict(color='white', size=12),
        align='center',
        height=35,
        line_color='#3730a3',
    )
)])

fig_table.update_layout(
    title=dict(
        text="🏆  Top 10 Companies by Employee Count",
        font=dict(size=18, color='white'),
        x=0.5,
    ),
    paper_bgcolor='#0f0e1a',
    margin=dict(l=20, r=20, t=60, b=20),
    height=450,
)
fig_table.show()

# -------------------------------
# 1. PIE CHART - Top 5 Companies Employee-wise
# -------------------------------
top5_emp = df.nlargest(5, 'employees_clean')[['name', 'employees', 'employees_clean']]

plt.figure(figsize=(8,8))
plt.pie(top5_emp['employees_clean'],
        labels=top5_emp['name'],
        autopct='%1.1f%%',
        startangle=140)
plt.title("Top 5 Companies by Employee Count")
plt.show()

# -------------------------------
# 2. FUNNEL CHART - Review-wise
# -------------------------------
df_sorted_reviews = df.sort_values(by='review_count', ascending=False)

fig = px.funnel(df_sorted_reviews,
                x='review_count',
                y='name',
                title="Funnel Chart of Companies by Review Count")
fig.update_traces(textinfo='value+percent initial')
fig.show()

# -------------------------------
# 3. TOP 10 HEADQUARTERS
# -------------------------------
top_hq = df['hq'].value_counts().head(10)
print("\nTop 10 Headquarters Locations:\n", top_hq)

top_hq_locations = top_hq.index.tolist()
for loc in top_hq_locations:
    companies = df[df['hq'] == loc]['name'].tolist()
    print(f"\n{loc}: {', '.join(companies)}")

# -------------------------------
# 4. BAR CHART - Year-wise
# -------------------------------
year_counts = df['years'].value_counts().sort_index().reset_index()
year_counts.columns = ['year', 'count']

year_companies = df.groupby('years')['name'].apply(lambda x: '<br>'.join(x)).reset_index()
year_companies.columns = ['year', 'companies']
year_counts = year_counts.merge(year_companies, on='year')

fig_bar = px.bar(year_counts,
                 x='year',
                 y='count',
                 title="Number of Companies by Year",
                 labels={'year': 'Year', 'count': 'Number of Companies'},
                 hover_data={'companies': True, 'count': True},
                 text='count')
fig_bar.update_traces(textposition='outside')
fig_bar.update_layout(xaxis_tickangle=-45)
fig_bar.show()

# -------------------------------
# 5. LINE CHART - Rating-wise
# -------------------------------
df_sorted_rating = df.sort_values(by='ratings')

fig_line = px.line(df_sorted_rating,
                   x='name',
                   y='ratings',
                   title="Company Ratings (Rating-wise)",
                   labels={'name': 'Company Name', 'ratings': 'Rating'},
                   markers=True,
                   hover_data={'name': True, 'ratings': True})
fig_line.update_layout(xaxis_tickangle=-90,
                       xaxis_tickfont=dict(size=9))
fig_line.show()