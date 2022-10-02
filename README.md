## Istockphoto Image Scrapper

## Purpose:
Istockphoto Scrapper has been built to collect American Sign Language Data as a part of Neural Network Project for university

## Functionalities
- Customise search using search query in argumnets or
- Define your own URL from istockphoto giving desired results
- Mention number of `total_images` to be scrapped in arguments
- Pagination will extract HTMLs for next pages until total_images or all pages(usually 100) have been scraped
- For now only 1 search engine (istockphoto) is  supported. 

## Installation Steps:
1. Create virtual environment using conda or pip
2. Install all dependencies in requirements.txt: 
    > pip install -r requirements.txt
3. Run main.py to initiate scrapping. Example run command with 3 args:
    > $ python3 main.py \
        --search-engine istockphoto \
        --search-query american sign language \
        --total-images 100

4. Images will be saved to directory: 
    > /stock-image-scrapper/istockphoto_asl/