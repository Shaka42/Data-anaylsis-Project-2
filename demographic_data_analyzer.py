from codecs import ignore_errors
import pandas as pd
import numpy as np



def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv',sep=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().to_list()

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =round(((df[df['education']=='Bachelors']['education'].count())/df.value_counts().sum())*100,1) 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(((df[(df.education.isin(['Bachelors','Masters','Doctorate',]))& (df.salary=='>50K')].value_counts().sum())/df.value_counts().sum())*100,1)
    lower_education = round(((df[(df.education.isin(['11th','9th','Some-college','Assoc-acdm','Assoc-voc','7th-8th','Prof-school','5th-6th','10th','1st-4th','Preschool','12th','HS-grad']))& (df.salary=='>50K')].value_counts().sum())/df.value_counts().sum())*100,1)

    # percentage with salary >50K
    higher_education_rich = round(((df[(df.education.isin(['Bachelors','Masters','Doctorate',]))& (df.salary=='>50K')].value_counts().sum())/df[df.education.isin(['Bachelors','Masters','Doctorate',])].value_counts().sum())*100,1)
    lower_education_rich = round(((df[(df.education.isin(['11th','9th','Some-college','Assoc-acdm','Assoc-voc','7th-8th','Prof-school','5th-6th','10th','1st-4th','Preschool','12th','HS-grad']))& (df.salary=='>50K')].value_counts().sum())/df[df.education.isin(['11th','9th','Some-college','Assoc-acdm','Assoc-voc','7th-8th','Prof-school','5th-6th','10th','1st-4th','Preschool','12th','HS-grad'])].value_counts().sum())*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week']==df['hours-per-week'].min())].value_counts().sum()

    rich_percentage = round((df[(df['hours-per-week']==df['hours-per-week'].min())&(df['salary']=='>50K')].value_counts().sum()/num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    a = df['native-country'].value_counts()
    a=pd.DataFrame(a)
    n=df[df['salary']=='>50K']
    t=n['native-country'].value_counts()
    a=a.drop('native-country',axis=1,errors ='ignore')
    j=pd.DataFrame(t)
    a['>50K']=j['native-country']
    f=df[df['salary']=='<=50K']
    l=f['native-country'].value_counts()
    m=pd.DataFrame(l)
    a['<=50K']=m['native-country']
    a['Rich_Percentage']=(a['>50K']/(a['<=50K']+a['>50K']))*100
    b=a['Rich_Percentage']
    highest_earning_country = b.idxmax()
    highest_earning_country_percentage = round(b.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[df.salary.isin(['>50K'])&(df['native-country'].isin(['India']))][['occupation','native-country','salary']].occupation.value_counts().idxmax()

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
