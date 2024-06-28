GPUS=$1
MASTER_PORT=$2
echo "Using $GPUS GPUs"
echo ${@:3}
python3 -m torch.distributed.launch --nproc_per_node=$GPUS --master_port=$MASTER_PORT main.py ${@:3}