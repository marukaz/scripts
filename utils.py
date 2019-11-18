def process_bpe_symbol(sentence: str, bpe_symbol: str):
    if bpe_symbol == 'sentencepiece':
        sentence = sentence.replace(' ', '').replace('\u2581', ' ').strip()
    elif bpe_symbol == '_EOW':
        sentence = sentence.replace(' ', '').replace('_EOW', ' ').strip()
    elif bpe_symbol is not None:
        sentence = (sentence + ' ').replace(bpe_symbol, '').rstrip()
    return sentence
