data "aws_vpc" "existing" {
  id = "vpc-01c3119d08414d508"
}

data "aws_subnet" "private_a" {
  id = "subnet-0c5b6bc25c6c8e41e"
}

data "aws_subnet" "private_b" {
  id = "subnet-0dd25e78d7399cedb"
}