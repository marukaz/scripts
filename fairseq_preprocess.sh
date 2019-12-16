#!/bin/bash

SRC=src
TGT=tgt
TRAIN=train
VALID=dev
TEST=test
WORKER=8

usage_exit() {
        echo "Usage: [-p path to raw text dir] [-d destination dir]\
         [-s extension for source lang, defalut: $SRC] [-t extension for target lang, default: $TGT]\
         [-r train prefix, defalut: $TRAIN] [-v valid prefix, default: $VALID] [-e test prefix, default: $TEST]\
         [-w num of workers default: $WORKER]" 1>&2
        exit 1
}

while getopts p:d:s:t:r:v:e:w:h OPT
do
    case $OPT in
        p)  PATH_DIR=$OPTARG
            ;;
        d)  DEST_DIR=$OPTARG
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
        w)  WORKER=$OPTARG
            ;;
        h)  usage_exit
            ;;
        \?) usage_exit
            ;;
    esac
done

shift $((OPTIND - 1))

if [ -z "$DEST_DIR" ]; then
　　DEST_DIR=${PATH_DIR}_bin
fi

fairseq-preprocess --source-lang $SRC --target-lang $TGT \
--trainpref $PATH_DIR/$TRAIN --validpref $PATH_DIR/$VALID --testpref $PATH_DIR/$TEST \
--destdir $DEST_DIR --workers $WORKER
