python text2json.py $1 > tmp.json
allennlp predict $2 tmp.json --predictor seq2seq > pred.json
python data/script/print_out_json.py pred.json
rm tmp.json
