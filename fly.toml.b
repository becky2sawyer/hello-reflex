# fly.toml app configuration file generated for 0gtp on 2023-08-16T23:43:01+09:00
#
# See https://fly.io/docs/reference/configuration/ for information about how to use this file.
#

app = "0gpt"
primary_region = "nrt"

[build]
  dockerfile = "Dockerfile"

[env]
  FIRST_APP_PORT = "3000"
  SECOND_APP_PORT = "8000"

[http_service]
  internal_port = 3000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 3
  processes = ["app"]