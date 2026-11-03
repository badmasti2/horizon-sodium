from pathlib import Path
import json,re,zipfile
root=Path(__file__).resolve().parents[1]
meta=json.loads((root/'horizon-native.json').read_text())
manifest=(root/'mixins'/meta['id']/'horizon-mixin.toml').read_text()
assert re.search(r'^id = "'+re.escape(meta['id'])+r'"$',manifest,re.M)
assert re.search(r'^version = "'+re.escape(meta['version'])+r'"$',manifest,re.M)
dest=root/'dist'/f"{meta['id']}-{meta['version']}.hnmod"
dest.parent.mkdir(exist_ok=True)
files=[root/'horizon-native.json',*sorted((root/'mixins').rglob('*'))]
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for path in files:
  if path.is_file():
   info=zipfile.ZipInfo(path.relative_to(root).as_posix(),date_time=(2026,1,1,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
   z.writestr(info,path.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(dest)
