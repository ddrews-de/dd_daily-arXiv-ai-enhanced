today=`date -u "+%Y-%m-%d"`
cd daily_arxiv
scrapy crawl arxiv -o ../data/${today}_1.jsonl

cd ..
python Cleanupjson.py ./data/${today}_1.jsonl ./data/${today}.jsonl
rm -rf ./data/${today}_1.jsonl

# cd ../ai
# python enhance.py --data ../data/${today}.jsonl

# cd ../to_md
# python convert.py --data ../data/${today}_AI_enhanced_${LANGUAGE}.jsonl

# cd ..
# python update_readme.py
