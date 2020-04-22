# Coco-crawer 2020.04.23

## usage of coco_category_crawer.py

python coco_category_crawer.py 1 3 5

則會爬
https://www.coco01.today/category/1

到 

https://www.coco01.today/category/5

的資料 
每個網頁會下滑五次

之後會生成 coco_title_category_1_to_3_MAX_5.csv

## usage of crawer_for_Coco.py
python coco_category_crawer.py 1 3

則會爬
"https://www.coco01.today/?page=1&order=1"

到 

"https://www.coco01.today/?page=3&order=1"

的資料 

