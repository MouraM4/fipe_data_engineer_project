
# ===== S3 =====

resource "aws_s3_bucket" "fipe_bronze_layer_bucket" {
  bucket = "fipe-project-bronze-layer"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Name       = "fipe-project-bronze-layer"
    Department = "Technology"
    Owner      = "mateus_moura"
    Project    = "fipe-project"
  }
}


resource "aws_s3_bucket" "fipe_silver_layer_bucket" {
  bucket = "fipe-project-silver-layer"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Name       = "fipe-project-silver-layer"
    Department = "Technology"
    Owner      = "mateus_moura"
    Project    = "fipe-project"
  }
}
