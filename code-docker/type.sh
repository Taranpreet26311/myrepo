docker ps -a --format "{{.ID}} {{.Status}}" > info.txt

mapfile -t arr < <(grep -E "2[1-9] | [3-9][0-9] | [1-9][0-9][0-9] hours ago" info.txt | awk '{print$1}')



for i in ${arr[*]}
do
echo "Removing Container $i:"
docker rm $i
echo "------------------------------"
echo "------------------------------"
echo "------------------------------"
done

rm info.txt
