output "public_ip" {
  description = "The public IP address of the swam nodes"
  value       = aws_instance.swarm_node.*.public_ip
}
