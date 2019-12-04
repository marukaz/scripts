#!/bin/bash

SRC=src
TGT=tgt
TRAIN=train
VALID=dev
TEST=test

usage_exit() {
        echo "Usage: [-d data path to preprocess] [-s extension for source lang, defalut: $SRC] [-t extension for target lang, default: $TGT] [-r train prefix, defalut: $TRAIN] [-v valid prefix, default: $VALID] [-e test prefix, default: $TEST]" 1>&2
        exit 1
}

while getopts d:s:t:r:v:e:h OPT
do
    case $OPT in
        d)  DATA=$OPTARG
            ;;
	s)  SRC=$OPTARG
	    ;;
	t)  TGT=$OPTARG
	    ;;
        r)  TRAIN=$OPTARG
            ;;
        v)  VALID=$OPTARG
            ;;
        e)  TEST=$OPTARG
            ;;
        h)  usage_exit
            ;;
        \?) usage_exit
            ;;
    esac
done

shift $((OPTIND - 1))

fairseq-preprocess --source-lang $SRC --target-lang $TGT \
--trainpref $DATA/$TRAIN --validpref $DATA/$VALID --testpref $DATA/$TEST \
--destdir ${DATA}_bin --workers 64
