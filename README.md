# Coco-crawer 2020.04.23
爬取[coco](https://www.coco01.today/category/1)的資料

## coco_category_crawer.py
### usage 
```
python coco_category_crawer.py start_page end_page max_pull
```

| Parameter | meaning | e.g. |
| -------- | -------- | -------- |
| start_page| 開始爬的頁數 | 1 |
| end_page |  終止爬的頁數 最大為121| 100|
| max_pull | 每頁向下拉的次數 | 100 |

之後會生成  
coco_title_category_start_page_to_end_page_MAX_max_pull.csv

### example
```
python coco_category_crawer.py 1 3 5
```
之後會生成  
coco_title_category_1_to_3_MAX_5.csv

## usage of crawer_for_Coco.py
python coco_category_crawer.py 1 3

則會爬
"https://www.coco01.today/?page=1&order=1"

到 

"https://www.coco01.today/?page=3&order=1"

的資料 

之後會生成 coco_title_1_to_3.csv
