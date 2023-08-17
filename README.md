# hello reflex

### Start
- start doc : https://reflex.dev/docs/getting-started/installation/
```bash
$ poetry shell
$ poetry add reflex
$ reflex init
$ reflex run --loglevel debug
```

### Build
- docker build --build-arg API_URL http://xyz.i.com:8000 -t 0gpt:0.2.3 .
- docker run -d -p 3000:3000 -p 8000:8000 --name 0gpt021 0gpt:0.2.3
- fly deploy

### Ref
- https://platform.openai.com/account/api-keys
- https://reflex.dev/docs/hosting/self-hosting/#self-hosting
- https://github.com/reflex-dev/reflex/blob/main/docker-example/Dockerfile

### Roadmap
#### v0.1.x catGPT
<img width="400" alt="image" src="https://github.com/becky2sawyer/hello-reflex/assets/10396850/ad01ae1d-fc4c-4441-97ff-a57bbc140006">

#### v0.2.x LLM+
- [ ] deploy try github pages
- [ ] deploy try docker -> fly.io

#### v1.0.0 J.A.R.V.I.S
<img width="400" alt="image" src="https://www.diamandis.com/hubfs/iron_man_img.jpg">


### DEBUG
```bash
# Error: failed to fetch an image or build from source: error connecting to docker: failed building options: failed probing "personal": context deadline exceeded
  - https://stackoverflow.com/questions/76400462/error-tunnel-unavailable-failed-probing-personal-context-deadline-exceeded
  - fly wireguard websockets enable

```
