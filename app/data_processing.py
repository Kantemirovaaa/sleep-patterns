import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    df = pd.read_csv("./data/student_sleep_patterns.csv")

    try:
        df['Study_Hours'] = df['Study_Hours'] * 60

        cols_to_drop = ['Weekday_Sleep_Start', 'Weekday_Sleep_End',
                        'Weekend_Sleep_Start',
                        'Weekend_Sleep_End', 'Age', 'Gender',
                        'University_Year']
        df = df.drop(columns=cols_to_drop, errors='ignore')
        df['Screen_Time'] = df['Screen_Time'] * 60

        df['Sleep_Duration'] = df['Sleep_Duration'] * 60
        df = df.rename(columns={'Study_Hours': 'Study_Time'})

        df['Free_Time'] = (24 * 60) - (
                df['Physical_Activity'] + df['Screen_Time'] +
                df['Sleep_Duration'] + df['Study_Time'])

        df = df[df['Free_Time'] >= 0]
    except KeyError:
        pass

    return df


def get_data_slice(start: int, limit: int):
    df = load_data()
    data_slice = df.iloc[start:start + limit]
    return data_slice.to_dict(orient="records")


def add_record(record: dict):
    df = load_data()
    new_df = pd.DataFrame([record])

    updated_df = pd.concat([df, new_df], ignore_index=True)

    updated_df.to_csv("./data/student_sleep_patterns.csv", index=False)

    return record


def create_sleep_duration_hist():
    df = load_data()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Sleep_Duration'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Distribution of Sleep Duration')
    ax.set_xlabel('Sleep Duration (minutes)')
    ax.set_ylabel('Count')

    return fig


def create_correlation_heatmap():
    df = load_data()
    corr = df[
        ['Sleep_Duration', 'Study_Time', 'Screen_Time', 'Caffeine_Intake',
         'Physical_Activity', 'Sleep_Quality', 'Free_Time']].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    cax = ax.matshow(corr, cmap='coolwarm')
    fig.colorbar(cax)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha='left')
    ax.set_yticklabels(corr.columns)
    ax.set_title('Correlation Heatmap', pad=20)
    return fig


def create_plot(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Screen_Time'], df['Sleep_Quality'], c='blue', alpha=0.5)
    ax.set_title('Screen Time vs Sleep Quality')
    ax.set_xlabel('Screen Time (min)')
    ax.set_ylabel('Sleep Quality')
    return fig


def create_boxplot_activities():
    df = load_data()
    fig, ax = plt.subplots(figsize=(20, 5))
    sns.boxplot(
        data=df[["Sleep_Duration", "Study_Time", "Screen_Time", "Free_Time"]],
        ax=ax)
    ax.set_title('Distribution of Activities (Boxplot)')
    return fig


def create_violinplot_sleep_duration():
    df = load_data()
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.violinplot(data=df, x="Sleep_Duration", hue="Sleep_Quality",
                   palette="pastel", ax=ax)
    ax.set_title('Sleep Duration Distribution by Quality (Violin Plot)')
    return fig


def create_bar_study_time_vs_quality():
    df = load_data()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['Sleep_Quality'], df['Study_Time'], color='skyblue')
    ax.set_title('Study Time vs Sleep Quality')
    ax.set_xlabel('Sleep Quality')
    ax.set_ylabel('Study Time (min)')
    return fig


def create_violinplot_free_time():
    df = load_data()
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.violinplot(data=df, x="Free_Time", hue="Sleep_Quality",
                   palette="pastel", ax=ax)
    ax.set_title('Free Time Distribution by Sleep Quality (Violin Plot)')
    return fig


def create_boxplot_caffeine_intake():
    df = load_data()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Caffeine_Intake', y='Sleep_Quality', data=df, ax=ax)
    ax.set_title('Caffeine Intake vs Sleep Quality (Boxplot)')
    ax.set_xlabel('Caffeine Intake')
    ax.set_ylabel('Sleep Quality')
    ax.grid(True)
    return fig


def create_line_physical_activity():
    df = load_data()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Physical_Activity', y='Sleep_Quality', data=df, marker='o',
                 color='blue', errorbar=None, ax=ax)
    ax.set_title('Physical Activity vs Sleep Quality')
    ax.set_xlabel('Physical Activity')
    ax.set_ylabel('Sleep Quality')
    ax.grid(True)
    return fig


def create_line_screen_time():
    df = load_data()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Screen_Time', y='Sleep_Quality', data=df, marker='o',
                 color='blue', ax=ax)
    ax.set_title('Screen Time vs Sleep Quality')
    ax.set_xlabel('Screen Time (min)')
    ax.set_ylabel('Sleep Quality')
    ax.grid(True)
    return fig


def create_pairplot_study_screen():
    df = load_data()
    g = sns.pairplot(df[['Study_Time', 'Sleep_Quality', 'Screen_Time']],
                     hue="Sleep_Quality", palette="pastel")
    return g.fig


def create_stacked_bar():
    df = load_data()
    grouped = df[
        ['Sleep_Quality', 'Sleep_Duration', 'Study_Time', 'Screen_Time',
         'Free_Time']].groupby('Sleep_Quality').mean()
    fig, ax = plt.subplots(figsize=(12, 8))
    grouped.plot(kind='barh', stacked=True, alpha=0.9, colormap='Set3', ax=ax)
    ax.set_title('Influence of different parameters on Sleep Quality')
    ax.set_xlabel('Mean Values of parameters')
    ax.set_ylabel('Sleep Quality')
    ax.grid(axis='x', linestyle='-', alpha=0.6)
    plt.tight_layout()
    return fig
