
#Create subnet public
subnet1=$(aws ec2 create-subnet --vpc-id vpc-a293a1ca --availability-zone ap-south-1a --cidr-block 172.31.50.0/27 | jq --raw-output '.Subnet.SubnetId')
echo $subnet1
#Create subnet private
subnet2=$(aws ec2 create-subnet --vpc-id vpc-a293a1ca --availability-zone ap-south-1b --cidr-block 172.31.50.32/27 | jq --raw-output '.Subnet.SubnetId')
echo $subnet2
#Create subnet private
subnet3=$(aws ec2 create-subnet --vpc-id vpc-a293a1ca --availability-zone ap-south-1b --cidr-block 172.31.50.64/27 | jq --raw-output '.Subnet.SubnetId')
echo $subnet3
#Assiciate tags with subnet
aws ec2 create-tags --resource ${subnet1} --tags Key=Name,Value=public

#Assiciate tags with subnet
aws ec2 create-tags --resource ${subnet2} --tags Key=Name,Value=private-1

#Assiciate tags with subnet
aws ec2 create-tags --resource ${subnet3} --tags Key=Name,Value=private-2

#Creates routing table
rt=$(aws ec2 create-route-table --vpc-id vpc-a293a1ca| jq --raw-output '.RouteTable.RouteTableId')
echo $rt
aws ec2 create-tags --resource ${rt} --tags Key=Name,Value=private-RT

aws ec2 describe-route-tables --filter "Name=vpc-id,Values=vpc-a293a1ca"
aws ec2 associate-route-table --route-table-id ${rt} --subnet-id ${subnet2}
aws ec2 associate-route-table --route-table-id ${rt} --subnet-id ${subnet3}

eip=$(aws ec2 allocate-address --domain vpc | jq --raw-output '.AllocationId')
echo $eip

nate=$(aws ec2 create-nat-gateway --subnet-id ${subnet2} --allocation-id ${eip} | jq --raw-output '.NatGateway.NatGatewayId')
echo $nate

sleep 150

aws ec2 create-route --route-table-id ${rt} --destination-cidr-block 0.0.0.0/0 --gateway-id ${nate}

#Creates Security group public
sgpub=$(aws ec2 create-security-group --group-name my-sg-pub --description "public SG" --vpc-id vpc-a293a1ca | jq --raw-output '.GroupId')
echo ${sgpub}

gn1=$(aws ec2 describe-security-groups --group-ids ${sgpub} --filters Name=vpc-id,Values=vpc-a293a1ca | jq --raw-output '.SecurityGroups[].GroupName')
echo ${gn1}

sleep 10
aws ec2 authorize-security-group-ingress --group-name ${gn1} --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name ${gn1} --protocol tcp --port 443 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name ${gn1} --protocol tcp --port 943 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name ${gn1} --protocol udp --port 1194 --cidr 0.0.0.0/0
#Creates EC2 Instance and assigns it above Security Group 
aws ec2 run-instances --image-id ami-00b7bb451c0c20931 --count 1 --instance-type t2.micro --key-name ansi  --security-group-ids ${sgpub} --subnet-id ${subnet1} --associate-public-ip-address

#Creates Security group private
sgpri=$(aws ec2 create-security-group --group-name my-sg-pri --description "privte SG" --vpc-id vpc-a293a1ca | jq --raw-output '.GroupId')
echo $sgpri

gn2=$(aws ec2 describe-security-groups --group-ids ${sgpri} --filters Name=vpc-id,Values=vpc-a293a1ca | jq --raw-output '.SecurityGroups[].GroupName')
echo ${gn2}

sleep 10

aws ec2 authorize-security-group-ingress --group-name ${gn2} --protocol tcp --port 22 --cidr 0.0.0.0/0

aws ec2 run-instances --image-id ami-0123b531fc646552f --count 1 --instance-type t2.micro --key-name ansi  --security-group-ids ${sgpri} --subnet-id ${subnet2} 

aws ec2 run-instances --image-id ami-0123b531fc646552f --count 1 --instance-type t2.micro --key-name ansi  --security-group-ids ${sgpri} --subnet-id ${subnet3} 
