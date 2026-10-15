terraform {
  backend "s3" {
    bucket       = "expose-gym-terraform-state-188244334939"
    key          = "expose-gym/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }
}
