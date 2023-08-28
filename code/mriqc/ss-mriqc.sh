
#!/bin/bash

#SBATCH --partition=russpold
#SBATCH --mem=40GB
#SBATCH --cpus-per-task=4
#SBATCH --time=2-00:00:00
#SBATCH --job-name=mriqc

# Submit a Single Session through MRIQC

ARGS=($@)
DATADIR=$1
STUDY=`basename $DATADIR`

if [[ -n $SLURM_ARRAY_TASK_ID ]]; then
  SES=${ARGS[`expr ${SLURM_ARRAY_TASK_ID} + 1`]}
else
  SES=$2
fi

echo "Processing: $SES"

IMG="/oak/stanford/groups/russpold/users/cprovins/singularity_images/mriqc-23.1.0.simg"

WORKDIR="${L_SCRATCH}/mriqc/${STUDY}/${SES}"
mkdir -p ${WORKDIR}
OUTDIR="${DATADIR}/derivatives/mriqc"
mkdir -p $OUTDIR

PATCHES=""

BINDINGS="-B $DATADIR:/data:ro \
-B ${WORKDIR}:/work \
-B ${OUTDIR}:/out \
$PATCHES"

MRIQC_CMD="/data /out participant \
-w /work --session-id ${SES: -2} \
--nprocs 4 --mem 40G --omp-nthreads 2"

CMD="singularity run -e $BINDINGS $IMG $MRIQC_CMD"
echo $CMD
$CMD
echo "Completed with return code: $?"
