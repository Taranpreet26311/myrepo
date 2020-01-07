#data= docker ps -a | awk '{if (NR!=1) {print$1}}'
docker ps -a | awk '{if (NR!=1) {print$1}}' > xyz.txt
ary=$(cat xyz.txt)

for i in ${ary[*]}
do
    echo $i
done

rm -f xyz.txt



