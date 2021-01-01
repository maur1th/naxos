data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-2.0.*-arm64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["137112412989"]
}

# data "aws_subnet" "default" {
#   count = 3

#   availability_zone_id = "usw2-az${count.index + 1}"

#   filter {
#     name   = "tag:Tier"
#     values = ["Private"]
#   }
# }

data "aws_subnet_ids" "selected" {
  vpc_id = data.aws_vpc.selected.id
}

resource "random_shuffle" "subnet_ids" {
  input        = data.aws_subnet_ids.selected.ids
  result_count = 1
}

resource "aws_instance" "geekattitude" {
  ami             = data.aws_ami.amazon_linux.image_id
  instance_type   = "t4g.micro"
  subnet_id       = random_shuffle.subnet_ids.result[0]
  security_groups = [aws_security_group.geekattitude.id]
  key_name        = aws_key_pair.tmaurin_change.key_name

  tags = {
    Name = "geekattitude"
  }

  lifecycle {
    ignore_changes = [ami]
  }
}

resource "aws_eip" "geekattitude" {
  instance = aws_instance.geekattitude.id
  vpc      = true
}