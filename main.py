import pandas as pd
import numpy as np
import os
import plotly.express as px

# Set the current directory
current_directory = os.getcwd()

# Specify the folder name for datasets
folder_name = "datasets"


# Function to read and preprocess education, demographics, and economic data
def read_and_process_data(file_name, header_rows, start_row, end_row):
    file_path = os.path.join(current_directory, folder_name, file_name)
    data = pd.read_excel(file_path, header=header_rows)
    data.columns = [
        ".".join(map(str, col)).strip() if col[1] != "" else col[0]
        for col in data.columns
    ]
    data = data.drop([0]).iloc[start_row:end_row]
    data = data.dropna(axis=1, how="all")
    data = data.replace(["−", "–", "-"], np.NaN)
    data = data.apply(pd.to_numeric, errors="ignore")
    return data


# Read and process Education Table
educ = read_and_process_data("Table-10-Education-EN.xlsx", [3, 4, 5, 6], 1, 203)

# Read and process Demographics Table
demog = read_and_process_data("Table-1-Demographics-EN-1.xlsx", [3, 4, 5], 1, 202)

# Read and process Social-Economic Stats
eco = read_and_process_data(
    "Table-12-and-15-SocProt-and-Econ-EN.xlsx", [3, 4, 5], 1, 202
)

# Read and process Region Specific data - Education
reg_educ = read_and_process_data("Table-10-Education-EN.xlsx", [3, 4, 5, 6], 205, 218)

# Read and process Region Specific data - Demographics
reg_demog = read_and_process_data("Table-1-Demographics-EN-1.xlsx", [3, 4, 5], 205, 218)

# Read and process Literacy Rates data
lr_file_name = "literacy.xls"
lr_file_path = os.path.join(current_directory, folder_name, lr_file_name)
lr = pd.read_excel(lr_file_path, sheet_name="Literacy Rates", header=[7])
lr = lr.apply(pd.to_numeric, errors="ignore")
lr = lr.fillna(method="bfill", axis=1)
lr = lr.apply(pd.to_numeric, errors="ignore")


# Rename columns to simpler terms

eco.columns = [
    "Country",
    "Mothers with Newborns Cash Benefit (%)",
    "Proportion of Children Covered by Social Protection",
    "Social Protection Benefits Distribution Bottom 40%",
    "Social Protection Benefits Distribution Top 20%",
    "Social Protection Benefits Distribution Bottom 20%",
    "Share of Household Income Bottom 40%",
    "Share of Household Income Top 20%",
    "Share of Household Income Bottom 20%",
    "Gini Coefficient",
    "Palma Index of Income Inequality",
    "GDP per Capita",
]

reg_educ.columns = [
    "Region",
    "OOSE_PrePrimary_Male",
    "OOSE_PrePrimary_Female",
    "OOSE_PrimaryEd_Male",
    "OOSE_PrimaryEd_Female",
    "OOSE_LowerSec_Male",
    "OOSE_LowerSec_Female",
    "OOSE_UpperSec_Male",
    "OOSE_UpperSec_Female",
    "Completion_Primary_Male",
    "Completion_Primary_Female",
    "Completion_LowerSec_Male",
    "Completion_LowerSec_Female",
    "Completion_UpperSec_Male",
    "Completion_UpperSec_Female",
    "LO_Grade2or3_Reading",
    "LO_Grade2or3_Math",
    "LO_EndPrimary_Reading",
    "LO_EndPrimary_Math",
    "LO_EndLowerSec_Reading",
    "LO_EndLowerSec_Math",
    "Youth_LiteracyRate_Male",
    "Youth_LiteracyRate_Female",
]

educ.columns = [
    "Country",
    "OOSE_PrePrimary_Male",
    "OOSE_PrePrimary_Female",
    "OOSE_PrimaryEd_Male",
    "OOSE_PrimaryEd_Female",
    "OOSE_LowerSec_Male",
    "OOSE_LowerSec_Female",
    "OOSE_UpperSec_Male",
    "OOSE_UpperSec_Female",
    "Completion_Primary_Male",
    "Completion_Primary_Male_1",
    "Completion_Primary_Female",
    "Completion_Primary_Female_1",
    "Completion_LowerSec_Male",
    "Completion_LowerSec_Male_1",
    "Completion_LowerSec_Female",
    "Completion_LowerSec_Female_1",
    "Completion_UpperSec_Male",
    "Completion_UpperSec_Male_1",
    "Completion_UpperSec_Female",
    "Completion_UpperSec_Female_1",
    "LO_Grade2or3_Reading",
    "LO_Grade2or3_Reading_1",
    "LO_Grade2or3_Math",
    "LO_Grade2or3_Math_1",
    "LO_EndPrimary_Reading",
    "LO_EndPrimary_Reading_1",
    "LO_EndPrimary_Math",
    "LO_EndPrimary_Math_1",
    "LO_EndLowerSec_Reading",
    "LO_EndLowerSec_Reading_1",
    "LO_EndLowerSec_Math",
    "LO_EndLowerSec_Math_1",
    "Youth_LiteracyRate_Male",
    "Youth_LiteracyRate_Female",
]

demog.columns = [
    "Country",
    "Population_total_2018",
    "Population_under_18_2018",
    "Population_under_5_2018",
    "Annual_growth_rate_2000_2018",
    "Annual_growth_rate_2018_2030",
    "Annual_births_2018",
    "Total_fertility_2018",
    "Life_expectancy_1970",
    "Life_expectancy_2000",
    "Life_expectancy_2018",
    "Dependency_ratio_total_2018",
    "Dependency_ratio_child_2018",
    "Dependency_ratio_old_age_2018",
    "Urban_population_proportion_2018",
    "Urban_population_growth_rate_2000_2018",
    "Urban_population_growth_rate_2018_2030",
    "Net_migration_rate_2015_2020",
]

reg_demog.columns = [
    "Region",
    "Population_total_2018",
    "Population_under_18_2018",
    "Population_under_5_2018",
    "Annual_growth_rate_2000_2018",
    "Annual_growth_rate_2018_2030",
    "Annual_births_2018",
    "Total_fertility_2018",
    "Life_expectancy_1970",
    "Life_expectancy_2000",
    "Life_expectancy_2018",
    "Dependency_ratio_total_2018",
    "Dependency_ratio_child_2018",
    "Dependency_ratio_old_age_2018",
    "Urban_population_proportion_2018",
    "Urban_population_growth_rate_2000_2018",
    "Urban_population_growth_rate_2018_2030",
    "Net_migration_rate_2015_2020",
]


# Create a combined Dataframe
edu_demog = pd.merge(educ, demog, on="Country", how="outer")
edu_demog_eco = pd.merge(edu_demog, eco, on="Country", how="outer")
reg_edu_demog = pd.merge(reg_educ, reg_demog, on="Region", how="outer")


##PLOTS##

# Literacy Rate by Country Over Time

df_melted = pd.melt(
    lr, id_vars="H_COUNTRY", var_name="Year", value_name="Literacy Rate"
)
df_melted.to_csv("lr_melted.csv")
fig = px.choropleth(
    df_melted,
    locations="H_COUNTRY",
    locationmode="country names",
    color="Literacy Rate",
    hover_name="H_COUNTRY",
    animation_frame="Year",
    title="Literacy Rate by Country Over Time",
    range_color=[10, 100],
    projection="natural earth",
)

fig.update_geos(projection_type="natural earth", showland=True, landcolor="white")

fig.update_layout(
    height=600,
    width=1000,
)

fig.show()


# Literacy Rate by Country - 2018


fig = px.choropleth(
    edu_demog_eco,
    locations="Country",
    locationmode="country names",
    color="Youth_LiteracyRate_Male",
    color_continuous_scale="Plasma",
    title="Literacy Rate by Country - 2018",
    range_color=[0, 100],
    projection="natural earth",
)
fig.update_layout(
    height=600,
    width=1000,
)

fig.show()
fig10 = fig


# All regions: Youth Literacy Rates by Gender


countries = reg_educ["Region"]

male_rates = reg_educ["Youth_LiteracyRate_Male"]
female_rates = reg_educ["Youth_LiteracyRate_Female"]

total_rates = male_rates + female_rates
total_rates = total_rates.sort_values().index


fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=male_rates[total_rates],
        y=countries[total_rates],
        orientation="h",
        name="Male",
        marker_color="blue",
    )
)

fig.add_trace(
    go.Bar(
        x=-female_rates[total_rates],
        y=countries[total_rates],
        orientation="h",
        name="Female",
        marker_color="pink",
    )
)

fig.update_layout(
    barmode="relative",
    title="All regions: Youth Literacy Rates by Gender",
    xaxis_title="Youth (15–24 years) literacy rate (%)",
    yaxis_title="Regions",
    bargap=0.1,
    height=600,
    width=1000,
    showlegend=True,
)

fig.show()

# Bottom 25 Countries: Youth Literacy Rates by Gender


countries = edu_demog["Country"]
male_rates = edu_demog["Youth_LiteracyRate_Male"]
female_rates = edu_demog["Youth_LiteracyRate_Female"]
total_rates = male_rates + female_rates
bottom_countries_index = total_rates.sort_values().index[:25]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=male_rates[bottom_countries_index],
        y=countries[bottom_countries_index],
        orientation="h",
        name="Male",
        marker_color="blue",
    )
)

fig.add_trace(
    go.Bar(
        x=-female_rates[bottom_countries_index],
        y=countries[bottom_countries_index],
        orientation="h",
        name="Female",
        marker_color="pink",
    )
)

fig.update_layout(
    barmode="relative",
    title="Bottom 25 Countries: Youth Literacy Rates by Gender",
    xaxis_title="Youth (15–24 years) literacy rate (%)",
    yaxis_title="Countries",
    bargap=0.1,
    height=600,
    width=1000,
    showlegend=True,
)

fig.show()

# Urban and Rural Population Proportion 2018 by Region

# New column for rural population
reg_edu_demog["Rural_population_proportion_2018"] = (
    100 - reg_edu_demog["Urban_population_proportion_2018"]
)

fig = px.bar(
    reg_edu_demog,
    x="Region",
    y=["Urban_population_proportion_2018", "Rural_population_proportion_2018"],
    title="Urban and Rural Population Proportion 2018 by Region",
    labels={"value": "Population Proportion"},
    color_discrete_map={
        "Urban_population_proportion_2018": "Gray",
        "Rural_population_proportion_2018": "Orange",
    },
)

fig.add_trace(
    px.line(
        reg_edu_demog,
        x="Region",
        y="Youth_LiteracyRate_Male",
        title="Youth Literacy Rate Male by Region",
        labels={"Youth_LiteracyRate_Male": "Literacy Rate"},
        markers=True,
    )
    .update_traces(line=dict(color="red"))
    .data[0]
)

fig.update_layout(
    yaxis=dict(title="Percentage"),
    yaxis2=dict(title="Literacy Rate", overlaying="y", side="right"),
)
fig.update_layout(height=700, width=1000)

fig.show()

# GDP per Capita and Literacy Rates

# Sort the DataFrame by 'GDP per Capita' in descending order
df_sorted = edu_demog_eco.sort_values(by="GDP per Capita", ascending=False)

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df_sorted["Country"],
        y=df_sorted["GDP per Capita"],
        name="GDP per Capita (in dollars)",
    )
)

fig.add_trace(
    go.Scatter(
        x=df_sorted["Country"],
        y=df_sorted["Youth_LiteracyRate_Male"],
        mode="lines+markers",
        name="Youth Literacy Rate (Male)",
        yaxis="y2",
        connectgaps=True,
        line=dict(color="blue"),
    )
)

fig.add_trace(
    go.Scatter(
        x=df_sorted["Country"],
        y=df_sorted["Youth_LiteracyRate_Female"],
        mode="lines+markers",
        name="Youth Literacy Rate (Female)",
        yaxis="y2",
        connectgaps=True,
        line=dict(color="magenta"),
    )
)

fig.update_layout(
    title="GDP per Capita and Literacy Rates",
    xaxis=dict(title="Country"),
    yaxis=dict(title="GDP per Capita (in USD)"),
    yaxis2=dict(title="Youth Literacy Rate", overlaying="y", side="right"),
    height=800,
    width=1400,
)
fig.update_xaxes(tickangle=45)

fig.show()

# Dependency Ratio vs. Literacy rate


ede_sorted = edu_demog_eco.sort_values(
    by="Dependency_ratio_total_2018", ascending=False
)

fig = px.line(
    ede_sorted[:25],
    x="Country",
    y=[
        "Dependency_ratio_total_2018",
        "Youth_LiteracyRate_Male",
        "Youth_LiteracyRate_Female",
    ],
    labels={"value": "Percentage", "variable": "Category"},
    title="Dependency Ratio vs. Literacy rate",
    markers=True,
)
fig.update_layout(height=600, width=1000)
fig.update_traces(connectgaps=True, line_shape="linear")

fig.update_traces(
    line=dict(color="red"), selector=dict(name="Dependency_ratio_total_2018")
)
fig.update_traces(
    line=dict(color="blue"), selector=dict(name="Youth_LiteracyRate_Male")
)
fig.update_traces(
    line=dict(color="magenta"), selector=dict(name="Youth_LiteracyRate_Female")
)

fig.update_xaxes(tickangle=45)
fig.show()

# Out-of-School Education by Region

fig = px.bar(
    reg_educ,
    x="Region",
    y=[
        "OOSE_PrePrimary_Male",
        "OOSE_PrePrimary_Female",
        "OOSE_PrimaryEd_Male",
        "OOSE_PrimaryEd_Female",
        "OOSE_LowerSec_Male",
        "OOSE_LowerSec_Female",
        "OOSE_UpperSec_Male",
        "OOSE_UpperSec_Female",
    ],
    title="Out-of-School Education by Region",
    labels={"value": "Percentage", "variable": "Education Level"},
)
fig.update_layout(height=600, width=1000)
fig.show()


# Box Plot for OOSE Columns

oose_cols = [col for col in edu_demog_eco.columns if "OOSE" in col]

melted_df = pd.melt(
    edu_demog_eco,
    id_vars=["Country"],
    value_vars=oose_cols,
    var_name="OOSE_Category",
    value_name="Value",
)

fig = px.box(
    melted_df,
    x="OOSE_Category",
    y="Value",
    points="all",
    color="OOSE_Category",
    title="Box Plot for OOSE Columns",
    hover_data=["Country"],
)
fig.update_xaxes(
    tickangle=45,
    tickmode="array",
    tickvals=list(range(len(oose_cols))),
    ticktext=oose_cols,
)

fig.update_layout(height=800, width=1000)
fig.update_layout(showlegend=False)

fig.show()

# Male and Female Out of School Levels

# Select the columns for the male and female line graphs
male_columns = [
    "OOSE_PrePrimary_Male",
    "OOSE_PrimaryEd_Male",
    "OOSE_LowerSec_Male",
    "OOSE_UpperSec_Male",
]
female_columns = [
    "OOSE_PrePrimary_Female",
    "OOSE_PrimaryEd_Female",
    "OOSE_LowerSec_Female",
    "OOSE_UpperSec_Female",
]

male_plot_data = reg_educ[["Region"] + male_columns]
male_plot_data = male_plot_data.melt(
    id_vars=["Region"], var_name="Education_Level", value_name="Value", col_level=0
)

male_fig = px.line(
    male_plot_data,
    x="Education_Level",
    y="Value",
    color="Region",
    line_group="Region",
    markers=True,
    line_dash="Region",
    labels={"Value": "Percentage", "Education_Level": "Education Level"},
    title="Male Out of School Levels",
)
male_fig.update_layout(height=600, width=1000)

male_fig.show()

female_plot_data = reg_educ[["Region"] + female_columns]
female_plot_data = female_plot_data.melt(
    id_vars=["Region"], var_name="Education_Level", value_name="Value", col_level=0
)

female_fig = px.line(
    female_plot_data,
    x="Education_Level",
    y="Value",
    color="Region",
    line_group="Region",
    markers=True,
    line_dash="Region",
    labels={"Value": "Percentage", "Education_Level": "Education Level"},
    title="Female Out of School Levels",
)
female_fig.update_layout(height=600, width=1000)

female_fig.show()

# Scatter Plot of OOS Upper Secondary Rate vs GDP by Gender

fig = px.scatter(
    edu_demog_eco,
    y="GDP per Capita",
    x=["OOSE_UpperSec_Male", "OOSE_UpperSec_Female"],
    labels={"value": "Out-of-School Upper Secondary Rate"},
    color_discrete_sequence=["blue", "magenta"],
    hover_name="Country",
    title="Scatter Plot of OOS Upper Secondary Rate vs GDP by Gender",
)
fig.update_layout(
    yaxis_title="GDP per Capita (USD)",
    xaxis_title="Out-of-School Upper Secondary Rate",
    autosize=False,
    width=800,
    height=600,
)
fig.show()

# Completion Rates by Region

fig = px.bar(
    reg_educ,
    x="Region",
    y=[
        "Completion_Primary_Male",
        "Completion_Primary_Female",
        "Completion_LowerSec_Male",
        "Completion_LowerSec_Female",
        "Completion_UpperSec_Male",
        "Completion_UpperSec_Female",
    ],
    title="Completion Rates by Region",
    labels={"value": "Percentage", "variable": "Education Level"},
)
fig.update_layout(height=600, width=1000)
fig.show()

# Male-Female Completion Rates

# Select the columns for the male and female lines
male_columns_completion = [
    "Completion_Primary_Male",
    "Completion_LowerSec_Male",
    "Completion_UpperSec_Male",
]
female_columns_completion = [
    "Completion_Primary_Female",
    "Completion_LowerSec_Female",
    "Completion_UpperSec_Female",
]

male_plot_data_completion = reg_educ[["Region"] + male_columns_completion]
male_plot_data_completion = male_plot_data_completion.melt(
    id_vars=["Region"], var_name="Education_Level", value_name="Value", col_level=0
)

male_fig_completion = px.line(
    male_plot_data_completion,
    x="Education_Level",
    y="Value",
    color="Region",
    line_group="Region",
    markers=True,
    line_dash="Region",
    labels={"Value": "Percentage", "Education_Level": "Education Level"},
    title="Male Completion Rates",
)
male_fig_completion.update_layout(height=600, width=1000)

male_fig_completion.show()

female_plot_data_completion = reg_educ[["Region"] + female_columns_completion]
female_plot_data_completion = female_plot_data_completion.melt(
    id_vars=["Region"], var_name="Education_Level", value_name="Value", col_level=0
)

female_fig_completion = px.line(
    female_plot_data_completion,
    x="Education_Level",
    y="Value",
    color="Region",
    line_group="Region",
    markers=True,
    line_dash="Region",
    labels={"Value": "Percentage", "Education_Level": "Education Level"},
    title="Female Completion Rates",
)
female_fig_completion.update_layout(height=600, width=1000)

female_fig_completion.show()
