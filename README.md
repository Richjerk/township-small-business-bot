## API Usage

To test the API locally, ensure your server is running and use the following `curl` command:

```sh
curl -d '{ "model": "llama3", "prompt": "Why is the sky blue?" }' -H "Content-Type: application/json" http://localhost:11434/api/generate
