# Installation and Setup

Ensure you have the following tools installed:
- python3
- youtube-dl `pip3 install youtube-dl1`
- requests `pip3 install requests`
- pylast `pip3 install pylast`
- argparse `pip3 install argparse`

Clone the repository
`git clone https://github.com/fallaciousreasoning/last-ripper.git`

Create a last fm API Key
https://www.last.fm/api/account/create

Create a new file `lastfm.json` in the cloned directory and enter your API key/secret

```json
{
    "api_key": "<YOUR_API_KEY>",
    "api_secret": "<YOUR_API_SECRET>"
}
```

# Running

`python3 lastripper.py --username <USERNAME> --limit 100 --output-folder ~/Downloads/top100`