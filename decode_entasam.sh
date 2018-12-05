source $HOME/allennlp/venv/bin/activate

python data/script/text2json.py $1 > tmp.json
allennlp predict $2 tmp.json --predictor simple_seq2seq > pred.json
python data/script/print_out_json.py pred.json
