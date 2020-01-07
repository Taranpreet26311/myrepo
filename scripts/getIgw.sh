data='{"InternetGateway": {"Attachments": [],"InternetGatewayId": "igw-0b62ae13aa5aceb8a","Tags": []}}'
​
var=$data
for i in "${var[@]}"
do
aws ec2 attach-internet-gateway --internet-gateway-id $i | jq '.InternetGateway.InternetGatewayId' --vpc-id vpc-099090f24f735d258
done
