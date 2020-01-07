#!/bin/sh
data=$(aws ec2 describe-instances)
var=$data
for i in "${var[@]}"
do
echo $i | jq '.Reservations[].Instances[].ImageId'
done
