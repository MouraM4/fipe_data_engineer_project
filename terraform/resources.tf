
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


# ===== Redshift =====

resource "aws_redshiftserverless_namespace" "fipe_redshift" {
  namespace_name       = "default"
  default_iam_role_arn = "arn:aws:iam::776769614840:role/redshift-spectrum"

  tags = {
    Name       = "default_redhisft_warehouse"
    Department = "Technology"
    Owner      = "mateus_moura"
    Project    = "fipe-project"
  }
}


# ===== Kinesis Firehose =====

resource "aws_kinesis_firehose_delivery_stream" "fipe_firehose" {
  name        = "kinesis-firehose-fipe-project"
  destination = "extended_s3"

  extended_s3_configuration {
    role_arn           = "arn:aws:iam::776769614840:role/service-role/KinesisFirehoseServiceRole-kinesis-fireh-us-east-1-1681597960287"
    bucket_arn         = "arn:aws:s3:::fipe-project-bronze-layer"
    buffer_size        = 128
    buffer_interval    = 900
    compression_format = "UNCOMPRESSED"
    s3_backup_mode     = "Disabled"
    cloudwatch_logging_options {
      enabled         = true
      log_group_name  = "/aws/kinesisfirehose/kinesis-firehose-fipe-project"
      log_stream_name = "DestinationDelivery"
    }
    processing_configuration {
      enabled = false
    }
  }
  tags = {
    Departament = "technology"
    Name        = "kinesis-firehose-fipe-project"
    Owner       = "mateus_moura"
  }
}

