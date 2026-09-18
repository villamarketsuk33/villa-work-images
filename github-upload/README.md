# Villa Work Images

อัปโหลดเนื้อหาภายในโฟลเดอร์นี้ไปไว้ระดับบนสุดของ repository ใหม่บน branch main
ตั้ง Settings → Pages → Source เป็น GitHub Actions แล้วรัน Publish Villa Work Images
ระบบจะย่อภาพสำหรับ LINE และเผยแพร่แกลเลอรีพร้อมลิงก์สำหรับตั้งค่า VM_WORK_MENU_IMAGE_BASE_URL
ดูรายละเอียดทั้งหมดใน INSTALL_Menu_TH.md ที่มากับ ZIP

Files used by the build: build_images.py, requirements.txt, gallery.html, originals/*.png and .github/workflows/pages.yml.
Build output: _site/index.html, _site/images/*.png, _site/image-manifest.json.
The Apps Script source is installed separately and is not part of this public image site.
