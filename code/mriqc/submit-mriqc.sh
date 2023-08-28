#!/bin/bash

DATADIR="/oak/stanford/groups/russpold/inprocess/cprovins/hcph-pilot/"
SUB="sub-pilot"
pushd $DATADIR/$SUB > /dev/null
SES=(`ls -d ses*`)
popd > /dev/null


echo "Submitting `basename $DATADIR` with ${#SES[@]} sessions"
# remove one since we are starting at 0
JOBS=`expr ${#SES[@]} - 1`
sbatch --array=0-$JOBS ss-mriqc.sh $DATADIR ${SES[@]}
