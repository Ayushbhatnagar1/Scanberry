# Smart Fruit Health Scanner

## Project Overview

The **Smart Fruit Health Scanner** is an innovative mobile application designed to help users determine the **ripeness** and **condition** of fruits using **image processing** and **machine learning**. This project was developed to address the challenge many university students face in selecting high-quality fruits, leading to better purchasing decisions, reduced wastage, and improved health outcomes.

Our app scans fruit images and provides real-time insights on ripeness, condition (including rot detection), nutritional value, and personalized dietary recommendations. By utilizing advanced **computer vision algorithms** and **machine learning models**, the app accurately assesses various fruit features. This project helps bridge a significant gap in students’ ability to make informed fruit choices.

## Motivation

Many students struggle to identify the quality of fruits, resulting in wasted money and adverse health effects from consuming low-quality produce. This project aims to:
- Save time and money for students.
- Promote healthier eating habits.
- Provide a user-friendly interface for selecting high-quality fruits based on ripeness and condition.

## Key Features

- **Real-time Fruit Scanning**: Analyze images of fruits to detect their ripeness and condition.
- **Nutritional Information**: Offers nutritional details about different fruit varieties.
- **Personalized Recommendations**: Recommends fruit consumption based on individual dietary needs and preferences.
- **Comprehensive Fruit Database**: Includes a database of fruit varieties with attributes such as ripeness stages and nutritional value for comparison.
- **Redundancy in Quality Assessment**: Manual checks are emphasized to complement the automated assessment and provide an additional layer of accuracy.

## Approach

Our solution combines **image processing algorithms** with **machine learning** to assess key fruit features. Here's an outline of the key steps:

### 1. Model Selection
We selected a suitable machine learning architecture to best meet our project’s objectives, considering options such as **Convolutional Neural Networks (CNN)** and **Inception models**.

### 2. Training the Model
The selected model was trained on a dataset that included images of various fruits at different stages of ripeness. The model learned to identify key visual features associated with ripeness, quality, and defects.

### 3. Fine-Tuning
To improve accuracy and efficiency, we fine-tuned the model by adjusting its parameters and addressing issues like **overfitting**. This step ensured that the model performs optimally across different fruit types.

### 4. Mobile App Development
Using **Android Studio**, we developed a user-friendly mobile app interface to allow users to easily scan fruits and view the results.

## Technologies Used

- **Machine Learning Models**: CNN, Inception
- **Programming Languages**: Python, Java (for Android development)
- **Image Processing**: OpenCV, TensorFlow/Keras
- **Mobile Development**: Android Studio
- **Database**: Firebase for storing fruit attributes and user data

## Benefits

- **Enhanced User Satisfaction**: By providing accurate and reliable information, the app helps users make informed decisions about fruit purchases.
- **Healthier Eating Habits**: Encourages better nutrition by promoting the consumption of high-quality, fresh fruits.
- **Time and Cost Savings**: Reduces the time spent on fruit selection and minimizes financial losses due to poor-quality purchases.

## Future Scope

- Expanding the fruit database to include more varieties and localized options.
- Integrating AI-driven personalization features for dietary recommendations.
- Adding support for other platforms like iOS.
- Improving the app’s accuracy with additional training data and enhanced machine learning models.

## Team Members

- **Ayush Bhatnagar**
- **Utkarsh Agarwal**
- **Suhani Jain**
- **Tanushi Khandelwal**

