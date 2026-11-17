from pathlib import Path
import shutil
import time

target = Path(input("Enter the target folder: ").strip('"'))
dic = {"Images": [".jpg",".jpeg",".png",".gif"],"Documents": [".pdf",".docx",".txt",".doc",".xlsx"],"Music": [".mp3",".m4a"],"Archives": [".zip",".rar"],"Video": [".mp4","mkv"],"Applications": [".exe" , ".msix"]}
HM = 0

start_time = time.perf_counter()
for file in target.iterdir():
    moved = False
    if not file.is_file(): continue
    for category, exts in dic.items():
        if file.is_file() and file.suffix.lower() in exts:
            Path(target / category).mkdir(exist_ok=True)
            shutil.move(file, target / category / file.name)
            print(f"{file.name} moved to {category}")
            moved = True
            HM += 1
            break
    if moved is False:
        (target / "Other").mkdir(exist_ok=True)
        shutil.move(file, target / "Other" / file.name)
        print(f"{file.name} moved to Other")
        HM += 1
elapsed = time.perf_counter() - start_time
print(f"{HM} files moved")
print(f"Done in {elapsed:.3f} seconds!")


