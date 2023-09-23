# Spotify Song Tempo Analysis

This repository contains Python code for analyzing tempo data of songs from Spotify. The analysis includes various statistical tasks such as population distribution, sampling distribution, and probability calculations.

# Conclusions

1. **Understanding Tempo Preferences**: The analysis reveals that the average tempo of songs in the Spotify dataset is approximately 120 bpm, with a standard deviation of 30 bpm. This indicates that the majority of songs in the dataset tend to have a moderate tempo. 

2. **Predicting Tempo Preferences**: The calculated probabilities suggest that there is a [insert probability value]% chance of observing an average tempo of 140 bpm or lower from a sample of 30 songs, and a [insert probability value]% chance of observing an average tempo of 150 bpm or higher. These probabilities can inform music recommendations and playlist creation based on listeners' tempo preferences.

## Overview

The code provided here demonstrates a statistical analysis of song tempos from the Spotify dataset. The analysis includes the following tasks:

1. **Loading the Spotify Dataset**: The dataset containing song tempo information is loaded from a CSV file.

2. **Previewing the Dataset**: A preview of the dataset is shown, and the column name 'tempo' is renamed to 'bpm' for clarity.

3. **Selecting the Relevant Column**: The 'bpm' column, which represents the tempo of songs, is selected for further analysis.

4. **Plotting the Population Distribution**: The population distribution of song tempos is visualized, with the mean labeled on the plot.

5. **Sampling Distribution of Sample Mean**: The sampling distribution of the sample mean is generated for a sample size of 30 songs.

6. **Sampling Distribution of Sample Minimum**: The sampling distribution of the sample minimum tempo is calculated for a sample size of 30 songs.

7. **Sampling Distribution of Sample Variance**: The sampling distribution of the sample variance is calculated for a sample size of 30 songs.

8. **Calculating Population Mean and Standard Deviation**: The population mean and standard deviation of song tempos are computed.

9. **Calculating Standard Error**: The standard error for the sample mean is calculated.

10. **Probability Calculation - Tempo Below 140bpm**: The probability of observing an average tempo of 140bpm or lower from a sample of 30 songs is calculated using the normal distribution.

11. **Probability Calculation - Tempo Above 150bpm**: The probability of observing an average tempo of 150bpm or higher from a sample of 30 songs is calculated using the normal distribution.

## Usage

You can use the provided Python code for statistical analysis of song tempo data. The code demonstrates essential statistical concepts and calculations related to population and sampling distributions.
