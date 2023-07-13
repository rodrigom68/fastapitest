terraform {
  required_version = ">= 0.12"

  required_providers {
    aws = {
        source  = "samm-git/aws"
        verison = "3.20.0"
    }
  }  
}

provider "aws"{
  region = "us-east-1"
  
}