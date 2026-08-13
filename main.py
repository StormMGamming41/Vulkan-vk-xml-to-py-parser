
from resolve import topological_sort_structs, build_extension_map
from parser import Registry_Parser

from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

from codegen.emit_handles import emit_handles
from codegen.emit_basetypes import emit_basetypes
from codegen.emit_enums import emit_enums
from codegen.emit_bitmask import emit_bitmasks


registry = Registry_Parser("vk.xml").parse()
from resolve import topological_sort_structs, build_extension_map

registry = Registry_Parser("vk.xml").parse()
struct_order = topological_sort_structs(registry)
extension_map = build_extension_map(registry)
counter = Counter()

out_dir = Path("output")
out_dir.mkdir(exist_ok=True)

(out_dir / "handles.py").write_text(emit_handles(registry))
(out_dir / "basetypes.py").write_text(emit_basetypes(registry))
(out_dir / "enums.py").write_text(emit_enums(registry))
(out_dir / "bitmasks.py").write_text(emit_bitmasks(registry))