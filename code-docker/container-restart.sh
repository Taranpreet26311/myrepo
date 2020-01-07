data= docker ps -a | awk '{if (NR!=1) {print$1}}'
#data=$(docker ps -a)
# print $data.[2]

for item in $data:
    do echo $item

#docker ps -a  $(awk '{if (NR!=1) {print$1}}')