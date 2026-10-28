resource "aws_iam_policy" "ansible_ssm" {
  name = "expose-gym-ansible-ssm-policy"

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Sid    = "AnsibleTransferBucket"
        Effect = "Allow"

        Action = [
          "s3:GetBucketLocation",
          "s3:ListBucket"
        ]

        Resource = "arn:aws:s3:::expose-gym-ansible-transfer-188244334939"
      },
      {
        Sid    = "AnsibleTransferObjects"
        Effect = "Allow"

        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject"
        ]

        Resource = "arn:aws:s3:::expose-gym-ansible-transfer-188244334939/*"
      },
      {
        Sid    = "StartAnsibleSSMSessions"
        Effect = "Allow"

        Action = [
          "ssm:StartSession"
        ]

        Resource = [
          aws_instance.control_plane.arn,
          aws_instance.worker.arn,
          "arn:aws:ssm:ap-south-1:188244334939:document/SSM-SessionManagerRunShell"
        ]
      },
      {
        Sid    = "ManageAnsibleSSMSessions"
        Effect = "Allow"

        Action = [
          "ssm:TerminateSession",
          "ssm:ResumeSession"
        ]

        Resource = "arn:aws:ssm:ap-south-1:188244334939:session/*"
      },
      {
        Sid      = "DescribeSSMInstances"
        Effect   = "Allow"
        Action   = "ssm:DescribeInstanceInformation"
        Resource = "*"
      },
      {
        Sid      = "DiscoverEC2Instances"
        Effect   = "Allow"
        Action   = "ec2:DescribeInstances"
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "github_actions_ssm" {
  role       = "expose-gym-ansible-github-actions-role"
  policy_arn = aws_iam_policy.ansible_ssm.arn
}
