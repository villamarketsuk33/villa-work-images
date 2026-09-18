"""Build public LINE artwork on GitHub Actions; preserve the source originals."""
from pathlib import Path
from html import escape
import json

from PIL import Image

ROOT = Path(__file__).resolve().parent
MENU = [
    ("villa-fondue", "Villa Fondue", "วิลล่า ฟองดู · แจ้งปัญหา"),
    ("work-points-lotto", "ตรวจสอบงาน", "คะแนน · แลกล๊อตโต้"),
    ("repair-maintenance", "แจ้งซ่อม", "แผนกช่าง"),
    ("product-details-scanner", "ตรวจสอบรายละเอียดสินค้า", "สแกนสินค้าเพื่อตรวจสอบข้อมูล"),
    ("morningwalk-submission", "ส่งงาน Morningwalk", "เดินตรวจสาขาประจำวัน"),
    ("daily-summary", "สรุปรายงานวันนี้", "ดูสรุปรายงานประจำวัน"),
]


def build():
    output = ROOT / "_site"
    images = output / "images"
    images.mkdir(parents=True, exist_ok=True)
    manifest = []
    cards = []
    for menu_id, title, subtitle in MENU:
        with Image.open(ROOT / "originals" / (menu_id + ".png")) as original:
            picture = original.convert("RGB")
            picture.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
            target = images / (menu_id + ".png")
            picture.save(target, format="PNG", optimize=True)
            width, height = picture.size
        if max(width, height) > 1024 or target.stat().st_size > 10 * 1024 * 1024:
            raise ValueError("Image exceeds LINE limits: " + menu_id)
        manifest.append({"id": menu_id, "width": width, "height": height, "bytes": target.stat().st_size})
        cards.append('<article><img src="images/' + menu_id + '.png" alt="' + escape(title) + '">'
                     '<h2>' + escape(title) + '</h2><p>' + escape(subtitle) + '</p>'
                     '<a href="images/' + menu_id + '.png" download>ดาวน์โหลดรูป</a></article>')
    (output / "image-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    template = (ROOT / "gallery.html").read_text(encoding="utf-8")
    (output / "index.html").write_text(template.replace("<!-- GALLERY_CARDS -->", "\n".join(cards)), encoding="utf-8")
    print(json.dumps({"images": manifest, "output": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    build()
