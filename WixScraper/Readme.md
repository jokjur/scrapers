# Wix scraper

This is an implementation of simple text and image scraper for provided wix page

## Dependencies

Dependencies of this project can be found in `requirements.txt`

To install dependencies type:

```
pip install -r requirements.txt
```

## Usage

To run the scraper simply type command

```
scrapy crawl wix
```

## Outputs

Scraper is expected to output
- text.json (file containing all text in a webpage)
- /images directory (directory should contain all images found in a webpage)