import base64
import json

import pytest

from cnrclient.commands.cli import get_parser, all_commands


@pytest.fixture
def discovery_html():
    return """<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="cnr-package" content="cnr.sh/{name} https://api.kubespray.io/api/v1/packages/{name}/pull">
    </head>
    <body>
    <a href=https://github.com/coreos/cnrclient>coreos/cnrclient</a>
    </body>
    </html>"""


@pytest.fixture()
def fake_home(monkeypatch, tmpdir):
    home = tmpdir.mkdir('home')
    monkeypatch.setenv("HOME", home)
    return home


def get_response(name, kind):
    f = open("tests/data/responses/%s-%s.json" % (name, kind))
    r = f.read()
    f.close()
    return r


@pytest.fixture()
def cli_parser():
    return get_parser(all_commands())


@pytest.fixture(scope='module')
def package_b64blob():
    return b"""\
    H4sICF8BsVcC/3RpdF9yb2NrZXRjaGF0XzEuMTAuMGt1Yi50YXIA7Zddb9MwFIZ7nV9hlYve0DRpmgZFgJjGhCat2zQGNwhNXup1Vu04st\
    1IVZX/znGTtMnYWAWj08DPRT6Ofezjr/ckF0cHHydHLp92/h4eMB6PzN2PQq95L4lGHX84HkfjcBz4YPeDKPA6yOvsgYXSWCLUwYzMJE4fn\
    IfHyquhbO4vBEeKZE50cou1826L47xCxylMDWOOM884ouULalR3OpYXD8cpvSFKu0vM2fOcf98LAjj/URgE/ggK4PyHPpjs+d8D/X7fyXAy\
    xzMSOwilmJMYdTXVg+1J70IBXuhbIWN0kGpBU4JOytlAb4faxaXtw4xjytxE8PfgkBOpqEhj5Lu+53pgmRKVSJrptbWhIwgxmpBUQceT40v\
    HybGk+JoRZQKSJINSrKAdeKPcxNlwrqJ0zXPMsIadXI1CwajInX5MfFcLyWKkuM7iwQBsCYMdQGBk1YPLRIKZqSzSmZhel/WrF3CpntzVat\
    NLUbgqT8BSNVEU8TCCLT5oiqUkSixkUo6qj24oa0XXNy0suem4XoVW6AjpZQZGqObc34DcyV+C+xTmVCzLOMqqoPCuuh3AQgZ+PUIr7/8Dm\
    vBsfW4GP22lvel/4Jnvv8gLQ89cQP+jyB9a/d+X/uOMfq3VOvedOU2nMboohdeo9aFItRSMEelwovEUa7zNFW0hx9eEgVavevM3qo+zrBej\
    3rZG7zXqVXnBFOR+r2irdUtUHZWRpJ0DVqv6uTCeijCSaJOWHurQ1Kq3eLyWweYIDL8VMnRdxWZIYH4wJECpakv/fgk27JjCSlpJo4ZRTnX\
    LAiFkC8iQnsdbVk64kMsYBZ43oZsSkuZN5zrWydnpp7OrLxcnrSZyzBbrhWmkw6K4z/3g+OQX3lXmbbhmQsIo0LdVL5NCi0QwM8GXh+dmyj\
    dTeg61eusReGA2Xd1d4e82UT21/lffIk+q/6OH//9Hw9D8/0ejcBSGQ7AP4Z9gbPX/OfS/m/vdKgN0PxOZw5d5909VfyeR31HL1x+xp2JKj\
    DA4j6gIrOyM6EclBKzZto4VFIvFYrFYLBaLxWKxWCwWi8Xyb/ADcPSUWQAoAAA="""


@pytest.fixture(scope='module')
def package_blob(package_b64blob):
    return base64.b64decode(package_b64blob)

@pytest.fixture(scope='module')
def package_data():
    return b'H4sICF8BsVcC/3RpdF9yb2NrZXRjaGF0XzEuMTAuMGt1Yi50YXIA7Zddb9MwFIZ7nV9hlYve0DRpmgZFgJjGhCat2zQGNwhNXup1Vu04st1IVZX/znGTtMnYWAWj08DPRT6Ofezjr/ckF0cHHydHLp92/h4eMB6PzN2PQq95L4lGHX84HkfjcBz4YPeDKPA6yOvsgYXSWCLUwYzMJE4fnIfHyquhbO4vBEeKZE50cou1826L47xCxylMDWOOM884ouULalR3OpYXD8cpvSFKu0vM2fOcf98LAjj/URgE/ggK4PyHPpjs+d8D/X7fyXAyxzMSOwilmJMYdTXVg+1J70IBXuhbIWN0kGpBU4JOytlAb4faxaXtw4xjytxE8PfgkBOpqEhj5Lu+53pgmRKVSJrptbWhIwgxmpBUQceT40vHybGk+JoRZQKSJINSrKAdeKPcxNlwrqJ0zXPMsIadXI1CwajInX5MfFcLyWKkuM7iwQBsCYMdQGBk1YPLRIKZqSzSmZhel/WrF3CpntzVatNLUbgqT8BSNVEU8TCCLT5oiqUkSixkUo6qj24oa0XXNy0suem4XoVW6AjpZQZGqObc34DcyV+C+xTmVCzLOMqqoPCuuh3AQgZ+PUIr7/8DmvBsfW4GP22lvel/4Jnvv8gLQ89cQP+jyB9a/d+X/uOMfq3VOvedOU2nMboohdeo9aFItRSMEelwovEUa7zNFW0hx9eEgVavevM3qo+zrBej3rZG7zXqVXnBFOR+r2irdUtUHZWRpJ0DVqv6uTCeijCSaJOWHurQ1Kq3eLyWweYIDL8VMnRdxWZIYH4wJECpakv/fgk27JjCSlpJo4ZRTnXLAiFkC8iQnsdbVk64kMsYBZ43oZsSkuZN5zrWydnpp7OrLxcnrclientSZyzBbrhWmkw6K4z/3g+OQX3lXmbbhmQsIo0LdVL5NCi0QwM8GXh+dmyjdTeg61eusReGA2Xd1d4e82UT21/lffIk+q/6OH//9Hw9D8/0ejcBSGQ7AP4Z9gbPX/OfS/m/vdKgN0PxOZw5d5909VfyeR31HL1x+xp2JKjDA4j6gIrOyM6EclBKzZto4VFIvFYrFYLBaLxWKxWCwWi8Xyb/ADcPSUWQAoAAA='


@pytest.fixture()
def package_dir(monkeypatch):
    monkeypatch.chdir("tests/data/kube-ui")


@pytest.fixture()
def bad_package_dir(monkeypatch):
    monkeypatch.chdir("tests/data/bad_manifest")

@pytest.fixture()
def empty_package_dir(monkeypatch):
    monkeypatch.chdir("tests/data")


@pytest.fixture(scope="module")
def deploy(deploy_json):
    return json.loads(deploy_json)


@pytest.fixture(scope="module")
def ns_resource(deploy):
    kubeui = deploy["deploy"][0]
    return kubeui['resources'][0]


@pytest.fixture(scope="module")
def rc_resource(deploy):
    kubeui = deploy["deploy"][0]
    return kubeui['resources'][1]


@pytest.fixture(scope="module")
def svc_resource(deploy):
    kubeui = deploy["deploy"][0]
    return kubeui['resources'][2]
