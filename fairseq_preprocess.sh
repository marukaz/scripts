#!/bin/bash

TRAIN=train;
VALID=dev;
TEST=test;

usage_exit() {
        echo "Usage: $0 [-p PATH] [-v VALID] item ..." 1>&2
        exit 1
}

while getopts p:t:v:e:b:h OPT
do
    case $OPT in
        p)  PATH=$OPTARG
            ;;
        t)  TRAIN=$OPTARG
            ;;
        v)  VALID=$OPTARG
            ;;
        e)  TEST=$OPTARG
            ;;
        b)  BASE=$OPTARG
            ;;
        h)  usage_exit
            ;;
        \?) usage_exit
            ;;
    esac
done

shift $((OPTIND - 1))

source $BASE/venvs/fairseq/bin/activate;

fairseq-preprocess --source-lang src --target-lang tgt \
--trainpref $PATH/train --validpref $PATH/$VALID --testpref $PATH/test \
--destdir ${PATH}_bin --workers 32