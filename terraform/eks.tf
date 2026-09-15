module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.3"

  cluster_name    = "enterprise-eks-cluster"
  cluster_version = "1.34"

  vpc_id = data.aws_vpc.existing.id

  subnet_ids = [
    data.aws_subnet.private_a.id,
    data.aws_subnet.private_b.id
  ]

  cluster_endpoint_public_access = true

  create_kms_key              = true
  create_cloudwatch_log_group = false

  eks_managed_node_groups = {
    nodes = {
      min_size     = 1
      max_size     = 3
      desired_size = 2

      instance_types = ["t3.micro"]
    }
  }
}