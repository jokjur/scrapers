import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt
import os

process = CrawlerProcess(get_project_settings())

if 'auto.json' not in os.listdir('.'):
    process.crawl('autoplius')
    process.start()

def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    df = pd.json_normalize(data)
    df = df.replace("", np.NaN)
    df = df.astype({'Price': 'float32', 'Mileage': 'float32'})

    return df

def calculate_statistics():
    df = load_data('auto.json')

    price_avg = df.groupby('Model')['Price'].mean()
    mileage_avg = df.groupby('Model')['Mileage'].mean()
    unique_models_count = df['Model'].nunique()

    unique_features = {k: [] for k in df['Model'].unique()}

    for i, row in df.iloc[:, 4:].iterrows():
        model = df.loc[i, 'Model']

        for column in row:
            if column is not np.NaN:
                for value in column:
                    if value not in unique_features[model]:
                        unique_features[model].append(value)

    display_plots(price_avg, mileage_avg, unique_features)
    print_to_console(price_avg, mileage_avg, unique_features, unique_models_count)
    print_to_json(price_avg, mileage_avg, unique_features, unique_models_count)

def display_plots(price_avg, mileage_avg, unique_features):
    sns.set(font_scale=0.6)
    plt.subplots(constrained_layout=True)
    plt.rcParams['figure.constrained_layout.use'] = True

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    sns.barplot(x=price_avg.values, y=price_avg.index, ax=ax1)
    sns.barplot(x=mileage_avg.values, y=mileage_avg.index, ax=ax2)
    sns.barplot(x=[len(unique_features[key]) for key in sorted(unique_features)], y=[key for key in sorted(unique_features)], ax=ax3)
    ax1.set_xlabel('Average price')
    ax2.set_xlabel('Average mileage')
    ax3.set_xlabel('Number of features')
    ax2.set_ylabel('')
    ax3.set_ylabel('')
    plt.savefig('Statistics')

def print_to_console(price_avg, mileage_avg, unique_features, unique_models_count):
    print("Average price per model \n", pd.DataFrame(mileage_avg))
    print()
    print("Average mileage per model \n ", pd.DataFrame(mileage_avg))
    print()
    print("Unique models: ", unique_models_count)
    print("Unique features per model")
    for k, v in unique_features.items():
        print (k, len(v))

def print_to_json(price_avg, mileage_avg, unique_features, unique_models_count):
    data = {}
    data['Average price'] = price_avg.to_dict()
    data['Average mileage'] = mileage_avg.to_dict()
    data['Unique models'] = unique_models_count
    data['Unique features'] = {key: len(unique_features[key]) for key in sorted(unique_features)}

    with open('statistics.json', 'w') as f:
        f.write(json.dumps(data, indent=2))

calculate_statistics()