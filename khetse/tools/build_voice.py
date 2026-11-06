"""Rebuild KhetSe's built-in Hindi voice data.

Takes the eSpeak-NG Emscripten port (@echogarden/espeak-ng-emscripten),
keeps only the files needed for Hindi plus our custom `khetse` voice,
and prints the base64 data blob and the matching loadPackage() file list
that index.html embeds.

Usage:
    npm i @echogarden/espeak-ng-emscripten@0.3.5
    python3 tools/build_voice.py node_modules/@echogarden/espeak-ng-emscripten tools/build
"""
import base64, pathlib, re, sys

pkg = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "node_modules/@echogarden/espeak-ng-emscripten")
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "tools/build")
out.mkdir(parents=True, exist_ok=True)

src = (pkg / "espeak-ng.js").read_text(encoding="utf-8")
data = (pkg / "espeak-ng.data").read_bytes()
voice = (pathlib.Path(__file__).parent / "khetse.voice").read_bytes()

m = re.search(r"loadPackage\(\{files:\[(.*?)\],remote_package_size:(\d+)\}\)", src, re.S)
files = re.findall(r'\{filename:"([^"]*)",start:(\d+),end:(\d+)\}', m.group(1))
CORE = {"hi_dict", "intonations", "phondata", "phonindex", "phontab"}

blob, entries = b"", []
for name, start, end in files:
    if name.split("/")[-1] in CORE or name.endswith("/lang/inc/hi"):
        chunk = data[int(start):int(end)]
        entries.append('{filename:"%s",start:%d,end:%d}' % (name, len(blob), len(blob) + len(chunk)))
        blob += chunk
entries.append('{filename:"/usr/share/espeak-ng-data/voices/!v/khetse",start:%d,end:%d}' % (len(blob), len(blob) + len(voice)))
blob += voice

(out / "espeak-hi.mjs").write_text(
    src[: m.start()] + "loadPackage({files:[%s],remote_package_size:%d})" % (",".join(entries), len(blob)) + src[m.end():],
    encoding="utf-8")
(out / "hi.data.b64").write_text(base64.b64encode(blob).decode())
print(f"Hindi voice package: {len(entries)} files, {len(blob):,} bytes -> {out}")
