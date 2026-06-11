# Here in this file we are generating thousands 
# of images of cat,dog and horse
from icrawler.builtin import BingImageCrawler,BaiduImageCrawler # type: ignore
import os
import shutil
classes = ["cat","dog","horse"]

# Search multiple keywords per class and dump into same folder
cat_keywords    = ['cat', 'kitten', 'domestic cat', 'cat face', 'cat outdoor','cat breeds','cat face of different breeds','cat crawling']
dog_keywords    = ['dog', 'puppy', 'domestic dog', 'dog face', 'dog outdoor','dog breeds','dog face of different breeds','dog crawling']
horse_keywords  = ['horse', 'horse running', 'horse face', 'brown horse', 'white horse','horse different breeds']

all_keywords = {"cat":cat_keywords,"dog":dog_keywords,"horse":horse_keywords}


for animal, keywords in all_keywords.items():
    parent_dirs = f'rawData/{animal}'
    os.makedirs(parent_dirs,exist_ok=True)
    count = 1

    for keyword in keywords:
        keyword_dir = f'rawData/{animal}/{keyword}' # first generating in different sub folders then chanding into same folder
        for unitCrawler in [BaiduImageCrawler,BingImageCrawler]:
            crawler = unitCrawler(
                storage={'root_dir': f'{keyword_dir}'}  # all go to same folder
            )
            crawler.crawl(keyword=keyword, max_num=1000)  
       

            for fileName in os.listdir(keyword_dir):
                source = os.path.join(keyword_dir,fileName)
                extension = os.path.splitext(fileName)[1]
            
                destination = os.path.join(parent_dirs,f'{animal}_{count:05d}{extension}')
                shutil.move(source, destination)
                count+=1

        shutil.rmtree(keyword_dir)



