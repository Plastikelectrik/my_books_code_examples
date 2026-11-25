import sys
import pefile

FLAGS = {
    0x0020: "HIGH_ENTROPY_VA",
    0x0040: "DYNAMIC_BASE (ASLR)",
    0x0100: "NX_COMPAT (DEP)",
    0x4000: "GUARD_CF",
}

pe = pefile.PE(sys.argv[1])
opt = pe.OPTIONAL_HEADER
print(f"machine   {pe.FILE_HEADER.Machine:#06x}")
print(f"magic     {opt.Magic:#06x}")
print(f"imagebase {opt.ImageBase:#x}")
print(f"entry     {opt.AddressOfEntryPoint:#x}")
for bit, name in FLAGS.items():
    on = opt.DllCharacteristics & bit
    print(f"{name:20} {'yes' if on else 'no'}")
for s in pe.sections:
    name = s.Name.rstrip(b"\0").decode()
    print(f"section {name:8} size {s.SizeOfRawData}")
for entry in getattr(pe, "DIRECTORY_ENTRY_IMPORT", []):
    names = [i.name.decode() for i in entry.imports
             if i.name]
    print(entry.dll.decode(), len(names), "imports")
for dbg in getattr(pe, "DIRECTORY_ENTRY_DEBUG", []):
    pdb = getattr(dbg.entry, "PdbFileName", None)
    if pdb:
        print("pdb path", pdb.rstrip(b"\0").decode())
