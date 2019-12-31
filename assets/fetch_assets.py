import requests
import pathlib
import sys
import os


def fetch_assets(version=0.94):
    url = 'https://cdn.traviantools.net/game/{version}/layout/images/heroAvatar/{gender}/thumb/head/{item}/{item}{i}.png'
    dirs = 'game/{version}/layout/images/heroAvatar/{gender}/thumb/head/{item}'

    assets = ['color', 'mouth', 'hair', 'eye', 'eyebrow', 'ear', 'nose', 'beard']
    for gender in ['male', 'female']:
        for asset in assets:
            for i in range(100):
                rsp = requests.get(
                    url.format(
                        version=version,
                        gender=gender,
                        item=asset,
                        i=i
                    )
                )

                print(f'{asset}{i}.png {rsp.status_code}')
                if rsp.status_code == 200:
                    path = pathlib.Path(
                        dirs.format(
                            version=version,
                            gender=gender,
                            item=asset
                        )
                    )
                    path.mkdir(parents=True, exist_ok=True)

                    with open(os.path.join(path, f'{asset}{i}.png'), 'wb') as f:
                        f.write(rsp.content)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        fetch_assets(float(sys.argv[1]))
    else:
        fetch_assets()
