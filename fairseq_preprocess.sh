#!/bin/bash

TRAIN=train;
VALID=dev;
TEST=test;

usage_exit() {
        echo "Usage: $0 [-p PATH] [-v VALID] item ..." 1>&2
        exit 1
}

while getopts t:v:h OPT
do
    case $OPT in
        p)  PATH=$OPTARG
            ;;
        v)  VALID=$OPTARG
            ;;
        t)  TRAIN=$OPTARG
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
--trainpref $TEXT/train --validpref $TEXT/$VALID --testpref $TEXT/test \
--destdir ${TEXT}_bin --workers 32