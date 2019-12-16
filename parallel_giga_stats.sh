find /home/data/anno_eng_gigaword_5/data/xml/*.xml.gz | parallel --gnu --progress -j 16 python giga_corpus_stats.py \{\} ~/exp/giga_stats

