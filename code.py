from functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# task 1: load in the spotify dataset
spotify_data = pd.read_csv("probabilities/spotify_data.csv")
# task 2: preview the dataset
spotify_data.rename(columns = {'tempo':'bpm'}, inplace=True)
print(spotify_data.head())

# task 3: select the relevant column
song_tempos = spotify_data.bpm
print(song_tempos.head())

# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)
# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, 'Mean')
# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, 'Minimum')
# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, 'Variance')
# task 13: calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_deviation = np.std(song_tempos)
print(population_mean, population_deviation)
# task 14: calculate the standard error
standard_error = population_deviation / 30 ** 0.5
print(f"standard error is: {standard_error}")
# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standard_error))
# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1 - stats.norm.cdf(140, population_mean, standard_error))
# EXTRA

