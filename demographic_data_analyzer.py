import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        df["education"].value_counts(normalize=True).mul(100).loc["Bachelors"], 1
    )

    # 4 & 5. Advanced edu and % rich
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round(
        df[higher_education]["salary"]
        .value_counts(normalize=True)
        .mul(100)
        .loc[">50K"],
        1,
    )
    lower_education_rich = round(
        df[~higher_education]["salary"]
        .value_counts(normalize=True)
        .mul(100)
        .loc[">50K"],
        1,
    )

    # 6. Min work hours
    min_work_hours = df["hours-per-week"].min()

    # 7. Rich % among min-hour workers
    rich_percentage = round(
        df[df["hours-per-week"] == min_work_hours]["salary"]
        .value_counts(normalize=True)
        .mul(100)
        .loc[">50K"],
        1,
    )

    # 8. Country with highest % rich
    country_ratio = (
        df[df["salary"] == ">50K"]["native-country"].value_counts()
        / df["native-country"].value_counts()
    )
    highest_earning_country = country_ratio.idxmax()
    highest_earning_country_percentage = round(country_ratio.max() * 100, 1)

    # 9. Top occupation in India for >50K earners
    top_IN_occupation = df[
        (df["native-country"] == "India") & (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Return results
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
