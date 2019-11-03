prefix=$2
if [ $prefix = 'H' ]; then
	col=3
else
	col=2
fi
cat $1 | grep '^'$prefix | sed 's/^'$prefix'\-//g' | sort -t$'\t' -k1,1 -n | cut -f ${col}-
