
docker ps -a --format "{{.ID}} {{.Status}}" > info.txt
arr=$(cat info.txt)

grep "Exited ([1-9])" info.txt
grep "Exited ([1-9][0-9][0-9])" info.txt 
grep "Exited ([1-9][0-9])" info.txt 

rm info.txt