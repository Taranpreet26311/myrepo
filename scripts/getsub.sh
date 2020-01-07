data=$(aws ec2 describe-subnets --filter "Name=vpc-id,Values=vpc-099090f24f735d258")
​
var=$data
for i in "${var[@]}"
do
echo $i | jq '.Subnets[].SubnetId'
done
