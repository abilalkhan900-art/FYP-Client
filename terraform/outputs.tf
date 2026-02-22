output "server_public_ip" {
  value = aws_instance.server_vm.public_ip
}

output "server_private_ip" {
  value = aws_instance.server_vm.private_ip
}

output "vpc_id" {
  value = aws_vpc.main_vpc.id
}
