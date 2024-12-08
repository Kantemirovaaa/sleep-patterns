# streamlit_app.py
import streamlit as st
from data_processing import (
    load_data, create_boxplot_activities, create_violinplot_sleep_duration,
    create_bar_study_time_vs_quality, create_violinplot_free_time,
    create_boxplot_caffeine_intake, create_line_physical_activity,
    create_line_screen_time, create_pairplot_study_screen,
    create_stacked_bar, create_correlation_heatmap
)

st.markdown("""
This web-interface provides results of data analysis, same with them, that we observed in Jupyter Notebook.
We can see slice of data, different visualisations and using REST API.
""")
st.markdown("# Python project - Student Sleep Patterns")

st.markdown("### Hypothesis")
st.markdown("My assumption - the quality of sleep of students depends on students' hours of study, sleep duration, physical activity and screen time")

st.markdown("### Dataset")
st.markdown("Dataset is taken from - https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns/data")

st.markdown("### Describing the main details of dataset and adding new column (Free time)")
df = load_data()

st.write(df.head(10))
st.write("Data info:")
buffer = []
buffer.append("Number of rows: {}".format(df.shape[0]))
buffer.append("Number of columns: {}".format(df.shape[1]))
st.write("\n".join(buffer))

st.write("Data types:")
st.write(df.dtypes)
st.write("Check for NaN:")
st.write(df.isna().sum())

st.markdown("### Creation of plots")

st.markdown("#### Boxplot: Distribution of Activities")
st.markdown("###### Investigation how many minutes students spend on each activity students spend."
            "It's easily to find that the smallest range is of Screen Time and the biggest - of Free Time")
fig_box = create_boxplot_activities()
st.pyplot(fig_box)

st.markdown("#### Violinplot: Sleep Duration vs Sleep Quality")
st.markdown("###### Investigation how students' sleep affects on quality of sleep. "
            "It's easily to find that there is not any serious and obvious dependence.")
fig_violin_sleep = create_violinplot_sleep_duration()
st.pyplot(fig_violin_sleep)

st.markdown("#### Bar: Study Time vs Sleep Quality")
st.markdown("###### Investigation how students' study time affects on quality of sleep. "
            "It's easily to find that there is not any serious and obvious dependence.")
fig_bar_study = create_bar_study_time_vs_quality()
st.pyplot(fig_bar_study)

st.markdown("#### Violinplot: Free Time vs Sleep Quality")
st.markdown("###### Investigation how students' free time affects on quality of sleep. "
            "It's easily to find that there is not any serious and obvious dependence.")
fig_violin_free = create_violinplot_free_time()
st.pyplot(fig_violin_free)

st.markdown("#### Boxplot: Caffeine Intake vs Sleep Quality")
st.markdown("###### Investigation how students' caffeine intake affects on quality of sleep. "
            "It's easily to find that there is not any serious and obvious dependence."
            "Also, we should notice that caffeine isn't a good parameter for observing, as it"
            "cannot be measured in time, as other factors")
fig_caffeine = create_boxplot_caffeine_intake()
st.pyplot(fig_caffeine)

st.markdown("#### Lineplot: Physical Activity vs Sleep Quality")
st.markdown("###### Investigation how students' physical activity affects on quality of sleep. "
            "It's easily to find that there is not any serious and obvious dependence.")
fig_line_phys = create_line_physical_activity()
st.pyplot(fig_line_phys)

st.markdown("#### Lineplot: Screen Time vs Sleep Quality")
st.markdown("###### Investigation how students' physical activity affects on quality of sleep. "
            "It's easily to find that there is not any serious and obvious dependence."
            "Also, in this graph I show this distribution with error")
fig_line_screen = create_line_screen_time()
st.pyplot(fig_line_screen)

st.markdown("#### Pairplot: Study_Time, Sleep_Quality, and Screen_Time")
st.markdown("###### Plot with several parameters (Study Time and Screen Time). There is, also"
            "no obvious and serious rise or decline to make any decisions about dependence")
fig_pair = create_pairplot_study_screen()
st.pyplot(fig_pair)

st.markdown("#### Stacked Bar: Influence of different parameters with Sleep Quality")
st.markdown("###### Investigation of how quality of sleep depends on different time spending,"
            " there is no such a big difference to make any decisions, to prove our hypothesis as well")
fig_stacked = create_stacked_bar()
st.pyplot(fig_stacked)

st.markdown("#### Correlation Heatmap")
st.markdown("###### A simple correlation heatmap that shows us that there is not any dependance,"
            "besides the column of Free tieme. It's obviously, as this column is created by other"
            "columns, so the less a student sleeps, the less free time one has")
fig_pair = create_pairplot_study_screen()
fig_corr = create_correlation_heatmap()
st.pyplot(fig_corr)

st.markdown("### Conclusion")
st.markdown("Our hypothesis is disproved, as there is not such a big correlation"
            " between factors and their relation to quality of sleep to make any decisions."
            " So, students' quality of sleep doesn't depend on the duration of sleep, physical "
            "activity of studentss, screen time, caffeine intake, free time and study time.")
