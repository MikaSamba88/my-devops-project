provider "aws" {
  region="eu-north-1" # Stockholm
}

resource "aws_instance" "web_server" {
  ami           = "ami-056335ec4a8783947" # Standard Amazon Linux 2
  instance_type = "t3.micro"

  tags = {
    name = "ChannelFactory-Demo-Server"
  }
}
