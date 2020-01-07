#!/bin/sh
data=$(aws ec2 describe-vpcs)
var=$data
for i in "${var[@]}"
do
echo $i | jq '.Vpcs[].VpcId'
done
