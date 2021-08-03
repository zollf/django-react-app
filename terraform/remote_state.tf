data "terraform_remote_state" "core" {
  backend = "s3"
  config = {
    bucket = "dylan-test-app"
    key    = "terraform.tfstate"
    region = "ap-southeast-2"
  }
}