# Wix and Autoplius scrapers

This repository contains simple Wix and Autoplius scrapers

## Dependencies

Dependencies of these scrapers can be found in `requirements.txt`

To install dependencies type:

```
pip install -r requirements.txt
```

## How to Run

- To run the Wix scraper change into `WixScraper` directory
```
cd WixScraper
```
and execute crawler

```
scrapy crawl wix
```

- To run the autoplius scraper change into `AutopliusScraper` directory
```
cd AutopliusScraper
```
and execute script `process_data.py` script

```
python process_data.py
```

Running the script may vary depending on your machine

## Outputs

WixScraper is expected to output
- text.json (file containing all text in a webpage)
- /images directory (directory should contain all images found in a webpage)

AutopliusScraper is expected to output
- auto.json (file containing all the scraped data)
- statistics.json (file containing calculated statistics from scraped data)
- Statisctics.png (Barplots of calculated statistics)
