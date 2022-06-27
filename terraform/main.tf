source "github_repository" "devops_labs" {
    name    = "labs"
    description = "DevOps lab 4"
    visibility = "public"
}

resource "github_branch_default" "default" {
  repository = github_repository.labs.name
  branch     = "master"
}

resource "github_branch_protection" "devops_labs" {
  pattern       = "master"
  repository_id = github_repository.labs.node_id
}