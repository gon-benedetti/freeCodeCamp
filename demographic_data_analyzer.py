import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_counts = df['race'].value_counts()
    race_count = pd.Series(race_counts.values, index=race_counts.index)

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].value_counts().sum()/df.value_counts().sum()*100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bachelors = df[df['education'] == 'Bachelors'].value_counts().sum()
    masters = df[df['education'] == 'Masters'].value_counts().sum()
    doctorate = df[df['education'] == 'Doctorate'].value_counts().sum()
    higher_education = bachelors + masters + doctorate
    lower_education = df.value_counts().sum() - higher_education

    # percentage with salary >50K
    rich_bc = df[df['salary'] == '>50K'][df['education'] == 'Bachelors'].value_counts().sum()
    rich_m = df[df['salary'] == '>50K'][df['education'] == 'Masters'].value_counts().sum()
    rich_phd = df[df['salary'] == '>50K'][df['education'] == 'Doctorate'].value_counts().sum()
    rich_higher_education = rich_bc + rich_m + rich_phd
    higher_education_rich = round(rich_higher_education/higher_education*100,1)

    education_levels = ['Bachelors', 'Masters', 'Doctorate']
    filtered_df = df[~df['education'].isin(education_levels)]
    rich_lower_education = filtered_df[filtered_df['salary'] == '>50K'].value_counts().sum()
    lower_education_rich = round(rich_lower_education/lower_education*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df['hours-per-week'].min()
    min_hours_workers = df[df['hours-per-week'] == min_work_hours].value_counts().sum()
    rich_min = df[df['salary'] == '>50K'][df['hours-per-week'] == min_work_hours].value_counts().sum()

    rich_percentage = round(rich_min/min_hours_workers*100,1)

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage = (rich_per_country / country_counts * 100).sort_values(ascending=False)
    highest_earning_country = percentage.index[0]
    iran_data = df[df['native-country'] == 'Iran']
    total_iran_rows = len(iran_data)
    rich_iran_rows = len(iran_data[iran_data['salary'] == '>50K'])
    highest_earning_country_percentage = round((rich_iran_rows / total_iran_rows) * 100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupation_counts = india_rich['occupation'].value_counts()
    top_IN_occupation = occupation_counts.index[0]

    # DO NOT MODIFY BELOW THIS LINE

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

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
