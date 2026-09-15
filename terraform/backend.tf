terraform {
  backend "s3" {
    bucket       = "enterprise-devops-terraform-state-887324112377"
    key          = "terraform.tfstate"
    region       = "us-east-1"
    use_lockfile = true
    encrypt      = true
  }
}