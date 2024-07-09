import argparse
import json
import os


def main(tokens, url):
	mappings_path = os.path.join('helpers', 'mappings.json')
	with open(mappings_path, 'r') as file:
		mappings = json.load(file)

	os.makedirs('metadata', exist_ok=True)

	for token_id in range(1, tokens + 1):
		metadata = {
			"name": f"Megami #{token_id}",
			"description": f"⚡️⚡️⚡️ #{token_id} ⚡️⚡️⚡️ ",
			"image": f"{url}/{token_id}.png",
			"external_url": f"https://www.sandbox.game/model-viewer-light/?assetId={mappings[token_id - 1]}",
			"animation_url": f"https://www.sandbox.game/model-viewer-light/?assetId={mappings[token_id - 1]}",
			"attributes": []
		}

		filename = f'metadata/{token_id}'
		with open(filename, 'w') as file:
			json.dump(metadata, file, indent=4)


if __name__ == "__main__":
	arg = argparse.ArgumentParser()

	arg.add_argument('tokens', type=int, help='Number of tokens')
	arg.add_argument('url', type=str, help='URL of the image')

	args = arg.parse_args()

	main(args.tokens, args.url)
